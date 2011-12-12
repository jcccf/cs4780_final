import numpy as np
from sklearn.decomposition import PCA
from sklearn import linear_model
from sklearn import metrics
import rpy2.robjects as R
import MSVMLight
import Converters

class MRegression:
  
  def __init__(self, filename, select_y = 'INCMIN', select_x = ['DOSAGE', 'SEX', 'RACE_1']):
    self.select_x = select_x
    self.select_y = select_y
    self.train_file, self.val_file = Converters.split_orangetab_into_2(filename)
    self.X, self.Y = self.__read_into_array(self.train_file)
    self.Xv, self.Yv = self.__read_into_array(self.val_file)
    # self.X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    # self.Y = [-1,-1,-1,1,1,1]

  def __read_into_array(self, filename):
    select_y_index = 0
    select_x_indices = []
    x_array, y_array = [], []
    with open(filename, 'r') as f:
      lines = f.readlines()
      if len(lines) == 1:
        lines = lines[0].split('\r')
        lines = [l+'\n' for l in lines]
      attributes = lines[0].replace('\n','').split('\t')
      for x in self.select_x:
        select_x_indices.append(attributes.index(x))
      select_y_index = attributes.index(self.select_y)
      for i in range(3, len(lines)):
        vals = lines[i].replace('\n', '').split('\t')
        if len([j for j in select_x_indices if len(vals[j]) == 0]) == 0: # Eliminate any rows with missing values
          x_array.append([float(vals[j]) for j in select_x_indices])
          y_array.append(float(vals[select_y_index]))
    return [np.array(x_array), y_array]

  def to_svmlight(self, out_filename):
    with open(out_filename+".train", 'w') as f:
      for j, y in enumerate(self.Y):
        line = '%s' % y
        for i, x in enumerate(self.X[j]):
          line += ' %s:%s' % (i+1,x)
        f.write(line+"\n")
    with open(out_filename+".val", 'w') as f:
      for j, y in enumerate(self.Yv):
        line = '%s' % y
        for i, x in enumerate(self.Xv[j]):
          line += ' %s:%s' % (i+1,x)
        f.write(line+"\n")
  
  def svm_regression(self, out_filename, delete=True):
    self.to_svmlight(out_filename)
    
    train_file = out_filename+".train"
    test_file = out_filename+".val"
    model_file = train_file+".mod"
    classified_file = test_file+".class"
    classified_file_original = test_file+".class_orig"
    
    for t in [0]:
      print "---"
      print "SVM Regression..."
      MSVMLight.learn(train_file, model_file, z='r', t=t)
      print "Learnt Model"
      MSVMLight.classify(test_file, model_file, classified_file)
      MSVMLight.classify(train_file, model_file, classified_file_original)
    
      with open(test_file, 'r') as f:
        ytrue = f.readlines()
        ytrue = [float(l.split(' ', 1)[0]) for l in ytrue]
    
      with open(classified_file, 'r') as f:
        yguess = f.readlines()
        yguess = [float(l.replace('\n', '')) for l in yguess]
        
      with open(train_file, 'r') as f:
        ytrue_orig = f.readlines()
        ytrue_orig = [float(l.split(' ', 1)[0]) for l in ytrue_orig]

      with open(classified_file_original, 'r') as f:
        yguess_orig = f.readlines()
        yguess_orig = [float(l.replace('\n', '')) for l in yguess_orig]
    
      print metrics.r2_score(ytrue, yguess), metrics.r2_score(ytrue_orig, yguess_orig)
      print metrics.mean_square_error(ytrue, yguess), metrics.mean_square_error(ytrue_orig, yguess_orig)
      print "---"

  def pca(self, n_components=None, verbose=False):
    num_comps = len(self.X[0]) if n_components == None else n_components
    self.pca = PCA(n_components=num_comps)
    self.pca.fit(self.X)
    self.Xt = self.pca.transform(self.X)
    self.Xvt = self.pca.transform(self.Xv)
    if verbose:
      print "---"
      print "PCA..."
      print "Explained Variance"
      print self.pca.explained_variance_ratio_
      print "Components"
      print self.pca.components_
      print "---"
  
  def regression(self, type='PCA', verbose=False):
    self.lm = linear_model.LinearRegression()
    if type == 'PCA':
      X = self.Xt
      Xv = self.Xvt
    else:
      X = self.X
      Xv = self.Xv
    self.lm.fit(X, self.Y)
    Ypv = self.lm.predict(Xv)
    Yp = self.lm.predict(X)
    if verbose:
      print "---"
      print type, "Regression..."
      print "R2 Score (Val / Test)"
      print metrics.r2_score(self.Yv, Ypv), metrics.r2_score(self.Y, Yp)
      print "MSE (Val / Test)"
      print metrics.mean_square_error(self.Yv, Ypv), metrics.mean_square_error(self.Y, Yp)
      print "Coefficients"
      print self.lm.coef_
      print "Intercept"
      print self.lm.intercept_
      print "---"
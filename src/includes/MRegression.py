import numpy as np
from sklearn.decomposition import PCA
from sklearn import linear_model
from sklearn import metrics
import rpy2.robjects as R
import MSVMLight
import Converters
import os.path

np.set_printoptions(threshold='nan')

class MRegression:
  
  def __init__(self, filename, select_y = 'INCMIN', select_x = ['DOSAGE', 'SEX', 'RACE_1']):
    self.base_file = '../data_reg/' + os.path.basename(filename).split('.')[0]
    self.select_x = select_x
    self.select_y = select_y
    self.train_file, self.val_file = Converters.split_orangetab_into_2(filename, randomize=True)
    self.X, self.Y = self.__read_into_array(self.train_file, remove_constants=True)
    self.Xv, self.Yv = self.__read_into_array(self.val_file, remove_constants=False)
    # self.X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    # self.Y = [-1,-1,-1,1,1,1]
    
  def to_csv(self, filename):
    with open(filename, 'w') as f:
      header = "%s" % self.select_y
      for x in self.select_x:
        header += ",%s" % x
      f.write(header+"\n")
      for i,x in enumerate(self.X):
        s = "%s" % self.Y[i]
        s += "".join([","+str(x2) for x2 in x])
        f.write(s+"\n")

  def __read_into_array(self, filename, remove_constants=True):
    select_y_index = 0
    select_x_indices = []
    x_array, y_array = [], []
    with open(filename, 'r') as f:
      lines = f.readlines()
      if len(lines) == 1:
        lines = lines[0].split('\r')
        lines = [l+'\n' for l in lines]
      attributes = lines[0].replace('\n','').split('\t')
      # print lines[0]
      # print attributes
      select_x_new = list(self.select_x)
      for x in self.select_x:
        if x not in attributes: # If an attribute specified doesn't exist
          print "Removing Attribute ", x
          select_x_new.remove(x)
        else:
          select_x_indices.append(attributes.index(x))
      self.select_x = select_x_new
      select_y_index = attributes.index(self.select_y)
      for i in range(3, len(lines)):
        vals = lines[i].replace('\n', '').split('\t')
        if len([j for j in select_x_indices if len(vals[j]) == 0]) == 0: # Eliminate any rows with missing values
          x_array.append([float(vals[j]) for j in select_x_indices])
          y_array.append(float(vals[select_y_index]))
          
    a = np.array(x_array)
    
    if remove_constants:
      a = np.transpose(a)
      i = 0
      eyes = []
      for b in a:
        if b.std() == 0:
          eyes.append(i)
        i += 1
      print "Removed sd=0 attributes ", eyes
      a = np.delete(a, eyes, 0)
      sx_new = list(self.select_x)
      for eye in eyes:
        print self.select_x[eye]
        sx_new.remove(self.select_x[eye])
      self.select_x = sx_new
      a = np.transpose(a)
    
    return [a, y_array]

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
    
    print "Writing output to " + self.base_file+"_svm.txt"
    with open(self.base_file+"_svm.txt", 'w') as fx:
      d = 1
      for t in [0]: #[0, 1, 1, 1, 1, 1, 2]:
        print "---"
        print "SVM Regression..."
        if t != 1:
          MSVMLight.learn(train_file, model_file, z='r', t=t)
        else:
          MSVMLight.learn(train_file, model_file, z='r', t=t, d=d)
          d += 1
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
        
        fx.write("---t=%d d=%d\n" % (t, d))
        fx.write("R2 (val/test)\n")
        fx.write("%f %f \n" % (metrics.r2_score(ytrue, yguess), metrics.r2_score(ytrue_orig, yguess_orig)))
        fx.write("MSE (val/test)\n")
        fx.write("%f %f \n" % (metrics.mean_square_error(ytrue, yguess), metrics.mean_square_error(ytrue_orig, yguess_orig)))
        fx.write("---\n")

  def pca(self, n_components=None):
    num_comps = len(self.X[0]) if n_components == None else n_components
    self.pca = PCA(n_components=num_comps)
    self.pca.fit(self.X)
    self.Xt = self.pca.transform(self.X)
    self.Xvt = self.pca.transform(self.Xv)
    print "Writing output to " + self.base_file+"_pca_comp.txt"
    with open(self.base_file+"_pca_comp.txt", 'w') as f:
      f.write("---\n")
      f.write("PCA...\n")
      f.write("Explained Variance\n")
      f.write("%s\n" % self.pca.explained_variance_ratio_)
      f.write("Components\n")
      for j, c in enumerate(self.pca.components_):
        f.write("---%d---\n" % j)
        comps = []
        for i, n in enumerate(c):
          comps.append((n,self.select_x[i]))
        for n, w in sorted(comps, key=lambda x:-x[0]):
          f.write("%e \t %s\n" % (n, w))
      f.write("------\n")
  
  def regression(self, type='PCA'):
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
    print "Writing output to " + self.base_file+"_"+type+".txt"
    with open(self.base_file+"_"+type+".txt", 'w') as f:
      if type == 'Linear':
        f.write("---\n")
        f.write("Linear Components\n")
        for i, x in enumerate(self.select_x):
          
          f.write("%d\t%s\n" % (i,x))
      f.write("---\n")
      f.write("%s Regression...\n" % type)
      f.write("R2 Score (Val / Test) \n")
      f.write("%f %f \n" % (metrics.r2_score(self.Yv, Ypv), metrics.r2_score(self.Y, Yp)))
      f.write("MSE (Val / Test)")
      f.write("%f %f \n" % (metrics.mean_square_error(self.Yv, Ypv), metrics.mean_square_error(self.Y, Yp)))
      f.write("Coefficients\n")
      f.write("%s\n" % self.lm.coef_)
      f.write("Intercept\n")
      f.write("%s\n" % self.lm.intercept_)
      f.write("---\n")      
      # Do R Linear Regression
      lm_string = "y ~ x0"
      data_frame_val = {}
      data_frame_train = {}
      for i in range(len(self.select_x)):
        R.globalenv['x%d' % i] = R.FloatVector(X[:,i].tolist())
        data_frame_val['x%d' % i] = R.FloatVector(Xv[:,i].tolist())
        #data_frame_train['x%d' % i] = R.FloatVector(X[:,i].tolist())
        if i > 0:
          lm_string += " + x%d" % i
      R.globalenv['y'] = R.FloatVector(self.Y)
      data_frame_val['y'] = R.FloatVector(self.Yv)
      #data_frame_train['y'] = R.FloatVector(self.Y)
      data_frame_val = R.DataFrame(data_frame_val)
      #data_frame_train = R.DataFrame(data_frame_train)
      #R.r.attach(data_frame_train)
      fit = R.r.lm(lm_string)
      
      aic = R.r.AIC(fit)
      
      f.write("%s\n" % R.r.summary(fit))
      f.write("%s\n" % aic)
      
      #R.r.attach(data_frame_val)
      
      # Print Test R2 Value
      predicted = R.r.predict(fit)
      YpR = []
      for p in predicted:
        YpR.append(p)
      f.write("Test: %s\n" % metrics.r2_score(self.Y, YpR))
      
      # Print Validation R2 Value
      for i in range(len(self.select_x)):
        R.globalenv['x%d' % i] = R.FloatVector(Xv[:,i].tolist())
      R.globalenv['y'] = R.FloatVector(self.Yv)
      predicted = R.r.predict(fit, newdata=data_frame_val)
      YpvR = []
      for p in predicted:
        YpvR.append(p)
      f.write("Val: %s\n" % metrics.r2_score(self.Yv, YpvR))
      # fit2 = R.r.lm('y ~ x1 + x2 + x3')
      # print R.r.anova(fit, fit2)
      
      #print aic[0]
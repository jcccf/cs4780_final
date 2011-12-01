import orange, orngBayes, orngTree, orngTest, orngStat, orngWrap, commands, math

class OrangeClassifiers:
  def __init__(self, orangeDataFile, orangeValFile):
    self.data = orange.ExampleTable(orangeDataFile)
    self.valdata = orange.ExampleTable(orangeValFile)
    if len(self.data.domain.classVar.values) == 2:
      self.is_binary = True
    else:
      self.is_binary = False
      
  def print_decision_tree(self, measure='infoGain', mForPruning=2, maxMajority=0.8, minSubset=10, minExamples=10, suffix='demo'):
    classifier = orngTree.TreeLearner(self.data, measure=measure, sameMajorityPruning=1, mForPruning=mForPruning, maxMajority=maxMajority, minSubset=minSubset, minExamples=minExamples)
    stringy = orngTree.dumpTree(classifier, maxDepth=3).split('\n')
    # stringy = [s for s in stringy if "null node" not in s]
    orngTree.printDot(classifier, fileName='../data_stat/dtree_%s.dot' % suffix, internalNodeShape="ellipse", leafShape="box", maxDepth=2)
    print commands.getoutput('dot -Tsvg ../data_stat/dtree_%s.dot > ../data_stat/dtree_%s.svg' % (suffix, suffix))
    print "\n".join(stringy)
    self.output_classified(classifier, '../data_stat/dtree_%s.txt' % suffix)
  
  def print_knn(self, k=10):
    classifier = orange.kNNLearner(self.data, k=k)
    self.output_classified(classifier, '../data_stat/knn.txt')
  
  def output_classified(self, classifier, filename):
    with open(filename, 'w') as f:
      for i in range(0, len(self.valdata)):
        f.write('%s\n' % classifier(self.valdata[i]))
  
  def print_bayes(self):
    for i, dist in enumerate(orngBayes.BayesLearner(self.data).conditionalDistributions):
      print self.data.domain[i]
      print dist
    classifier = orange.BayesLearner(self.data)
    self.output_classified(classifier, '../data_stat/bayes.txt')
    
  def print_linear_svm(self):
    classifier = orange.LinearLearner(self.data)
    if self.is_binary:
      print "Attribute weights"
      for attr, w in  zip(self.data.domain.attributes, classifier.weights[0]):
          print "\t%s: %.3f " % (attr.name, w)
    else:
      for i, cls_name in enumerate(self.data.domain.classVar.values):
          print "Attribute weights for %s vs. rest classification:\n" % cls_name,
          for attr, w in  zip(self.data.domain.attributes, classifier.weights[i]):
              print "\t%s: %.3f " % (attr.name, w)
    self.output_classified(classifier, '../data_stat/linsvm.txt')
  
  def cross_validate(self):
    bayes = orngBayes.BayesLearner()
    kmeans = orange.kNNLearner(k=55)
    tree = orngTree.TreeLearner(mForPruning=5, maxMajority=1.0, minExamples=2, minSubset=2, measure='gini') # orngTree.TreeLearner(, mForPruning=2)
    lin_svm = orange.LinearLearner()
    bayes.name = "bayes"
    tree.name = "c4.5"
    kmeans.name = "kmeans"
    lin_svm.name = "lin_svm"
    learners = [bayes, tree, lin_svm, kmeans]
    results = orngTest.crossValidation(learners, self.data, folds=10)
    cm = orngStat.confusionMatrices(results)

    print "-----"
    print "Learner  CA     IS     Brier  AUC    TP     FP     FN     TN     "
    for i in range(len(learners)):
      if not self.is_binary:
        print "%-8s %-5.3f  %-5.3f  %-5.3f  %-5.3f" % (learners[i].name, orngStat.CA(results)[i], \
          orngStat.IS(results)[i], orngStat.BrierScore(results)[i], orngStat.AUC(results)[i])
      else:
        print "%-8s %-5.3f  %-5.3f  %-5.3f  %-5.3f  %-5d  %-5d  %-5d  %-5d" % (learners[i].name, \
          orngStat.CA(results)[i], orngStat.IS(results)[i], 
          orngStat.BrierScore(results)[i], orngStat.AUC(results)[i], cm[i].TP, cm[i].FP, cm[i].FN, cm[i].TN)
    print "-----\n\tCA=Classification Accuracy\n\tIS=Information Score\n\tBrier=Brier score\n\tAUC=Area Under ROC curve\n\tTP=True Positives, FP=False Positives, FN=False Negatives, TN=True Negatives"

# print "Possible classes:", data.domain.classVar.values
# print "Probabilities for democrats:"
# for i in range(5):
#     p = tree(data[i], orange.GetProbabilities)
#     print "%d: %5.3f (originally %s)" % (i+1, p[1], data[i].getclass())

class OrangeTuners:
  def __init__(self, filename):
    self.filename = filename
    self.data = orange.ExampleTable(self.filename)
    
  def tune_decision_tree(self):
    tree = orngTree.TreeLearner(sameMajorityPruning=True)
    # tunedTree = orngWrap.Tune1Parameter(object=tree, parameter='mForPruning', \
    #     values=[0, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100], verbose=2)
    tunedTree = orngWrap.TuneMParameters(object=tree, parameters = [
      ('mForPruning', [0, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]), 
      ('maxMajority', [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]),
      ('minExamples', [0, 1, 2]), # ('minExamples', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
      ('minSubset', [0, 1, 2]), # ('minSubset', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
      ('measure', ['infoGain', 'gainRatio', 'gini', 'relief'])
    ], folds=10, verbose=2)
    
    self.tunedTree = tunedTree

    return tunedTree(self.data)
    
  def tune_knn(self):
    knn = orange.kNNLearner()
    tunedKnn = orngWrap.TuneMParameters(object=knn, parameters = [
      ('k', range(1, 2*int(math.sqrt(len(self.data)))))
    ], folds=10, verbose=2)
  
    return tunedKnn(self.data)
import orange, orngBayes, orngTree, orngTest, orngStat, orngWrap

class OrangeClassifiers:
  def __init__(self, orangeDataFile):
    self.data = orange.ExampleTable(orangeDataFile)
    if len(self.data.domain.classVar.values) == 2:
      self.is_binary = True
    else:
      self.is_binary = False
      
  def print_decision_tree(self, measure='infoGain', mForPruning=2, maxMajority=0.8, minSubset=10, minExamples=10):
    stringy = orngTree.dumpTree(orngTree.TreeLearner(self.data, measure=measure, sameMajorityPruning=1, mForPruning=mForPruning, maxMajority=maxMajority, minSubset=minSubset, minExamples=minExamples)).split('\n')
    stringy = [s for s in stringy if "null node" not in s]
    print "\n".join(stringy)
  
  def print_bayes(self):    
    for i, dist in enumerate(orngBayes.BayesLearner(self.data).conditionalDistributions):
      print self.data.domain[i]
      print dist
    
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
  
  def cross_validate(self):
    bayes = orngBayes.BayesLearner()
    kmeans = orange.kNNLearner(k=10)
    tree = orngTree.TreeLearner(sameMajorityPruning=1, mForPruning=2) # orngTree.TreeLearner(, mForPruning=2)
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
    
  def tune_decision_tree(self):
    self.data = orange.ExampleTable(self.filename)
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
    
  def decision_tree_info(self):
    classifier = self.tunedTree(self.data)
    orngTree.dumpTree(classifier, maxDepth=3)
    print "\n\n\n#\n\n\n"
    for i in range(0, len(self.data)):
      print classifier(self.data[i])
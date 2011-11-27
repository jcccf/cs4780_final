from includes import *

#
# Orange Machine Learning Algorithms
#

oc = OrangeML.OrangeClassifiers('../data/data_orange_full_bin_4.tab')
# oc.cross_validate()
# oc.print_linear_svm()
oc.print_decision_tree(measure='infoGain', mForPruning=2, maxMajority=0.8, minSubset=10, minExamples=10)
# oc.print_bayes()


#
# HW Decision Tree (Modified to Allow Discrete Attributes)
#

# # attr_list is the list of attributes, dc_list is a boolean list of whether a certain attribute
# # at a particular index is discrete or not, examples is a list of examples
# ci, attr_list, dc_list, examples = Loaders.load_dcdata("../data/voting.tab")
# dt = DecisionTree.DecisionTree(examples, dc_list, splitting_criterion='ce')
# # prediction_error returns (# correct, # wrong, correct, # examples, % correct, % wrong)
# print dt.prediction_error(examples)
# dt.print_tree()


#
# Possible Converters to Implement
#

#Converters.base_to_orangetab()
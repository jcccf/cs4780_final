from includes import *
import orngTree

#
# Orange Machine Learning Algorithms
#

# oc = OrangeML.OrangeClassifiers('../data/data_orange_full_bin_4.tab')
# oc.cross_validate()
# oc.print_linear_svm()
# oc.print_decision_tree(measure='infoGain', mForPruning=2, maxMajority=0.8, minSubset=10, minExamples=10)
# oc.print_bayes()

#
# Orange Tuners
#
ot = OrangeML.OrangeTuners('../data/do_20111129_b_v_u_bal_noincmax_nopcs.tab')
ot.tune_decision_tree()
ot.decision_tree_info()

#
# SVMLight File Converters
#
# Converters.orangetab_to_svmlight('../data/do_20111129_b_v_u_bal_noincmax_nopcs.tab', '../data_svm/do_20111129_b_v_u_bal_noincmax_nopcs.train')

#
# SVMLight Tuner
#
# MSVMLight.tune_parameters('../data_svm/do_20111129_b_v_u_bal_noincmax_nopcs.train')

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
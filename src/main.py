from includes import *

#
# Orange Machine Learning Algorithms
#

# oc = OrangeML.OrangeClassifiers('../data/do_20111129_b_v_u_bal_noincmax_nopcs.tab')
# oc.cross_validate()
# oc.print_linear_svm()
# oc.print_decision_tree(mForPruning=0.5, maxMajority=0.8, minExamples=0, minSubset=1, measure='relief')
# oc.print_bayes()
# oc.print_knn(k=28)

#
# Orange Tuners
#
# ot = OrangeML.OrangeTuners('../data/do_20111130_b_v_u_bal_demo_train.tab')
# ot.tune_decision_tree()
# ot.decision_tree_info()
# ot.tune_knn()

#
# SVMLight Tuner
#
MSVMLight.tune_parameters('../data_svm/do_20111130_b_v_u_bal_demo_train.train')

#
# Significance Tests
#
# Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/dtree.txt', '../data_stat/svm.txt', verbose=True)
# Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/dtree.txt', '../data_stat/knn.txt', verbose=True)
# Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/dtree.txt', '../data_stat/bayes.txt', verbose=True)

#
# Example File Balanced Label Classes
#
# Converters.balance_orangetab('../data/do_20111130_b_v_u.tab', '../data/do_20111130_b_v_u_bal.tab')
# Converters.split_orangetab_into_2('../data/do_20111130_b_v_u_bal_crime.tab')
# Converters.split_orangetab_into_2('../data/do_20111130_b_v_u_bal_demo.tab')
# Converters.split_orangetab_into_2('../data/do_20111130_b_v_u_bal_base.tab')

#
# SVMLight File Converters
#
# Converters.orangetab_to_svmlight('../data/do_20111130_b_v_u_bal_demo_train.tab', '../data_svm/do_20111130_b_v_u_bal_demo_train.train')
# Converters.orangetab_to_svmlight('../data/do_20111130_b_v_u_bal_crime_train.tab', '../data_svm/do_20111130_b_v_u_bal_crime_train.train')
# Converters.orangetab_to_svmlight('../data/do_20111130_b_v_u_bal_base_train.tab', '../data_svm/do_20111130_b_v_u_bal_base_train.train')


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
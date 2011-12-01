from includes import *

#
# Orange Machine Learning Algorithms
#

oc = OrangeML.OrangeClassifiers('../data/do_20111130_b_v_u_bal_base_train.tab', '../data/do_20111130_b_v_u_bal_base_val.tab')
oc.cross_validate()
oc.print_linear_svm()
oc.print_bayes()

oc.print_decision_tree(mForPruning=100, maxMajority=0.8, minExamples=0, minSubset=0, measure='relief', suffix='demo')
oc.print_knn(k=42)

# oc.print_decision_tree(mForPruning=100, maxMajority=1.0, minExamples=2, minSubset=2, measure='relief', suffix='demo')
# oc.print_knn(k=28)

# oc.print_decision_tree(mForPruning=5, maxMajority=1.0, minExamples=2, minSubset=2, measure='gini', suffix='demo')
# oc.print_knn(k=55)

#
# Orange Tuners
#
# ot = OrangeML.OrangeTuners('../data/do_20111130_b_v_u_bal_base_train.tab')
# ot.tune_decision_tree()
# ot.tune_knn()

#
# SVMLight Tuner
#
# MSVMLight.tune_parameters('../data_svm/do_20111130_b_v_u_bal_demo_train.train')

#
# Significance Tests
#
# Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/dtree.txt', '../data_stat/svm.txt', verbose=True)
Converters.write_actual_labels('../data/do_20111130_b_v_u_bal_crime_val.tab', '../data_stat/original.txt')
Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/dtree_demo.txt', '../data_stat/linsvm.txt', verbose=True)
Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/dtree_demo.txt', '../data_stat/knn.txt', verbose=True)
Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/dtree_demo.txt', '../data_stat/bayes.txt', verbose=True)
Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/linsvm.txt', '../data_stat/knn.txt', verbose=True)
Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/linsvm.txt', '../data_stat/bayes.txt', verbose=True)
Validators.binomial_sign_test('../data_stat/original.txt', '../data_stat/knn.txt', '../data_stat/bayes.txt', verbose=True)

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
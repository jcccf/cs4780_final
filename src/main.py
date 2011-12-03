from includes import *

#
# CONSTANTS
#
TRAIN_FILE = '../data/do_20111201_b_v_u_bal_demo_train.tab'
VAL_FILE = '../data/do_20111201_b_v_u_bal_demo_val.tab'

#
# Example File Balanced Label Classes and so on
#
# Converters.balance_orangetab('../data/do_20111201_b_v_u.tab', '../data/do_20111201_b_v_u_bal.tab')
# Converters.normalize_orange('../data/do_20111201_b_v_u_bal.tab','../data/do_20111201_b_v_u_bal_norm.tab')
# Converters.split_orangetab_into_2('../data/do_20111201_b_v_u_bal_crime.tab')
# Converters.split_orangetab_into_2('../data/do_20111201_b_v_u_bal_demo.tab')
# Converters.split_orangetab_into_2('../data/do_20111201_b_v_u_bal_base.tab')

#
# SVMLight File Converters
#
# Converters.orangetab_to_svmlight('../data/do_20111201_b_v_u_bal_demo_train.tab', '../data_svm/do_20111201_b_v_u_bal_demo_train.train')
# Converters.orangetab_to_svmlight('../data/do_20111201_b_v_u_bal_crime_train.tab', '../data_svm/do_20111201_b_v_u_bal_crime_train.train')
# Converters.orangetab_to_svmlight('../data/do_20111201_b_v_u_bal_base_train.tab', '../data_svm/do_20111201_b_v_u_bal_base_train.train')
# Converters.orangetab_to_svmlight('../data/do_20111201_b_v_u_bal_demo_val.tab', '../data_svm/do_20111201_b_v_u_bal_demo_val.val')
# Converters.orangetab_to_svmlight('../data/do_20111201_b_v_u_bal_crime_val.tab', '../data_svm/do_20111201_b_v_u_bal_crime_val.val')
# Converters.orangetab_to_svmlight('../data/do_20111201_b_v_u_bal_base_val.tab', '../data_svm/do_20111201_b_v_u_bal_base_val.val')

#
# Tuners
#
# ot = OrangeML.OrangeTuners(TRAIN_FILE)
# ot.tune_decision_tree()
# ot.tune_knn()
# MSVMLight.tune_parameters(TRAIN_FILE)

#
# Cross-validation and so on
#
attrs = { # Attributes to set after tuning
  'mForPruning': 100, # DTree
  'maxMajority': 0.8, # DTree
  'minExamples': 1, # DTree
  'minSubset': 2, # DTree
  'measure': 'relief', # DTree
  'k': 42 # KNN
}
# oc = OrangeML.OrangeClassifiers(TRAIN_FILE, VAL_FILE, attrs)
# oc.cross_validate()
# oc.print_linear_svm()
# oc.print_log_reg()
# oc.print_bayes()
# oc.print_decision_tree(suffix='demo')
# oc.print_knn()

#
# Significance Tests
#
# Converters.write_actual_labels(VAL_FILE, '../data_stat/original.txt')
Validators.binomial_sign_test_multiple('../data_stat/original.txt', [
  '../data_stat/dtree_demo.txt',
  '../data_stat/linsvm.txt',
  '../data_stat/logreg.txt',
  '../data_stat/knn.txt',
  '../data_stat/bayes.txt'
], verbose=True)

#
# IGNORE ALL BELOW
#

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
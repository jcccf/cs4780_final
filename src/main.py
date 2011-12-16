from includes import Converters, DecisionTree, MSVMLight, OrangeML, Validators

#
# CONSTANTS
#
TRAIN_FILE = '../data/do_20111201_b_v_u_bal_demo_train.tab'
TRAIN_FILE_SVM = '../data_svm/do_20111201_b_v_u_bal_demo_train.train'
VAL_FILE = '../data/do_20111201_b_v_u_bal_demo_val.tab'
VAL_FILE_SVM = '../data_svm/do_20111201_b_v_u_bal_demo_val.val'

#
# Example File Balanced Label Classes and so on
#
#Converters.balance_orangetab('../data/do_20111201_b_v_u_demo.tab', '../data/do_20111201_b_v_u_bal_demo.tab')
# Converters.normalize_orange('../data/do_20111201_b_v_u_bal.tab','../data/do_20111201_b_v_u_bal_norm.tab')
#Converters.split_orangetab_into_2('../data/do_20111201_b_v_u_bal_demo.tab', randomize=True)

#
# SVMLight File Converters
#
#Converters.orangetab_to_svmlight(TRAIN_FILE, TRAIN_FILE_SVM)
#Converters.orangetab_to_svmlight(VAL_FILE, VAL_FILE_SVM)

#
# Tuners
#
#ot = OrangeML.OrangeTuners(TRAIN_FILE)
#ot.tune_decision_tree()
#ot.tune_knn()
#MSVMLight.tune_parameters(TRAIN_FILE_SVM)
#MSVMLight.get_cross_val_accuracy(TRAIN_FILE_SVM, num=10, c=None, j=None, t=None, d=None, g=None, verbose=False)

#
# Cross-validation and so on
#
"""attrs = { # Attributes to set after tuning
  'mForPruning': 100, # DTree
  'maxMajority': 0.8, # DTree
  'minExamples': 1, # DTree
  'minSubset': 2, # DTree
  'measure': 'relief', # DTree
  'k': 42 # KNN
}"""
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
"""Converters.write_actual_labels(VAL_FILE, '../data_stat/original.txt')
Validators.binomial_sign_test_multiple('../data_stat/original.txt', [
  '../data_stat/dtree_demo.txt',
  '../data_stat/linsvm.txt',
  '../data_stat/logreg.txt',
  '../data_stat/knn.txt',
  '../data_stat/bayes.txt',
  '../data_stat/svmlight.txt'
], verbose=True)"""

#
# Precision and Recall Calculation
#
Converters.write_actual_labels(VAL_FILE, '../data_stat/original.txt')
Validators.precision_recall_multiple('../data_stat/original.txt', [
  '../data_stat/dtree_demo.txt',
  '../data_stat/linsvm.txt',
  '../data_stat/logreg.txt',
  '../data_stat/knn.txt',
  '../data_stat/bayes.txt',
  '../data_stat/svmlight.txt'
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
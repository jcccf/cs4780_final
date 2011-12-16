Predicting Criminal Sentences
=============================
jc882, yl477, jp624

Where's the raw data that we used in our report?
================================================
In raw_data/

Requirements
============
* Python 2.7+ (*incompatible with Python 3.x)
* pip (a package management system for Python)
* numpy and scipy (pip install numpy, pip install scipy)
* Orange (pip install orange)
* scikit-learn (pip install sklearn)
* R and rpy2 (pip install rpy2)

File Structure
==============
* bin/ - contains SVM binaries
* data/ - contains (sample) data for learning
* data_reg/ - contains output for linear/svm regression
* data_stat/ - contains output for doing the binomial sign test
* data_svm/ - contains SVMLight-compatible data files
** data/voting.tab - sample data (binary decision variable)
** data/voting_3class.tab - sample data (3-class decision variable)
* src/ - code to run
* src/includes - helper methods and classes

How to use
==========
* You should only need to use src/main.py and src/main_reg.py to figure out how to perform learning on the data (run it to see!)
* Add svm_light binaries to the bin/ folder (create it if it doesn't exist)
* Install all the packages listed in the requirements and ensure that they are working
* Many functions assume the data in the first column is the class/label - so make sure that's the case!

Creating an Example File
========================
1. Parse.py can be used and configured from the command line
2. Type python parse.py --help to see all the possible options available to generate data

Manipulating the Example File
=========================
1. Get output from parse.py
2. Use Converters.split_orangetab_into_2 to split the dataset into 2 - training and validation.
3. Use Converters.orangetab_to_svmlight to convert an orange file into an SVMLight-compatible format.

Tuning
======
1. Should be self-explanatory. Set the TRAIN_FILE to the training dataset and VAL_FILE to the validation dataset, and make a note of the optimal parameters, and the classification accuracy for that set of optimal parameters.

Output
======
1. Knowing the optimal parameters, the attrs variable, and run oc.cross_validate().

Sign Test
=========
1. Run print_linear_svm, print_decision_tree, and so on to print out each algorithm's predicted labels to /data_svm.
2. You also need to run Converters.write_actual_labels to print the true labels.
3. Validators.binomial_sign_test can then be used on the true labels, and predicted labels from 2 algorithms, to see if one of them performs better than the other.
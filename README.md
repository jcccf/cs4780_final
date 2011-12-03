Requirements
============
* Python 2.7+
* pip (a package management system for Python)
* Orange (pip install orange)

File Structure
==============
* bin/ - contains SVM binaries
* data/ - contains (sample) data for learning
** data/voting.tab - sample data (binary decision variable)
** data/voting_3class.tab - sample data (3-class decision variable)
* src/ - code to run
* src/includes - helper methods and classes

How to use
==========
* Should only need to use src/main.py to figure out how to perform learning on the data (run it to see!)
* add svm_light binaries to the bin folder (create it if it doesn't exist)

* A lot of functions assume the data in the first column is the class/label - so make sure that's the case!

Creating the Example File
=========================
0. Get output from parse.py
1. Use Converters.balance_orangetab to make the # of examples in each class equal.
2. Use Converters.normalize_orange to normalize the values of the examples. At this point you might want to use Excel to make copies of the output file and delete columns to create the DEMO and CRIME subsets, as well as the BASE subset.
3. Use Converters.split_orangetab_into_2 to split the dataset into 2 - training and validation (each gets limited to 1k examples, you can modify the code)
4. Use Converters.orangetab_to_svmlight to convert an orange file into an SVMLight-compatible format.

Tuning
======
1. Should be self-explanatory. Set the filename to the training dataset, and make a note of the optimal parameters, and the classification accuracy for that set of optimal parameters.

Output
======
1. Knowing the optimal parameters, the attrs variable, and run oc.cross_validate().

Sign Test
=========
1. Run print_linear_svm, print_decision_tree, and so on to print out each algorithm's predicted labels to /data_svm. You also need to run Converters.write_actual_labels to print the true labels.
2. Validators.binomial_sign_test can then be used on the true labels, and predicted labels from 2 algorithms, to see if one of them performs better than the other.
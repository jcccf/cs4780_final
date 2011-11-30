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
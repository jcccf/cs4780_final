import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('varsets', nargs='+')

ns = parser.parse_args(sys.argv[1:])
args = vars(ns)

nfolds = 10
file_prefix = '../data_svm/do_20111201_b_c_v_u_' + '_'.join(args['varsets']) + '_INCMIN_'
tot_acc = 0.0
TP = 0
FP = 0
TN = 0
FN = 0
for i in range(nfolds):
    orig_file = "%strain.train.%d.va" % (file_prefix, i)
    with open(orig_file) as f:
        trueval = [float(l.split()[0]) for l in f]
    clsfile = '%strain.train.%d.tr.cls' % (file_prefix, i)
    with open(clsfile) as f:
        clsval = [float(l) for l in f]
    assert len(trueval) == len(clsval)
    for i in range(len(trueval)):
        true, clv = trueval[i], clsval[i]
        if (true <= 0 and clv <= 0):
            TN += 1
        elif (true <= 0 and clv > 0):
            FP += 1
        elif (true > 0 and clv <= 0):
            FN += 1
        else:
            TP += 1
    acc = float(TP + TN) / float(TP + TN + FP + FN)
    tot_acc += acc
print "Accuracy = %.3f\nTP = %d\nFP = %d\nTN = %d\nFN = %d" % (tot_acc/nfolds, TP, FP, TN, FN)

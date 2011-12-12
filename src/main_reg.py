from includes import *

sy = 'INCMIN'
sx = ['DOSAGE', 'SEX', 'RACE_1', 'RACE_2', 'RACE_3', 'RACE_4', 'RACE_5', 'RACE_6']
mr = MRegression.MRegression('../data/do_20111201_b_m_v_DEMO_INCMIN.tab', select_y=sy, select_x=sx)
mr.svm_regression('../data_svm/incmintest')
mr.pca(verbose=True)
print
mr.regression('PCA', verbose=True)
print
mr.regression('Linear', verbose=True)

# R.globalenv['x1'] = R.FloatVector(mr.X[:,0].tolist())
# R.globalenv['x2'] = R.FloatVector(mr.X[:,1].tolist())
# R.globalenv['x3'] = R.FloatVector(mr.X[:,2].tolist())
# R.globalenv['y'] = R.FloatVector(mr.Y)
# fit = R.r.lm('y ~ x1 + x2')
# fit2 = R.r.lm('y ~ x1 + x2 + x3')
# # print R.r.summary(fit)
# print R.r.anova(fit, fit2)
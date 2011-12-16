## Screen windows
### 1. w1/. DEMO
	Optimal set of parameters:
    mForPruning: 5 maxMajority: 1.0 minExamples: 1 minSubset: 1 measure: infoGain 
		[0.9284076464441574]
    k = 8 [0.928016350113713]
	{'c': None, 't': 2, 'g': 0.2} 0.919313102799
	svmlight: Accuracy on test set: 85.20% (2717 correct, 472 incorrect, 3189 total)
	Precision/recall on test set: 82.53%/89.96%
	-----
	Learner  CA     IS     Brier  AUC    TP     FP     FN     TN 
	c4.5     0.905  0.766  0.171  0.922  5554   423    794    5982 
	linsvm   0.882  0.653  0.179  0.930  4996   150    1352   6255 
	logreg   0.882  0.661  0.178  0.930  4991   149    1357   6256 
	bayes    0.861  0.667  0.201  0.925  5274   694    1074   5711 
	kmeans   0.905  0.767  0.158  0.953  5667   535    681    5870 
	-----        
	CA=Classification Accuracy        
	IS=Information Score        
	Brier=Brier score        
	AUC=Area Under ROC curve        
	TP=True Positives, 
	FP=False Positives, 
	FN=False Negatives, 
	TN=True Negatives
	
### 2. w2/. CRIME
	*** Optimal set of parameters:
	mForPruning: 10 maxMajority: 1.0 minExamples: 2 minSubset: 2 measure: gini
		[0.8364480537635522]
	k: 39 [0.8320808869467371]
	{'c': None, 't': 2, 'g': 0.2} 0.836725211412
	svmlight: Accuracy on test set: 81.16% (2184 correct, 507 incorrect, 2691 total)
	Precision/recall on test set: 79.33%/83.13%
	-----
	Learner  CA     IS     Brier  AUC    TP     FP     FN     TN     
	c4.5     0.821  0.554  0.278  0.877  4484   1003   926    4348 
	linsvm   0.819  0.527  0.251  0.904  4605   1147   805    4204 
	logreg   0.819  0.532  0.253  0.901  4613   1152   797    4199 
	bayes    0.810  0.608  0.320  0.893  4394   1029   1016   4322 
	kmeans   0.822  0.546  0.249  0.905  4485   995    925    4356 
	-----
### 3. w3/. DEMO + CRIME = BASE
	*** Optimal set of parameters:  
	mForPruning: 5 maxMajority: 1.0 minExamples: 0 minSubset: 1 measure: gainRatio
	  	[0.9477498656756115]
	k = 8 [0.9219566377668414]
	{'c': None, 't': 2, 'g': 0.1} 0.951436130008
	svmlight: Accuracy on test set: 92.44% (2446 correct, 200 incorrect, 2646 total)
	Precision/recall on test set: 93.09%/91.83%
	-----
	Learner  CA     IS     Brier  AUC    TP     FP     FN     TN     
	c4.5     0.923  0.819  0.144  0.929  4823   356    458    4947 
	linsvm   0.919  0.771  0.117  0.975  4716   293    565    5010 
	logreg   0.919  0.788  0.117  0.974  4710   291    571    5012 
	bayes    0.886  0.771  0.190  0.968  4897   820    384    4483
	kmeans   0.896  0.754  0.160  0.957  4647   464    634    4839 
	-----
### 4. w4/. HISTORY
	*** Optimal set of parameters:
    mForPruning: 0 maxMajority: 0.8 minExamples: 2 minSubset: 1 measure: gini
		[0.4996925441967718]
    k: 125: [0.5002305918524212]
    {'c': 0.0, 't': 2, 'g': 0.0001} [0.500115287065]
	NOTE: did not get useful results with just history, so we did not continue with other tests.
### 5. w5/. CRIME + HISTORY
	*** Optimal set of parameters: 
	mForPruning: 10 maxMajority: 1.0 minExamples: 2 minSubset: 2 measure: gini
		[0.8364480537635522]
	k: 39: [0.8320808869467371]
	{'c': None, 't': 2, 'g': 0.2} 0.837375708577
	Accuracy on test set: 83.17% (2238 correct, 453 incorrect, 2691 total)
	Precision/recall on test set: 82.13%/85.55%
	-----
	Learner  CA     IS     Brier  AUC    TP     FP     FN     TN     
	c4.5     0.817  0.548  0.284  0.872  4344   953    1012   4452 
	linsvm   0.811  0.519  0.254  0.902  4447   1121   909    4284
	logreg   0.812  0.524  0.257  0.898  4475   1140   881    4265 
	bayes    0.807  0.604  0.323  0.890  4311   1029   1045   4376 
	kmeans   0.817  0.537  0.253  0.903  4375   986    981    4419 
	-----
	
## Binomial Sign Test Results
### DEMO
	../data_stat/dtree_demo.txt  against  ../data_stat/linsvm.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.903104421449 H2 CA is 0.885230479774
	D1 is 114 D2 is 171 k is 285
	p-value is 0.025 / 95.0 % confidence
	probability is 0.000438942739207 / significance is True
	
	../data_stat/dtree_demo.txt  against  ../data_stat/logreg.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.903104421449 H2 CA is 0.883976168078
	D1 is 115 D2 is 176 k is 291
	p-value is 0.025 / 95.0 % confidence
	probability is 0.000208649800437 / significance is True
	
	../data_stat/dtree_demo.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.903104421449 H2 CA is 0.904672311069
	D1 is 106 D2 is 101 k is 207
	p-value is 0.025 / 95.0 % confidence
	probability is 0.338379813989 / significance is False
	
	../data_stat/dtree_demo.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.903104421449 H2 CA is 0.871119473189
	D1 is 120 D2 is 222 k is 342
	p-value is 0.025 / 95.0 % confidence
	probability is 1.88733747775e-08 / significance is True
	
	../data_stat/dtree_demo.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.903104421449 H2 CA is 0.851991219818
	D1 is 142 D2 is 305 k is 447
	p-value is 0.025 / 95.0 % confidence
	probability is 4.63233799697e-15 / significance is True
	
	../data_stat/linsvm.txt  against  ../data_stat/logreg.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.885230479774 H2 CA is 0.883976168078
	D1 is 10 D2 is 14 k is 24
	p-value is 0.025 / 95.0 % confidence
	probability is 0.270628094673 / significance is False
	
	../data_stat/linsvm.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.885230479774 H2 CA is 0.904672311069
	D1 is 206 D2 is 144 k is 350
	p-value is 0.025 / 95.0 % confidence
	probability is 0.00036790013996 / significance is True
	
	../data_stat/linsvm.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.885230479774 H2 CA is 0.871119473189
	D1 is 102 D2 is 147 k is 249
	p-value is 0.025 / 95.0 % confidence
	probability is 0.00259675799398 / significance is True
	
	../data_stat/linsvm.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.885230479774 H2 CA is 0.851991219818
	D1 is 182 D2 is 288 k is 470
	p-value is 0.025 / 95.0 % confidence
	probability is 5.78301631469e-07 / significance is True
	
	../data_stat/logreg.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.883976168078 H2 CA is 0.904672311069
	D1 is 203 D2 is 137 k is 340
	p-value is 0.025 / 95.0 % confidence
	probability is 0.00013389995154 / significance is True
	
	../data_stat/logreg.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.883976168078 H2 CA is 0.871119473189
	D1 is 108 D2 is 149 k is 257
	p-value is 0.025 / 95.0 % confidence
	probability is 0.00622028908776 / significance is True
	
	../data_stat/logreg.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.883976168078 H2 CA is 0.851991219818
	D1 is 186 D2 is 288 k is 474
	p-value is 0.025 / 95.0 % confidence
	probability is 1.61126557397e-06 / significance is True
	
	../data_stat/knn.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.904672311069 H2 CA is 0.871119473189
	D1 is 136 D2 is 243 k is 379
	p-value is 0.025 / 95.0 % confidence
	probability is 2.12471853273e-08 / significance is True
	
	../data_stat/knn.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.904672311069 H2 CA is 0.851991219818
	D1 is 147 D2 is 315 k is 462
	p-value is 0.025 / 95.0 % confidence
	probability is 1.96815015232e-15 / significance is True
	
	../data_stat/bayes.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.871119473189 H2 CA is 0.851991219818
	D1 is 164 D2 is 225 k is 389
	p-value is 0.025 / 95.0 % confidence
	probability is 0.00115359053309 / significance is True

### CRIME
	../data_stat/dtree_demo.txt  against  ../data_stat/linsvm.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.813823857302 H2 CA is 0.804162021553
	D1 is 129 D2 is 155 k is 284
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0689045383708 / significance is False
	
	../data_stat/dtree_demo.txt  against  ../data_stat/logreg.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.813823857302 H2 CA is 0.803047194352
	D1 is 130 D2 is 159 k is 289
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0496893436214 / significance is False
	
	../data_stat/dtree_demo.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.813823857302 H2 CA is 0.806391675957
	D1 is 107 D2 is 127 k is 234
	p-value is 0.025 / 95.0 % confidence
	probability is 0.107061628814 / significance is False
	
	../data_stat/dtree_demo.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.813823857302 H2 CA is 0.799331103679
	D1 is 154 D2 is 193 k is 347
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0206005249483 / significance is True
	
	../data_stat/dtree_demo.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.813823857302 H2 CA is 0.811594202899
	D1 is 124 D2 is 130 k is 254
	p-value is 0.025 / 95.0 % confidence
	probability is 0.376899319233 / significance is False
	
	../data_stat/linsvm.txt  against  ../data_stat/logreg.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.804162021553 H2 CA is 0.803047194352
	D1 is 14 D2 is 17 k is 31
	p-value is 0.025 / 95.0 % confidence
	probability is 0.360050065909 / significance is False
	
	../data_stat/linsvm.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.804162021553 H2 CA is 0.806391675957
	D1 is 99 D2 is 93 k is 192
	p-value is 0.025 / 95.0 % confidence
	probability is 0.306773618797 / significance is False
	
	../data_stat/linsvm.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.804162021553 H2 CA is 0.799331103679
	D1 is 68 D2 is 81 k is 149
	p-value is 0.025 / 95.0 % confidence
	probability is 0.16279019025 / significance is False
	
	../data_stat/linsvm.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.804162021553 H2 CA is 0.811594202899
	D1 is 74 D2 is 54 k is 128
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0315043913042 / significance is False
	
	../data_stat/logreg.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.803047194352 H2 CA is 0.806391675957
	D1 is 101 D2 is 92 k is 193
	p-value is 0.025 / 95.0 % confidence
	probability is 0.235866055882 / significance is False
	
	../data_stat/logreg.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.803047194352 H2 CA is 0.799331103679
	D1 is 74 D2 is 84 k is 158
	p-value is 0.025 / 95.0 % confidence
	probability is 0.237053088393 / significance is False
	
	../data_stat/logreg.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.803047194352 H2 CA is 0.811594202899
	D1 is 78 D2 is 55 k is 133
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0185142550321 / significance is True
	
	../data_stat/knn.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.806391675957 H2 CA is 0.799331103679
	D1 is 117 D2 is 136 k is 253
	p-value is 0.025 / 95.0 % confidence
	probability is 0.128869098371 / significance is False
	
	../data_stat/knn.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.806391675957 H2 CA is 0.811594202899
	D1 is 78 D2 is 64 k is 142
	p-value is 0.025 / 95.0 % confidence
	probability is 0.103979210759 / significance is False
	
	../data_stat/bayes.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.799331103679 H2 CA is 0.811594202899
	D1 is 111 D2 is 78 k is 189
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0065916841908 / significance is True

### BASE
	../data_stat/dtree_demo.txt  against  ../data_stat/linsvm.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.915343915344 H2 CA is 0.916477702192
	D1 is 100 D2 is 97 k is 197
	p-value is 0.025 / 95.0 % confidence
	probability is 0.387869358353 / significance is False
	
	../data_stat/dtree_demo.txt  against  ../data_stat/logreg.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.915343915344 H2 CA is 0.916477702192
	D1 is 100 D2 is 97 k is 197
	p-value is 0.025 / 95.0 % confidence
	probability is 0.387869358353 / significance is False
	
	../data_stat/dtree_demo.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.915343915344 H2 CA is 0.892668178382
	D1 is 105 D2 is 165 k is 270
	p-value is 0.025 / 95.0 % confidence
	probability is 0.000156656151888 / significance is True
	
	../data_stat/dtree_demo.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.915343915344 H2 CA is 0.885865457294
	D1 is 95 D2 is 173 k is 268
	p-value is 0.025 / 95.0 % confidence
	probability is 1.09323021236e-06 / significance is True
	
	../data_stat/dtree_demo.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.915343915344 H2 CA is 0.924414210128
	D1 is 93 D2 is 69 k is 162
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0245862969393 / significance is True
	
	../data_stat/linsvm.txt  against  ../data_stat/logreg.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.916477702192 H2 CA is 0.916477702192
	D1 is 11 D2 is 11 k is 22
	p-value is 0.025 / 95.0 % confidence
	probability is 0.415905952454 / significance is False
	
	../data_stat/linsvm.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.916477702192 H2 CA is 0.892668178382
	D1 is 105 D2 is 168 k is 273
	p-value is 0.025 / 95.0 % confidence
	probability is 8.23860890485e-05 / significance is True
	
	../data_stat/linsvm.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.916477702192 H2 CA is 0.885865457294
	D1 is 67 D2 is 148 k is 215
	p-value is 0.025 / 95.0 % confidence
	probability is 1.69435867637e-08 / significance is True
	
	../data_stat/linsvm.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.916477702192 H2 CA is 0.924414210128
	D1 is 66 D2 is 45 k is 111
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0181532455707 / significance is True
	
	../data_stat/logreg.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.916477702192 H2 CA is 0.892668178382
	D1 is 105 D2 is 168 k is 273
	p-value is 0.025 / 95.0 % confidence
	probability is 8.23860890485e-05 / significance is True
	
	../data_stat/logreg.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.916477702192 H2 CA is 0.885865457294
	D1 is 69 D2 is 150 k is 219
	p-value is 0.025 / 95.0 % confidence
	probability is 2.28907175304e-08 / significance is True
	
	../data_stat/logreg.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.916477702192 H2 CA is 0.924414210128
	D1 is 68 D2 is 47 k is 115
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0198752525633 / significance is True
	
	../data_stat/knn.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.892668178382 H2 CA is 0.885865457294
	D1 is 162 D2 is 180 k is 342
	p-value is 0.025 / 95.0 % confidence
	probability is 0.178990488296 / significance is False
	
	../data_stat/knn.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.892668178382 H2 CA is 0.924414210128
	D1 is 150 D2 is 66 k is 216
	p-value is 0.025 / 95.0 % confidence
	probability is 2.30984309457e-09 / significance is True
	
	../data_stat/bayes.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.885865457294 H2 CA is 0.924414210128
	D1 is 152 D2 is 50 k is 202
	p-value is 0.025 / 95.0 % confidence
	probability is 5.95079541199e-14 / significance is True

### CRIME + HISTORY
	../data_stat/dtree_demo.txt  against  ../data_stat/linsvm.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.825715347454 H2 CA is 0.825715347454
	D1 is 150 D2 is 150 k is 300
	p-value is 0.025 / 95.0 % confidence
	probability is 0.47698624279 / significance is False
	
	../data_stat/dtree_demo.txt  against  ../data_stat/logreg.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.825715347454 H2 CA is 0.824228911185
	D1 is 151 D2 is 155 k is 306
	p-value is 0.025 / 95.0 % confidence
	probability is 0.431933777617 / significance is False
	
	../data_stat/dtree_demo.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.825715347454 H2 CA is 0.820512820513
	D1 is 108 D2 is 122 k is 230
	p-value is 0.025 / 95.0 % confidence
	probability is 0.195691951539 / significance is False
	
	../data_stat/dtree_demo.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.825715347454 H2 CA is 0.807134894091
	D1 is 150 D2 is 200 k is 350
	p-value is 0.025 / 95.0 % confidence
	probability is 0.00436001826528 / significance is True
	
	../data_stat/dtree_demo.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.825715347454 H2 CA is 0.831661092531
	D1 is 145 D2 is 129 k is 274
	p-value is 0.025 / 95.0 % confidence
	probability is 0.152204769036 / significance is False
	
	../data_stat/linsvm.txt  against  ../data_stat/logreg.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.825715347454 H2 CA is 0.824228911185
	D1 is 13 D2 is 17 k is 30
	p-value is 0.025 / 95.0 % confidence
	probability is 0.292332355864 / significance is False
	
	../data_stat/linsvm.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.825715347454 H2 CA is 0.820512820513
	D1 is 102 D2 is 116 k is 218
	p-value is 0.025 / 95.0 % confidence
	probability is 0.189323142989 / significance is False
	
	../data_stat/linsvm.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.825715347454 H2 CA is 0.807134894091
	D1 is 46 D2 is 96 k is 142
	p-value is 0.025 / 95.0 % confidence
	probability is 1.64693782945e-05 / significance is True
	
	../data_stat/linsvm.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.825715347454 H2 CA is 0.831661092531
	D1 is 69 D2 is 53 k is 122
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0617135434919 / significance is False
	
	../data_stat/logreg.txt  against  ../data_stat/knn.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.824228911185 H2 CA is 0.820512820513
	D1 is 108 D2 is 118 k is 226
	p-value is 0.025 / 95.0 % confidence
	probability is 0.274743828974 / significance is False
	
	../data_stat/logreg.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.824228911185 H2 CA is 0.807134894091
	D1 is 53 D2 is 99 k is 152
	p-value is 0.025 / 95.0 % confidence
	probability is 0.00011871346009 / significance is True
	
	../data_stat/logreg.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.824228911185 H2 CA is 0.831661092531
	D1 is 77 D2 is 57 k is 134
	p-value is 0.025 / 95.0 % confidence
	probability is 0.034629793591 / significance is False
	
	../data_stat/knn.txt  against  ../data_stat/bayes.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.820512820513 H2 CA is 0.807134894091
	D1 is 104 D2 is 140 k is 244
	p-value is 0.025 / 95.0 % confidence
	probability is 0.0124244893591 / significance is True
	
	../data_stat/knn.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.820512820513 H2 CA is 0.831661092531
	D1 is 90 D2 is 60 k is 150
	p-value is 0.025 / 95.0 % confidence
	probability is 0.00556079692361 / significance is True
	
	../data_stat/bayes.txt  against  ../data_stat/svmlight.txt
	Binomial Sign Test (McNemar's Test)
	H1 CA is 0.807134894091 H2 CA is 0.831661092531
	D1 is 118 D2 is 52 k is 170
	p-value is 0.025 / 95.0 % confidence
	probability is 9.61829971224e-08 / significance is True

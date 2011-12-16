from scipy.stats import binom
import itertools

def binomial_sign_test_multiple(original_file, filelist, p=0.025, verbose=False):
  for h1_file, h2_file in itertools.combinations(filelist, 2):
    binomial_sign_test(original_file, h1_file, h2_file, p=p, verbose=verbose)

# Assumes classification values between -1 and 1, and only two classes -1 and 1
def binomial_sign_test(original_file, h1_file, h2_file, p=0.025, verbose=False):
  print h1_file, ' against ', h2_file
  with open(original_file, 'r') as f:
    true_y = f.readlines()
  with open(h1_file, 'r') as f:
    h1_y = f.readlines()
  with open(h2_file, 'r') as f:
    h2_y = f.readlines()
  if len(true_y) != len(h1_y) != len(h2_y):
    raise Exception("Unequal # of classified examples")
    
  # Calculate d1 and d2
  h1_corr, h2_corr, d1, d2 = 0, 0, 0, 0
  for i in range(len(true_y)):
    true, h1, h2 = float(true_y[i]), float(h1_y[i]), float(h2_y[i])
    if (true <= 0 and h1 <= 0) or (true > 0 and h1 > 0): # h1 correct
      h1_corr += 1
      if (true <= 0 and h2 > 0) or (true > 0 and h2 <= 0): # but h2 incorrect
        d2 += 1
    if (true <= 0 and h2 <= 0) or (true > 0 and h2 > 0): # h2 correct
      h2_corr += 1
      if (true <= 0 and h1 > 0) or (true > 0 and h1 <= 0): # but h1 incorrect
        d1 += 1
        
  k = d1 + d2
  
  # Probability of observing D1 <= d1 or D1 >= d1
  prob = min(binom.cdf(d1, k, 0.5), 1 - binom.cdf(d1, k, 0.5))
  
  if verbose:
    print "Binomial Sign Test (McNemar's Test)"
    print "H1 CA is", float(h1_corr)/len(true_y), "H2 CA is", float(h2_corr)/len(true_y)
    print "D1 is", d1, "D2 is", d2, "k is", k
    print "p-value is", p, "/", (1-p*2)*100, "% confidence"
    print "probability is", prob, "/ significance is", (prob < p)
    print
  
  return (prob, prob < p)

def precision_recall_multiple(original_file, filelist, verbose=False):
    return [precision_recall(original_file, h_file, verbose=verbose) for h_file in filelist]

# Assumes classification values between -1 and 1, and only two classes -1 and 1
def precision_recall(original_file, h_file, p=0.025, verbose=False):
  with open(original_file, 'r') as f:
    true_y = f.readlines()
  with open(h_file, 'r') as f:
    h_y = f.readlines()
  if len(true_y) != len(h_y):
    raise Exception("Unequal # of classified examples")
  TP = 0
  FP = 0
  TN = 0
  FN = 0
  for i in range(len(true_y)):
      true, clv = float(true_y[i]), float(h_y[i])
      if (true <= 0 and clv <= 0):
          TN += 1
      elif (true <= 0 and clv > 0):
          FP += 1
      elif (true > 0 and clv <= 0):
          FN += 1
      else:
          TP += 1
  precision = float(TP) / float(TP + FP)
  recall = float(TP) / float(TP + FN)
  
  if verbose:
    print '%s\n\tprecision: %.3f\trecall: %.3f' % (h_file, precision, recall)
  
  return (precision, recall)
import random
from numpy import *
from math import floor, ceil

def base_to_orangetab(svmlight_file, output_file):
  '''Convert File from the Base Format to Orange Tabular Format'''
  raise NotImplementedError()
  
def orangetab_to_svmlight(orangetab_file, output_file):
  with open(output_file, 'w') as f2:
    with open(orangetab_file, 'r') as f:
      i, nfeatures, feature_index = 1, 0, 0
      lines = f.readlines()
      if len(lines) == 1:
        lines = lines[0].split('\r')
      for l in lines:
        items = l.replace('\n', '').split('\t')
        if i == 1:
          nfeatures = len(items)
        elif i == 2:
          if nfeatures != len(items):
            raise Exception("# of c's and d's don't correspond")
          # for cd in items:
          #           if cd != 'c':
          #             raise Exception("All attributes must be continuous")
        elif i == 3:
          for i,c in enumerate(items):
            if c == 'class':
              feature_index = i
          print feature_index
        else:
          fval, rest = 0, {}
          for i,c in enumerate(items):
            if i == feature_index:
              if c not in ['-1', '1']:
                raise Exception("Feature is not binarified!")
              fval = c
              # # MODIFY THIS PART IF LABEL IS ALREADY BINARIFIED
              # if float(c) < 12:
              #   fval = -1
              # else:
              #   fval = 1
            else:
              rest[i] = c
          f2.write('%s %s\n' % (fval, " ".join(['%s:%s' % (k,v) for k,v in rest.iteritems()])))
        i += 1  
        
def balance_orangetab(orangetab_file, output_file):
  neglist, poslist = [], []
  with open(output_file, 'w') as f2:
    with open(orangetab_file, 'r') as f:
      lines = f.readlines()
      print len(lines)
      for i in range(3, len(lines)):
        l = lines[i]
        if l.split('\t')[0] == '-1':
          neglist.append(l)
        else:
          poslist.append(l)
      f2.write(lines[0])
      f2.write(lines[1])
      f2.write(lines[2])
      
      print len(poslist)
      print len(neglist)
      
      # Sample from larger class to match size of smaller class
      if len(poslist) < len(neglist):
        random.shuffle(neglist)
        neglist = neglist[:len(poslist)]
      else:
        random.shuffle(poslist)
        poslist = poslist[:len(neglist)]
      
      print len(poslist)
      print len(neglist)
      
      combined = neglist + poslist
      random.shuffle(combined)
      for l in combined:
        f2.write(l)
        
def split_orangetab_into_2(orangetab_file, train_frac=.8):
  with open(orangetab_file, 'r') as f:
    lines = f.readlines()
  if len(lines) == 1:
    lines = lines[0].split('\r')
    lines = [l+'\n' for l in lines]

  train_size = int(floor((len(lines) - 3) * train_frac))
  
  with open(orangetab_file.rsplit('.', 1)[0]+'_train.tab', 'w') as f2:
    f2.write(lines[0])
    f2.write(lines[1])
    f2.write(lines[2])
    for l in lines[3:3+train_size]:
      f2.write(l)
    
  with open(orangetab_file.rsplit('.', 1)[0]+'_val.tab', 'w') as f2:
    f2.write(lines[0])
    f2.write(lines[1])
    f2.write(lines[2])
    for l in lines[3+train_size:]:
      f2.write(l)
      
  return [orangetab_file.rsplit('.', 1)[0]+'_train.tab', orangetab_file.rsplit('.', 1)[0]+'_val.tab']
      
def write_actual_labels(orangetab_file, output_file):
  with open(orangetab_file, 'r') as f:
    lines = f.readlines()
  if len(lines) == 1:
    lines = lines[0].split('\r')
    lines = [l+'\n' for l in lines]
  with open(output_file, 'w') as f:
    for i in range(3, len(lines)):
      f.write('%s\n' % lines[i].split('\t')[0])

def normalize_orange(orangetab_file, output_file):
  with open(orangetab_file, 'r') as f:
    lines = f.readlines()
  if len(lines) == 1:
    lines = lines[0].split('\r')
  headlines = array(lines[0].replace('\n', '').strip().split('\t'))
  sublines = array(lines[1].replace('\n', '').strip().split('\t'))
  splitlines = [l.replace('\n', '').strip().split('\t') for l in lines]
  splitlines = splitlines[3:]
  # print splitlines
  floatize = vectorize(lambda x: float(x)) # convert each string into a float (this creates a function)
  a = floatize(array(splitlines))
  a = transpose(a) # transpose columns to rows
  
  # Remove all columns with std deviation of 0 - i.e. all values are the same
  i = 0
  eyes = []
  for b in a:
    if b.std() == 0:
      eyes.append(i)
    i += 1
  a = delete(a, eyes, 0)
  headlines = delete(headlines, eyes, 0)
  sublines = delete(sublines, eyes, 0)
  
  a = array([(b - b.mean())/b.std() if (b.max() != 1 or b.min() != -1) else b for b in a]) # normalize each row
  a = transpose(a) # transpose rows back to columns
  a = a.tolist()
  with open(output_file, 'w') as f:
    f.write("\t".join([str(r) for r in headlines.tolist()])+"\n")
    f.write("\t".join([str(r) for r in sublines.tolist()])+"\n")
    f.write(lines[2].replace('\n','')+"\n")
    for row in a:
      f.write("\t".join([str(r) for r in row])+"\n")
import random

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
        
def split_orangetab_into_2(orangetab_file):
  with open(orangetab_file, 'r') as f:
    lines = f.readlines()
  if len(lines) == 1:
    lines = lines[0].split('\r')
    lines = [l+'\n' for l in lines]
  
  with open(orangetab_file.rsplit('.', 1)[0]+'_train.tab', 'w') as f2:
    f2.write(lines[0])
    f2.write(lines[1])
    f2.write(lines[2])
    for l in lines[3:1003]:
      f2.write(l)
    
  with open(orangetab_file.rsplit('.', 1)[0]+'_val.tab', 'w') as f2:
    f2.write(lines[0])
    f2.write(lines[1])
    f2.write(lines[2])
    for l in lines[1003:2003]:
      f2.write(l)
      
def write_actual_labels(orangetab_file, output_file):
  with open(orangetab_file, 'r') as f:
    lines = f.readlines()
  if len(lines) == 1:
    lines = lines[0].split('\r')
    lines = [l+'\n' for l in lines]
  with open(output_file, 'w') as f:
    for i in range(3, len(lines)):
      f.write('%s\n' % lines[i].split('\t')[0])
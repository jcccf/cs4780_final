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
              # MODIFY THIS PART IF LABEL IS ALREADY BINARIFIED
              if float(c) < 12:
                fval = -1
              else:
                fval = 1
            else:
              rest[i] = c
          f2.write('%s %s\n' % (fval, " ".join(['%s:%s' % (k,v) for k,v in rest.iteritems()])))
        i += 1  
class Example:
  def __init__(self, line='0'):
    parts = line.split(' ')
    self.label = parts[0]
    self.attrs = {}
    for i in range(1,len(parts)):
      if ':' in parts[i]:
        feature = parts[i].split(':')
        if len(feature) is 2:
          self.attrs[int(feature[0])] = float(feature[1])
        else:
          print "Error in length of feature for %s" % self.label

# Load data from a file and return an array of Examples
def load_data(filename):
  data = []
  with open("../data/%s" % filename) as f:
  	for l in f:
  		data.append(Example(l))
  return data
  
class DCExample:
  '''Object that stores an example'''
  def __init__(self, label, dictionary):
    self.label = label
    self.attrs = dictionary
    
def load_dcdata(orange_datafile):
  '''Loads data from a file which is in the Orange Tabular format'''
  class_index, attr_list, dc_list, examples = -1, [], [], []
  with open(orange_datafile, 'r') as f:
    i = 0
    for l in f:
      if i > 2: # Load Example
        elist = l.replace('\n', '').split('\t')
        nlist = []
        for j, val in enumerate(elist):
          if j != class_index and val != '':
            if dc_list[j]:
              nlist.append((j, val))
            else:
              nlist.append((j, float(val)))
        label = elist[class_index]
        examples.append(DCExample(label, dict(nlist)))
      elif i == 0: # Load Labels
        attr_list = l.replace('\n', '').split('\t')
      elif i == 1: # Determine whether discrete or continuous
        dcs = l.replace('\n', '').split('\t')
        dc_list = [(dc != 'c') for dc in dcs]
      elif i == 2: # Which is the label
        whichisit = l.replace('\n', '').split('\t')
        for i in range(0, len(whichisit)):
          if whichisit[i] != "":
            class_index = i
      i += 1
    return (class_index, attr_list, dc_list, examples)
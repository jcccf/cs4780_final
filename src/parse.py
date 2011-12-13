from string import strip
from copy import deepcopy
from datetime import date
import csv
import re
import time
from math import sqrt
import argparse
import sys

''' Records data (key: cid) and Offense Data
 unit of analysis: judicial proceeding ("a proceeding in which all offenses for 
 which the offender is convicted are pending before the court for sentencing at the same time.)
 
 NOTE: Unknown values have been left as is. They appear in various codes like "Unk" or "99."
 
 '''

dir = ""
record_fields = ['CID', 'SID', 'PPID', 'BATCH', 'DOB', 'DOS', 'DOSAGE', 
                  'AGEEPOCH', 'SEX', 'DSEX', 'RACE', 'DRACE', 'COUNTY', 
                  'DCOUNTY', 'MURA', 'MURC', 'VMA', 'VMC', 'RAPA', 'RAPC', 
                  'KIDA', 'KIDC', 'IVDA', 'IVDC', 'ARSPERSA', 'ARSPERSC', 
                  'ROBSBIA', 'ROBSBIC', 'ROBMVSBA', 'ROBMVSBC', 'AGASBIA', 
                  'AGASBIC', 'DRUGDTHA', 'DRUGDTHC', 'BURA', 'BURC', 'ETHF1A', 
                  'ETHF1C', 'INCHOATA', 'INCHOATC', 'ARSA', 'ARSC', 'ROBA', 
                  'ROBC', 'ROBMVA', 'ROBMVC', 'AGA', 'AGC', 'BUROTHRA', 
                  'BUROTHRC', 'AGINDA', 'AGINDC', 'SEXASLTA', 'SEXASLTC', 
                  'F1A', 'F1C', 'F2A', 'F2C', 'DRG50GA', 'DRG50GC', 'DRGA', 
                  'DRGC', 'F3A', 'F3C', 'M1DEATHA', 'M1DEATHC', 'WEA', 'WEC', 
                  'M1CHILDA', 'M1CHILDC', 'M1DUIA', 'M1DUIC', 'MIS']
record_col_end = [10, 18, 26, 34, 44, 54, 56, 57, 58, 66, 67, 75, 77, 97, 98, 
                   99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124, 
                   126, 127, 129, 130, 132, 133, 134, 135, 136, 137, 140, 141,
                   142, 143, 144, 145, 146, 147, 149, 150, 151, 152, 154, 156, 
                   158, 159, 160, 161, 162, 163, 164, 165, 166, 168]
offense_fields = ['CID', 'CID2', 'BATCH', 'OFFSEQ', 'OTN', 'DOCKET', 'DOF',
                  'GLEPOCH', 'DOFAGE', 'PCSOFF', 'PCSSUB', 'SUBSECT', 'OFFLABEL',
                  'DRUGTYPE', 'DRUGAMT', 'DRUGUNIT', 'COMPLETE', 'GRAD', 'GRADE',
                  'OGS', 'OGSRANK', 'PRS', 'DWE', 'DDWE', 'ENHANC', 'WEAPTYPE',
                  'MAN', 'DMAN', 'MANMIN', 'BOOTCAMP', 'DISP', 'DDISP', 'PSI',
                  'DPSI', 'DAASS', 'DDAASS', 'DRUGDEP', 'DDRUGDEP', 'IPDRUG',
                  'DIPDRUG', 'COUNTIP', 'DCOUNTIP', 'SEXPRED', 'DSEXPRED', 'RNGSTR1',
                  'RNGSTR2', 'RNGSTR3', 'INCSTR', 'RIPSTR', 'IPSTR',
                  'PROSTR', 'MONSTR', 'NFPSTR', 'SUSPSTR', 'INCTYPE', 'RIPTYPE',
                  'IPTYPE', 'PROCOND', 'INCMIN', 'INCMAX', 'RIPMIN', 'IPMIN',
                  'PROMIN', 'FINE', 'COST', 'REST', 'WORKRLS', 'CONFORM',
                  'GL', 'REASON1', 'REASON2', 'REASON3', 'REASON4', 'REASON5', 
                  'REASON6', 'REASON7', 'REASON8', 'JINCTYPE', 'JRIPTYPE',
                  'JIPTYPE', 'JPROCOND', 'JINCMIN', 'JINCMAX', 'JRIPMIN', 
                  'JIPMIN', 'JPROMIN', 'JFINE', 'JCOST','JREST', 'JINCSTR',
                  'JRIPSTR', 'JIPSTR', 'JPROSTR', 'JMONSTR', 'QTMSFLAG']
offense_col_end = [10, 20, 28, 31, 39, 54, 64, 65, 67, 73, 81, 89, 139, 154, 
                   163, 169, 170, 175, 177, 179, 181, 182, 183, 223, 224, 249, 
                   251, 281, 289, 290, 291, 311, 312, 320, 321, 333, 334, 354,
                   355, 375, 376, 396, 397, 409, 489, 529, 569, 619, 669, 719,
                   769, 819, 869, 919, 920, 922, 924, 926, 934, 943, 951, 959,
                   969, 978, 987, 997, 998, 1118, 1120, 1124, 1128, 1132, 1136,
                   1140, 1144, 1148, 1152, 1153, 1155, 1157, 1159, 1168, 1177, 
                   1185, 1193, 1198, 1204, 1213, 1223, 1273, 1323, 1373, 1423,
                   1473, 1481]
possible_labels = ['INCMIN', 'INCMAX', 'INCTYPE', 'IPTYPE', 'GRADE', 'FINE', 'BOOTCAMP']

def build_begin(end):
    begin = [0]
    for e in end:
        begin.append(e)
    begin.remove(end[len(end)-1])
    return begin

record_col_begin = build_begin(record_col_end)
offense_col_begin = build_begin(offense_col_end)
all_fields = deepcopy(record_fields)
all_fields.extend(offense_fields)
field_types = {}
field_nulls = {}
to_coarsify = []
to_binarize = []
to_split_median = []
to_split_value = {}
hist_split_value = {}
use_uno = False
filter_unknown = False

#==============================================================================

''' Args: 
        list1: dict of field values
        list2: dict of field values
        key: name of field to join on
'''
def left_join(list1, list2, key):
    results = []
    for point in list1:
        matches = filter(lambda p: p[key] == point[key], list2)
        for match in matches:
            row = deepcopy(point)
            row.update(match)
            results.append(row)
    return results
    
''' Args:
        omit_ends: omitting come columns that were blanked out for confidentiality
    Returns: 
        A list of dictionaries. i.e., a list of points, where every point is a dictionary of fields
'''
def parse_data(filename, fields, col_begins, col_ends, omit_fields, project):
    f = open(dir+filename, 'r')
    results = []
    for line in f:
        r = {}
        begin = 0
        skip = False
        
        for column in project:
            #print column
            i = fields.index(column)
            begin = col_begins[i]
            end = col_ends[i]
            field = fields[i]

            if field not in omit_fields and field in project:
                val = strip(line[begin:end])
                # exclude unknown values
                if not (field in field_nulls and field_nulls[field] == val) and len(val)>0:
                    r[field] = val
                    
                elif filter_unknown: # skip whole row
                    skip = True

        if not skip:
            results.append(r)

    f.close()
    return results

def parse_record(project):
    to_discard = ['SID', 'PPID', 'AGEEPOCH', 'DSEX', 'DRACE', 'DCOUNTY']
    features = deepcopy(project)
    for f in to_discard:
        if f in features:
            features.remove(f)
    return parse_data('records.txt', record_fields, record_col_begin, record_col_end, to_discard, project), features
        
def parse_offense(project):
    to_discard = ['OTN', 'DOCKET', 'CID2', 'OFFSEQ','DDWE', 'DMAN', 'DDISP', 'DPSI', 
                  'DDAASS', 'DDRUGDEP', 'DIPDRUG', 'DCOUNTIP', 'DSEXPRED', 'INCSTR', 'JMONSTR']
    features = deepcopy(project)
    for f in to_discard:
        if f in features:
            features.remove(f)
    return parse_data('offenses.txt', offense_fields, offense_col_begin, offense_col_end, to_discard, project), features

def read_field_types(filename):        
    f = open(dir+filename, 'rU')
    filereader = csv.reader(f,dialect='excel')
    for line in f:
        rem = re.match(r'([A-Za-z\d]+),([cid]),([\d\.]+)?', line)
        field = rem.group(1)
        type = rem.group(2)
        null = rem.group(3)
        field_types[field] = type
        if null != None:
            field_nulls[field] = null
    
# get set of all values this field ever takes on in the data set
def get_field_values(list, label):
    result = []
    for point in list:
        if label in point and point[label] not in result:
            result.append(point[label])
    return result

# might use later to dump together similar categories. e.g., all the different kinds of burglaries    
def similar_str(s):
    pass

# does not have side-effects
def process_vars(list, fields):
    list = deepcopy(list)
    for field in deepcopy(fields):
        process_var(field, list, fields)
    return list, fields

# has side-effects
def process_var(field, list, fields):
    if field in ['DOB', 'DOS', 'DOF']: # month/day/year
        newfields = map(lambda sub: field+'_'+sub, ['MONTH', 'YEAR', 'WEEKDAY','UNO'])
        if use_uno:
            fields.extend([newfields[3]])
            field_types[newfields[3]] = 'c'
        else:
            fields.extend(newfields[0:3])
            for newf in newfields:
                field_types[newf] = 'd'
        for row in list:
            if field not in row:
                continue
            dateobj = time.strptime(row[field], "%m/%d/%Y")
            if not use_uno:
                row[newfields[0]] = dateobj.tm_mon
                row[newfields[1]] = dateobj.tm_year
                row[newfields[2]] = date(dateobj.tm_year, dateobj.tm_mon, dateobj.tm_mday).isoweekday()
            else:
                row[newfields[3]] = time.mktime(dateobj)
    
            del row[field]
        fields.remove(field)
    elif field in to_coarsify: # into 10 buckets or a fifth size, whichever's greater
        values = get_field_values(list, field)
        values.sort()
        num_vals = len(values)
        scale = 5
        if num_vals/10 > scale:
            scale = num_vals/10
        num_buckets = num_vals / scale
        capacity_split = (num_vals % scale)*(scale+1)
        num_bigger_buckets = capacity_split
        # every bucket contains scale or scale+1 values
        for row in list:
            if field not in row:
                continue
            val = row[field]
            if values.index(val) < capacity_split:
                index = (values.index(val)/(scale+1))*(scale+1) 
            else:
                index = ((values.index(val)-capacity_split)/scale)*scale + capacity_split
            row[field] = values[index] # take lowest value from bucket 
    elif field in to_binarize: # every value gets own field
        values = get_field_values(list, field)
        newfields = map(lambda sub: field+'_'+sub, values)
        fields.extend(newfields)
        for row in list:
            if field not in row:
                continue
            for newfield in newfields:
                row[newfield] = -1
                field_types[newfield] = 'd'
            row[field+'_'+row[field]] = 1
            del row[field]
        fields.remove(field)
    elif field in to_split_median:
        values = get_field_values(list, field)
        field_types[field] = 'd'
        values.sort()
        median = values[len(values)/2]
        for row in list:
            if field not in row:
                continue
            if row[field] < median:
                row[field] = -1
            else:
                row[field] = 1
    elif field in to_split_value:
        split = to_split_value[field]
        field_types[field] = 'd'
        for row in list:
            if field not in row:
                continue
            if float(row[field]) < float(split):
                row[field] = -1
            else:
                row[field] = 1
    else:
        return


#==============================================================================
'''
ClassificationName \t {feature name \t} \n
{classification values \t} {[dci]} \n
{classification \t {feature values} \n}
'''
def to_orange_fmt(list, features, label, filename):
    features = deepcopy(features)
    listcpy = deepcopy(list)
    f = open(filename, 'w')
    s = ""
    # 1
    s += label + '\t'
    f_types = ""
    for feature in features:
        if feature != label:
            s += feature + '\t'
            #if feature in field_types:
            f_types += field_types[feature] + '\t'
            '''else:
                if string.find(feature, "_UNO") != -1:
                    f_types += 'd\t'
                else '''
            
    s += '\n'
    
    # 2
    #if field_types[label] == 'd':
    #    for val in get_field_values(list, label):
    #        s += val + ' '
    #else:
    s += field_types[label]
        
    s += '\t'
    s += f_types + '\n'
    
    # 3
    s += 'class' + '\t'*len(list[0]) + '\n'
    #print label
    features.remove(label)
    # 4
    for point in listcpy:
        row = ""
        if label in point:
            row += str(point[label])
            del point[label]
        else: # skip if label missing
            continue
        row += '\t'
        for field in features:
            if field in point:
                row += str(point[field])
            row += '\t'
        row += '\n'
        s += row
    f.write(s)
    f.close()        


''' Args: 
        list: dict of field values
        label: field to be used as label
        filename: output filename
'''
def to_svm_light(list, label, filename):
    listcpy = deepcopy(list)
    f = open(filename, 'w')
    for point in listcpy:
        s = point[label] + ' ' 
        del point[label]
        i = 1
        for field in point:
            s += str(i+1) + ':' + str(point[field]) + ' '
            i += 1
        s += '\n'
        f.write(s)
    f.close()

#==============================================================================
''' output ''' # specify fields to process. All lists must be mutually exclusive
def gen_file(list, features, labels, binarize, coarsify, medianize, valsplit, uno, balance, varsets):
    global use_uno, to_split_value, to_binarize, to_coarsify, to_split_median, hist_split_value
    filename = '../data/do_20111201'
    if binarize:
        filename += '_b'
        to_binarize = ['RACE', 'DISP', 'PCSOFF', 'PCSSUB', 'COUNTY']
    if coarsify:
        filename += '_c'
        to_coarsify = []
    if medianize:
        filename += '_m'
        to_split_median = []
    if valsplit:
        filename += '_v'
        to_split_value_indiv = {'SEX':2, 'DRUGDEP':2, 'SEXPRED':2} # to_split_value = {'INCMIN':12,'GRADE':5,'SEX':2}
        to_split_value = dict(to_split_value_indiv.items() + hist_split_value.items())
    if uno:
        filename += '_u'
        use_uno = uno
    if varsets:
        filename += '_' + '_'.join(varsets)
        
    # keep only the labels we want, remove others
    """labels_to_remove = possible_labels[:]
    for l in labels:
        labels_to_remove.remove(l)
    for l in labels_to_remove:
        if l in features:
            features.remove(l)"""

    ro, features = process_vars(list, features) # processes date fields, coarsifies, binarizes
    ro = normalize(ro, features)
    

    #print features, "being written to", filename
    
    for label in labels:
        if balance:
            ro_label = balance_list(ro, label)
        else:
            ro_label = ro
        to_orange_fmt(ro_label, features, label, filename+'_'+label+'.tab')


def mean(list):
    list = map(lambda x: float(x), list)
    return sum(list) / len(list)

def std(list, u):
    diff_squareds = map(lambda x: (float(x) - u)**2, list)
    return sqrt(sum(diff_squareds) / (len(list)))

# if standard deviation is 0, the feature is removed
def normalize(list, features):
    list = deepcopy(list)
    features = deepcopy(features)
    features = filter(lambda f: field_types[f]=='c',features)
    features = filter(lambda f: len(get_field_values(list,f)) > 0,features)
    means = []
    stds = []
    findex = {}
    i = 0

    for f in deepcopy(features):
        values = get_field_values(list, f)
        u = mean(values)  
        s = std(values, u)
        if s == 0:
            features.remove(f)
            continue
        findex[f] = i
        i += 1           
        means.append(u)
        stds.append(s)
    for row in list:
       for f in features:
           if f in row:
               row[f] = (float(row[f])-means[findex[f]]) / stds[findex[f]]
    
    return list

# label MUST be binary!
# returns perfectly shuffled list
def balance_list(list, label):
    pos = []
    neg = []
    for row in list:
        if label in row:
            if row[label] == 1:
                pos.extend([row])
            else:
                neg.extend([row])
    num_pos = len(pos)
    num_neg = len(neg)
    num = min(num_pos, num_neg)
    print "From %d pos and %d neg labels, outputting %d of each." % (num_pos, num_neg, num)
    result = []
    for i in range(num):
        result.extend([pos[i]])
        result.extend([neg[i]])
    return result

def parse_args(args):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-l', '--labels', nargs='+', required=True)
    parser.add_argument('-s', '--varsets', nargs='+', required=True)
    parser.add_argument('-f', '--filterunknown', action='store_true')
    parser.add_argument('-b', '--binarize', action='store_true')
    parser.add_argument('-c', '--coarsify', action='store_true')
    parser.add_argument('-m', '--medianize', action='store_true')
    parser.add_argument('-v', '--valsplit', action='store_true')
    parser.add_argument('-u', '--uno', action='store_true')
    parser.add_argument('-d', '--balance', action='store_true')
    
    ns = parser.parse_args(args)
    print ns
    return vars(ns)
   
if __name__ == '__main__':
    dir = '../penn97/'
    read_field_types('field_info.csv')
    ''' parse data '''
    #dir = '../test_data/'
    if dir == '../test_data/':
        print "***** Note: Running on test set, not actual set"
    
    args = parse_args(sys.argv[1:])
    
    recordvars = ['CID']
    offensevars = ['CID']
    
    ''' CHANGE ME BEGIN'''
    ''' Possible varsets: HIST, ABOUT, DEMO, CRIME '''
    filter_unknown = args['filterunknown']
    varsets = args['varsets']
    labels = args['labels']
    ''' CHANGE ME END'''
    
    if 'DEMO' in varsets:
        recordvars.extend(['DOSAGE','SEX', 'RACE', 'DOB', 'DOS', 'DOSAGE','COUNTY'])
    if 'CRIME' in varsets:
        offensevars.extend(['DOF','OGS','PCSOFF','PCSSUB','GRADE','DISP','COMPLETE'])
    if 'HIST' in varsets:
        HIST_base = ['MUR','VM','RAP','KID','IVD','ARSPERS','ROBSBI','ROBMVSB','AGASBI','DRUGDTH','BUR','ETHF1','INCHOAT','ARS','ROB','ROBMV','AG','BUROTHR','AGIND','SEXASLT','F1','F2','DRG50G','DRG','F3','M1DEATH','WE','M1CHILD','M1DUI']
        HIST_baseA = map(lambda x: x+'A', HIST_base)
        HIST_baseC = map(lambda x: x+'C', HIST_base)
        recordvars.extend(HIST_baseA)
        recordvars.extend(HIST_baseC)
        recordvars.extend(['MIS'])
        offensevars.extend(['PRS'])
        
        hist_vars = HIST_baseA
        hist_vars.extend(HIST_baseC)
        hist_vars.extend(['MIS','PRS'])
        for var in hist_vars:
            hist_split_value[var] = 1
            
    if 'ABOUT' in varsets:
        offensevars.extend(['DRUGDEP','SEXPRED'])
    
    for l in labels:
        if l not in offensevars:
            offensevars.extend([l])

    records, rec_fields = parse_record(recordvars)
    offenses, off_fields = parse_offense(offensevars)

    #to_orange_fmt(offenses, off_fields, 'GRADE', '../data/data_offenses.txt')

    ''' join '''
    ro = left_join(records, offenses, 'CID')
    rec_fields.remove('CID')
    off_fields.remove('CID')   
    features = rec_fields
    features.extend(off_fields)    
    print "num records = %d, num offenses = %d, rows after join = %d" % (len(records), len(offenses), len(ro))


    '''CUSTOMIZE THIS LINE AND LISTS/DICTIONARY INSIDE gen_file'''
    # list, features, label, binarize, coarsify, medianize, valsplit, uno, balance
    # gen_file(ro, features, labels, True, False, False, True, True, True)
    # gen_file(
    #     list=ro, 
    #     features=features, 
    #     labels=['INCMIN'], 
    #     binarize=True,
    #     coarsify=False,
    #     medianize=True,
    #     valsplit=True,
    #     uno=False,
    #     balance=False,
    #     varsets=['DEMO'])
    gen_file(
        list=ro, 
        features=features, 
        labels=labels, 
        binarize=args['binarize'],
        coarsify=args['coarsify'],
        medianize=args['medianize'],
        valsplit=args['valsplit'],
        uno=args['uno'],
        balance=args['balance'],
        varsets=varsets)
    

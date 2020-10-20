import os
import csv
import sys
from tqdm import tqdm

ROOT="./"
FARS_TEMPLATE="FARS_NationalCSV"
CONFIG_PATH=os.path.join(ROOT, 'config')

def grabFiles(farsFolder):
    '''
    Function grabs all filenames within 
    a given FARS folder
    '''
    for _,_,f in os.walk(farsFolder):
        pass
    return f

def grabCat(farsFileList):
    '''
    Function returns list of files without file extension.
    Used to categorize data from parser function
    '''
    return [fars[:-4] for fars in farsFileList]

def generateFARS(year):
    '''
    Function returns properly formatted FARS report
    folder name using parser.FARS_TEMPLATE
    '''
    return FARS_TEMPLATE.replace('_', str(year))

def csvRead(filename, filetype):
    '''
    Function reads csv file and returns list
    of OrderDicts
    '''
    with open(filename, 'r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        _ret = list(csvReader)
        _ret = [itemParser10(ret, filetype) for ret in _ret]
        return _ret

def loadConfig(year):
    '''
    Function should read and return a configuration file for
    a given FARS year (FARS number and file naming convention
    can change.

    NOTE: Since FARS 2010 Standardization Act, all following FARS
    reports should be the same format...
    '''
    with open(os.path.join(CONFIG_PATH, "%.txt"%(FARS_TEMPLATE.replace('_', year)))) as configFile:
        _config = config.readlines()
    return _config

def itemParser10(item, filetype):
    '''
    Function fixes datatype mismatch within any FARS report 2010 or later
    (standardization act compliant)
    '''
    if filetype == 'NMIMPAIR':
        for key in item.keys():
            if item[keu] == '':
                pass
            else:
                item[key] = int(item[key])
    elif filetype == 'DRIMPAIR':
        for key in items.keys():
            if item[key] == '':
                pass
            else:
                item[key] = int(item[key])
    elif filetype == 'SAFETYEQ':
        for key in items.keys():
            if item[key] == '':
                pass
            else:
                item[key] = int(item[key])
    elif filetype == 'ACCIDENT': 
        for key in item.keys():
            if item[key] == '':
                pass
            if key == 'LATITUDE' or key == 'LONGITUD':
                item[key] = float(item[key])
            elif key == 'TWAY_ID' or key == 'TWAY_ID2' or key == 'RAIL':
                pass
            else:
                item[key] = int(item[key])
    elif filetype == 'VIOLATN':
        for key in item.keys():
            if item[key] == '':
                pass
            else:
                item[key] = int(item[key])
    elif filetype == 'CEVENT':
        for key in item.keys():
            if item[key] == '':
                pass
            else:
                item[key] = int(item[key])
    elif filetype == 'VINDECODE':
        pass
    elif filetype == 'MIDRVACC':
        pass
    elif filetype == 'NMCRASH':
        pass
    elif filetype == 'VSOE':
        pass
    elif filetype == 'DAMAGE':
        pass
    elif filetype == 'MIACC':
        pass
    elif filetype == 'ACC_AUX':
        pass
    elif filetype == 'PER_AUX':
        pass
    elif filetype == 'VEVENT':
        pass
    elif filetype == 'FACTOR':
        pass
    elif filetype == 'MANEUVER':
        pass
    elif filetype == 'PERSON':
        pass
    elif filetype == 'PBTYPE':
        pass
    elif filetype == 'MIPER':
        pass
    elif filetype == 'DRUGS':
        pass
    elif filetype == 'VEH_AUX':
        pass
    elif filetype == 'PARKWORK':
        pass
    elif filetype == 'VEHICLE':
        pass
    elif filetype == 'VISION':
        pass
    elif filetype == 'DISTRACT':
        pass
    elif filetype == 'NMPRIOR':
        pass
    else:
        print("WARNING: No case detected! File may not follow 2010+ format.")
    return item

'''
if __name__ == '__main__':
    # API Testing area:
    fars = generateFARS(2018)
    fars_2018_files = grabFiles(fars)
    
    #for far in fars_2018_files:
    #    print(far)
    index = 3
    print(fars_2018_files[index])
    category = grabCat(fars_2018_files)
    _filecat = category[index]
    test = csvRead(os.path.join(ROOT, fars, fars_2018_files[index]), _filecat)
    print(test[0])
    print(len(test[0]))
'''

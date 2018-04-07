import sys

def readOut():
    interestInfo = open('interests.txt','r')
    lines = interestInfo.readlines()    
    interestDic = { }
    for i in range(len(lines)):
        item = lines[i][:-1]
        sep = item.split(':')
        specif = sep[1].split(',')
        specifs = []
        for name in specif:
            specifs += [name]
        interestDic[sep[0]] = specifs
    return interestDic
        
            
    
import string
import csv

def deleteComma(lst):
    result = ''
    for i in range(len(lst)):
        result += lst[i] + ' '
    return [result[:len(result)-1]]

def getText(lst):
    infoSep = { }
    infoSep['event'] = []
    infoSep['date'] = []
    infoSep['location'] = []
    infoSep['time'] = []
    # infoSep['description'] = []
    for speci in lst:
        #print(speci)
        if ('Mon' in speci) or ('Tue' in speci) or ('Wed' in speci) or ('Thur' in speci) or \
        ('Fri' in speci) or ('Sat' in speci) or ('Sun' in speci) or ('Jan' in speci) or \
        ('Feb' in speci) or ('Mar' in speci) or ('Apr' in speci) or ('May' in speci) or \
        ('Jun' in speci) or ('Jul' in speci) or ('Aug' in speci) or ('Sept' in speci) or \
        ('Oct' in speci) or ('Nov' in speci) or ('Dec' in speci) or ('MON' in speci) or ('TUE' in speci) or ('WED' in speci) or ('THUR' in speci) or \
        ('FRI' in speci) or ('SAT' in speci) or ('SUN' in speci) or ('JAN' in speci) or \
        ('FEB' in speci) or ('MAR' in speci) or ('APR' in speci) or ('MAY' in speci) or \
        ('JUN' in speci) or ('JUL' in speci) or ('AUG' in speci) or ('SEPT' in speci) or \
        ('OCT' in speci) or ('NOV' in speci) or ('DEC' in speci) or \
        (speci.isdigit() and len(speci)<=4 and int(speci[0])<=2 and len(speci) != 3) or \
        (speci[1:len(speci)].isdigit() and speci[0].isdigit == False) or (speci[:-1].isdigit() and speci[-1].isdigit()==False and len(speci[:-1])<=2):
            infoSep['date'] += [speci]
        elif speci.isupper() and ',' not in speci and 'date' not in speci and 'DATE' not in speci and \
        'AM' not in speci and 'PM' not in speci and ':' not in speci:
            infoSep['event'] += [speci]
        elif ',' in speci or 'Ave' in speci or 'Res' in speci or 'Ro' in speci and 'www.' not in speci or (speci[0].isupper() and speci[1].isdigit()):
            infoSep['location'] += [speci]
        elif ':' in speci or (len(speci)==2 and ('pm' in speci or 'am' in speci)) or (len(speci)==2 and ('PM' in speci or 'AM' in speci)):
            infoSep['time'] += [speci]
        # else:
        #     infoSep['description'] += [speci]
    for key in infoSep:
        infoSep[key] = deleteComma(infoSep[key])
    #print(infoSep)
    return infoSep


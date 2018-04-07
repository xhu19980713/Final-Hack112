# import module_manager
# module_manager.review()
from Hack112 import*
from InterestReader import*
from InfoSepMultiple import*
import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\Diane_HU\\Desktop\\API_Credential.json'


from google.cloud import vision
from google.cloud.vision import types

def detect_text(path):
    dic = { }
    result = []
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')

    for text in texts:
        #result += [['"{}"'.format(text.description)]]
        #print('\n"{}"'.format(text.description))

        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])
        vertices = ([(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        dic["{}".format(text.description)] = [(vertices)]
        #print('bounds: {}'.format(','.join(vertices)))
        #result += ['bounds: {}'.format(','.join(vertices))]
    #return result
    return dic

def cal(path):
    dic = detect_text(path)
    max = 0
    for key in dic:
        if len(key) < 10:
            pass
        elif dic[key][0][1][0]-dic[key][0][0][0] > max:
            max = dic[key][0][1][0]-dic[key][0][0][0]
            bound = (dic[key][0][1][0],dic[key][0][0][0])
    #print(max)
    #print(bound)
    midPoint = bound[1] + (max/2)
    #print(midPoint)
    return midPoint

def sePoster(path):
    dic = detect_text(path)
    midPoint = cal(path)
    pic1 = []
    pic2 = []
    for key in dic:
        if dic[key][0][1][0] <= midPoint:
            pic1 += [key]
        else:
            pic2 += [key]
    return [pic1,pic2[1:]]

def interestFilterTwo(self,path):
    posters = sePoster(path)
    interest = getInterestList(self)[0]
    interest = interest.lower()
    intDic = readOut()
    res = []
    for key in intDic:
        if key == interest:
            print(key)
            for i in intDic[key]:
                i1 = i[0].upper()+i[1:]
                i2 = i.upper()
                for poster in posters:
                    valid = i in poster or i1 in poster or i2 in poster
                    #print(valid)
                    itemdic = getText(poster)
                    if valid and itemdic not in res:
                        #writeOut(poster)
                        
                        res += [getText(poster)]
    return res
                    #getText(poster)
    
    
            
    


import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\Diane_HU\\Desktop\\API_Credential.json'


from google.cloud import vision
from google.cloud.vision import types

def imageReader(path):

    def detect_labels(path):
        result = []
        """Detects labels in the file."""
        client = vision.ImageAnnotatorClient()

        file_name = os.path.join(
            os.path.dirname(__file__),
             path)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations

        for label in labels:
            if label.score > 0.7:
                result.append(label.description)

        return result


def PosterReader(path):

    def getMidpoint(Vertices):
        x1,y1 = Vertices[0]
        x2,y2 = Vertices[1]
        x3,y3 = Vertices[2]
        x4,y4 = Vertices[3]
        midX = (x1 + x2 + x3 + x4) / 4
        midY = (y1 + y2 + y3 + y4) / 4
        return midX, midY

    def textIdentify(path):

        client = vision.ImageAnnotatorClient()

        file_name = os.path.join(
            os.path.dirname(__file__),
             path)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        result = []
        for text in texts:

            # vertices = ([(vertex.x, vertex.y)
            #             for vertex in text.bounding_poly.vertices])
            # midPoint = getMidpoint(vertices)
            result.append([text.description])
            # result.append([text.description, midPoint])
        return result

    def switch(result, i ,j):
        result[i], result[j] = result[j], result[i]

    def arrange(result):
        for i in range(1,len(result)):
            for j in range(i+1, len(result)):
                text1, pos1 = result[i]
                pos1x, pos1y = pos1
                text2, pos2 = result[j]
                pos2x, pos2y = pos2
                if (pos2y - pos1y) < -10:
                    switch(result,i,j)
                elif abs(pos2y - pos1y) < 10 and pos1x > pos2x:
                    switch(result,i,j)
        return result

    def connect(result):
        text = ''
        for i in range(1, len(result)):
            t, pos = result[i]
            text += ' ' + t
        return text

    def getTheText(path):
        pic = textIdentify(path)
        #arranged = arrange(pic)
        # return connect(pic)
        return pic

    return getTheText(path)







# if __name__ == '__main__':
#     path = 'poster.jpg'
#     print(PosterReader(path))
    # path1 = "10.jpeg"
    # print(imageReader(path1))





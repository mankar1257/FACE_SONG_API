import json
import numpy
import cv2

from Faces import detect_faces


def lambda_handler(event, context):
    """
    Handler function for lambda

    this function is used for preprocessing the input image
    befour feading to the model endpoint

   """

    # convert input to the desiered format
    data = event['data']

    img = numpy.asarray(data)
    img = img.astype(numpy.uint8)


    # detect the faces
    # we are going to take only one face for predcition
    face = detect_faces(img)[0]


    # preprocess the face array
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(face, (48,48), interpolation = cv2.INTER_AREA)
    face = face.reshape(1,48,48,1)

    
    payload = json.dumps(face.tolist())


    return {"faces":payload}

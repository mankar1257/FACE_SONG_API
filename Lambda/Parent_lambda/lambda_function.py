
## parent function

import os
import io
import boto3
import json
import csv
from Songs import get_songs

from Faces import get_face

# define gloabel vareables
ENDPOINT_NAME = 'tensorflow-training-2021-01-04-09-36-36-668'
runtime= boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
    """
    Handler function for parent lambda

    Returns : a dict contaning
        detected face
        predictated mood
        suggested songs

   """

    # retrive the faces from the given image using the child lambda function
    face = get_face(event)


    # predict the mood from face using the sagemaker Endpoint
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=face)

    result = json.loads(response['Body'].read().decode())
    predictions = list(result['predictions'][0])

    # map predictions to mood (calsses

    mood_values={0:"Angry",1:"Disgust",2:"Fear",3:"Happy",4:"Sad",5:"Surprise",6:"Neutral"}
    mood = mood_values[predictions.index(max(predictions))]

    # retriev the songs based on the mood
    songs = get_songs(mood)


    return_obj = {"face" : face ,
                    "mood" : mood ,
                     "songs":songs
                    }


    return return_obj

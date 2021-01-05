



import os
import io
import boto3
import json
import csv
import numpy


# Define the client to interact with AWS Lambda
client = boto3.client('lambda')


def get_face(event):
    """ retrive the faces in the image using child lambda function """

    data = json.loads(json.dumps(event))
    data = data['data']

    img = numpy.asarray(data)

    Payload =  {"data":img.tolist()}


    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-1:478270364551:function:face_detection',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(Payload)
    )

    responseFromChild = json.load(response['Payload'])


    face = responseFromChild['faces']


    return face


 
import numpy
import cv2

def detect_faces(img):
    """
    to detect the faces in the input image

    Parameters:
    img (np.ndarray): image array

    Returns:
    detected_faces (list): list of detected faces

   """

    #loading the CascadeClassifier from opencv
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detecting faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    detected_faces = []

    for (x, y, w, h) in faces:
        detected_faces.append(img[y:(y+h), x:(x+w)])

    return detected_faces

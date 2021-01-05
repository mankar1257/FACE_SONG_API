
import argparse
import os
import numpy as np
import json

# importing neccossory liberies
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras import backend
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout ,BatchNormalization,Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l1_l2
from sklearn.utils import class_weight


def get_model():
    """
    creates a simpel CNN arcitechure

    Parameters:
    Null

    Returns:

    kears Modle arcitecture

   """

    model = Sequential()

    # convolution layers
    model.add(Conv2D(64,(3,3),padding='same',input_shape=(48,48,1)) )
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(128,(5,5),padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(512,(3,3),padding='same',kernel_regularizer=l1_l2(0.01)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(1024,(3,3),padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(512,(3,3),padding='same' ))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    #flatten the layers
    model.add(Flatten())

    # full connection layers
    model.add(Dense(256 ))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.25))

    model.add(Dense(512,kernel_regularizer=l1_l2(0.01)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.25))

    model.add(Dense(1024))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.25))

    model.add(Dense(7,activation='softmax'))

    return model


def model(x_train, y_train, x_test, y_test,class_weights):
    """
    for model compilation and training

    Parameters:

    x_train, y_train(np.ndarray) : training data
    x_test, y_test(np.ndarray) : testing data
    class_weights (directory) : for balancing the baised dataset


    Returns:
    model (keras model) : trained model


   """
    # get model arcitechure
    model =  get_model()


    #compile
    opt = Adam(lr = 0.001)
    model.compile(optimizer=opt,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])


    # train on 10 epoches
    model.fit(x = x_train,y = y_train ,
                    epochs = 10 ,
                    batch_size = 64 ,
                    validation_data = (x_test,y_test),
                    class_weight=class_weights
                   )

    return model



def get_class_weights(y_train,y_test):
    """
    for mod

    Parameters:

    x_train, y_train(np.ndarray) : training data
    x_test, y_test(np.ndarray) : testing data
    class_weights (directory) : for balancing the baised dataset


    Returns:
    model (keras model) : trained model

    """

    # reversing one hot encoding
    Y = []

    encoded_Y = np.concatenate((y_train, y_test))

    for y in encoded_Y:
        Y_L = list(y)
        Y.append(Y_L.index(max(Y_L)))

    # creating balenced calss weights
    class_weights_N = class_weight.compute_class_weight('balanced',
                                                 np.unique(Y),
                                                 Y)

    # as the keras model takes the class weights as a directory
    class_weights = {}

    for i in range(7):
        class_weights[i] = int(class_weights_N[i]*10)

    return class_weights




def _load_training_data(train_dir):
    """ loading training data from S3 """

    x_train = np.load(os.path.join(train_dir, 'Train_X.npy'))
    y_train = np.load(os.path.join(train_dir, 'Train_y.npy'))

    return x_train, y_train

def _load_testing_data(test_dir):
    """ loading testing data from S3 """

    x_test = np.load(os.path.join(test_dir, 'Test_X.npy'))
    y_test = np.load(os.path.join(test_dir, 'Test_y.npy'))

    return x_test, y_test

def _parse_args():
    """ Parsing the arguments """
    parser = argparse.ArgumentParser()

    # Data, model, and output directories
    # model_dir is always passed in from SageMaker. By default this is a S3 path under the default bucket.
    parser.add_argument('--model_dir', type=str)

    parser.add_argument('--sm-model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))

    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--test', type=str, default=os.environ.get('SM_CHANNEL_TEST'))

    parser.add_argument('--hosts', type=list, default=json.loads(os.environ.get('SM_HOSTS')))
    parser.add_argument('--current-host', type=str, default=os.environ.get('SM_CURRENT_HOST'))

    return parser.parse_known_args()


if __name__ == "__main__":

    # parsing the arguments
    args, unknown = _parse_args()

    # loading the train and test data
    train_data, train_labels = _load_training_data(args.train)
    eval_data, eval_labels = _load_testing_data(args.test)

    # calculating the class weight
    class_weights = get_class_weights(train_labels,eval_labels)

    #training the model
    face_emotion_recognizer = model(train_data, train_labels, eval_data, eval_labels,class_weights)

    #saving the model
    if args.current_host == args.hosts[0]:
        # save model to an S3 directory
        face_emotion_recognizer.save(os.path.join(args.sm_model_dir, '00000001'), 'my_model.h5')

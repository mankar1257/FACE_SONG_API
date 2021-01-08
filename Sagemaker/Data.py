

import pandas as pd
import numpy as np


class Data:
    """ class for data loading and preprocessing  """

    def __init__(self):

        self.df = df = pd.read_csv("icml_face_data.csv.zip")

    def get_img(self,s):
        """ converting img from string to np array """
        array = [int(i) for i in s.split(" ")]
        img = np.array(array , dtype=np.float32).reshape(48,48,1)
        return img

    def one_hot_encode(self,x):
        """ one hot encoding of the lables """
        array = np.zeros(7,dtype=np.uint8 )
        array[x] = 1
        return array

    def Get_data(self):
        """
        To retrieve the data in the desired format

        Parameters:
        Null

        Returns: (np.ndarray)

        training and testing data

        X_train ,y_train,
        X_test,y_test

        """

        # change the pixel to np.array / img
        self.df['X_data'] =  self.df[' pixels'].apply(lambda x : self.get_img(x))

        # preparing one hot encoding
        self.df['y_data'] = self.df['emotion'].apply(lambda x : self.one_hot_encode(x))

        #preparing training dataset

        df_train = self.df[self.df[' Usage'] == 'Training']
        X_train = np.array([i for i in df_train['X_data']])
        y_train = np.array([i for i in df_train['y_data']])

        # preparing test dataset

        df_test = self.df[self.df[' Usage'] == 'PrivateTest']
        X_test = np.array([i for i in df_test['X_data']])
        y_test = np.array([i for i in df_test['y_data']])

        # normalize data
        X_train /= 255
        X_test /= 255

        return X_train,y_train,X_test,y_test
    
    

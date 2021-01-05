import numpy

import pandas as pd
md = pd.read_csv("final_music_sentiment.csv")


def get_songs(mood):
    """ retrive the songs based on the mood """

    df = md[md['mood'] == mood]
    df = df.sample(n=3)

    songs = [ "Song  : " + str(i) + " || Singer : " + str(j)
                for i,j in zip(df['Name'],df['Singer'])]

    return songs

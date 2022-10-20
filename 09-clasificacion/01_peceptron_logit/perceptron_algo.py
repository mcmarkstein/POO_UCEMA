import numpy as np
import matplotlib
from matplotlib import pyplot

import numpy as np
import matplotlib
from matplotlib import pyplot


# Some functions to plot our points and draw the lines
def plot_points(features, labels):
    X = np.array(features)
    y = np.array(labels)
    spam = X[np.argwhere(y == 1)]
    ham = X[np.argwhere(y == 0)]
    pyplot.scatter([s[0][0] for s in spam],
                   [s[0][1] for s in spam],
                   s=100,
                   color='cyan',
                   edgecolor='k',
                   marker='^')
    pyplot.scatter([s[0][0] for s in ham],
                   [s[0][1] for s in ham],
                   s=100,
                   color='red',
                   edgecolor='k',
                   marker='s')
    pyplot.xlabel('aack')
    pyplot.ylabel('beep')
    pyplot.legend(['happy', 'sad'])


#dictonary
alien = {
    'alien1': {'mood': 'happy', 'sentence': 'aack, aack, aack!'},
    'alien2': {'mood': 'sad', 'sentence': 'beep beep!'},
    'alien3': {'mood': 'happy', 'sentence': 'aack beep aack!'},
    'alien4': {'mood': 'sad', 'sentence': 'aack beep beep!'}
}

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(alien).T

#creo mi score, si dice aack sumo 1 y si dice beep resto uno por oración.
#elimino caracteres especiales y convierto a minúsculas

#create a column with quantity of aack and other column with quantity of beep
df['aack'] = df['sentence'].apply(lambda x: x.count('aack'))
df['beep'] = df['sentence'].apply(lambda x: x.count('beep'))

#Create a plot with the points and the line
def plot_points_and_line(features, labels, a, b, c):
    plot_points(features, labels)
    draw_line(a, b, c, color='black', linestyle='--', linewidth=2)
    pyplot.show()


def algoritmo_clasificacion(sentence):
    sentence = sentence.replace('!', '').replace(',', '').lower() #elimino caracteres especiales y convierto a minúsculas
    score = 0
    for word in sentence.split(): #recorro la oración
        if word == 'aack':
            score += 1
        elif word == 'beep':
            score -= 1
    return score

#creo mi columna score
df['score'] = df['sentence'].apply(algoritmo_clasificacion)
#plot_points_and_line(df['aack'], df['beep'], 1, -1, 0)

#create a dictionary
alien = {
    "alien1": {"mood": "Sad", "sentence": "Crack!"},
    "alien2": {"mood": "Sad", "sentence": "Doink doink!"},
    "alien3": {"mood": "Sad", "sentence": "Crack doink!"},
    "alien4": {"mood": "Sad", "sentence": "Crack doink crack!"},
    "alien5": {"mood": "Happy", "sentence": "Doink crack doink doink!"},
    "alien6": {"mood": "Happy", "sentence": "Crack doink doink crack!"},
    "alien7": {"mood": "Happy", "sentence": "Doink doink crack crack crack!"},
    "alien8": {"mood": "Happy", "sentence": "Crack doink doink crack doink!"}
}

#create a dataframe
df2 = pd.DataFrame(alien).T
#replace non characters and lower and create a column with quantity of crack and other column with quantity of doink
df2['crack'] = df2['sentence'].apply(lambda x: x.replace('!', '').replace(',', '').lower().count('crack'))
df2['doink'] = df2['sentence'].apply(lambda x: x.replace('!', '').replace(',', '').lower().count('doink'))


def plot_scatter(x_iterable, y_iterable, x_label="", y_label="", legend=None, **kwargs):
    x_array = np.array(x_iterable)
    y_array = np.array(y_iterable)
    plt.xlabel(x_label)
    plt.xlabel(y_label)
    if legend is not None:
        plt.legend(legend)
    plt.scatter(x_array, y_array, **kwargs)


def draw_line(slope, y_intercept, starting=0, ending=8, **kwargs):
    x = np.linspace(starting, ending, 1000)
    plt.plot(x, y_intercept + slope * x, **kwargs)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a = input()
b= float(input())
def read_and_filter(filename, filter_limit):
    df = pd.read_csv(filename)
    df.columns = ['X','Y']
    son = df[df.Y < filter_limit]
    return son

dataframe = read_and_filter(a, b)
def fix_deformation(dataframe):
    df = dataframe.copy()
    df.columns = ['X','Y']
    df['Y']= (df['Y']/0.5)-5
    df['X']= (df['X']*np.cos(np.pi/4)-(df['Y']*np.sin(np.pi/4)))
    df['Y']= (df['X']*np.sin(np.pi/4)+(df['Y']*np.cos(np.pi/4)))
    df['X']= (df['X']*100)+1500
    df['X'] = df.X.round()
    df = df[df.Y > 0]
    df = df[df.X > 0]
    dataset = df.to_numpy()
    return dataset
data = fix_deformation(dataframe)
print(data)
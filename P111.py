import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import pandas as pd
import statistics
import random

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

dataSet = []
populationMean = statistics.mean(data)
print (populationMean)


def randomSetOfMean(counter):
    dataSet = []
    for i in range (0,100):
        randomIndex = random.randint(0,len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)
    sampleMean = statistics.mean(dataSet)
    sampleStandardDeviation = statistics.stdev(dataSet)
    return sampleMean
def showFig(meanList):
    data1 = meanList
    mean = statistics.mean(data1)
    fig = ff.create_distplot([data1],['reading_time'], show_hist = False )
    fig.add_trace(go.Scatter(x = [ mean,mean], y = [0,1], mode = 'lines', name = 'mean'))
    fig.show()
def standardDev():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(30)
        meanList.append(setOfMeans)
    standardDev = statistics.stdev(meanList)
    print (standardDev)
standardDev()

def setup():
    newmean = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(100)
        newmean.append(setOfMeans)
    showFig(newmean)
    mean = statistics.mean(newmean)
    print (mean)
    return mean
mean = setup()
zscore = (populationMean - mean)/standardDev
print (zscore)

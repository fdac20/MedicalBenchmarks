import parser
import os
import sys
import geojson
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import numpy as np
import random
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib.image import imread
import seaborn as sns
from matplotlib.colors import ListedColormap

def accidentAmount(accidents): 
    # List coordinates:
    print('Number of accidents in 2018 US:', len(accidents))
    accident_tuples = []
    for item in accidents:
        if item['LATITUDE'] != 99.9999 and item['LONGITUD'] != 777.7777:
            accident_tuples.append( (item['LATITUDE'], item['LONGITUD']) )
    return accident_tuples

def generateMapBounds(accident_tuples):
    max_lng, min_lng = -10000,10000
    max_lat, min_lat = 0,10000

    for acc in accident_tuples:
        if max_lng <= acc[1]:
            max_lng = acc[1]
        if min_lng >= acc[1]:
            min_lng = acc[1]

        if max_lat <= acc[0]:
            max_lat = acc[0]
        if min_lat >= acc[0]:
            min_lat = acc[0]

    regular_lat = max_lat-min_lat
    regular_lng = max_lng+(abs(min_lng))

    print("regular_lat: ", regular_lat, "regular_lng: ", regular_lng)
    print("max_lng: ", max_lng, "min_lng: ", min_lng)
    print("max_lat: ", max_lat, "min_lat: ", min_lat)
    extent = [max_lng, min_lng,max_lat,min_lat] #y1,y2,x1,x2
    return (extent, max_lat, min_lat, max_lng, min_lng, regular_lat, regular_lng)

def generateMap(accident_tuples, extent, year, us_shapes, l_tuple):
    max_lat, max_lng, min_lat, min_lng, regular_lat, regular_lng = l_tuple
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(1,1,1, projection=ccrs.PlateCarree())
    ax.imshow(imread('shapes/NE1_50M_SR_W.tif'), origin='upper', transform=ccrs.PlateCarree(), extent=[-180, 180, -90, 90])
    ax.add_geometries(us_shapes, ccrs.PlateCarree(), edgecolor='black', facecolor='none')
    #ax.add_feature(cfeature.BORDERS)
    ax.set_extent(extent)

    #heat_data = np.random.normal(0.0,1.0,size=(400,200))
    heat_data = np.zeros((600,300))

    for item in accident_tuples:
        _lat, _lon = \
                        heat_data.shape[1]*((max_lat-item[0])/regular_lat), \
                        heat_data.shape[0]*((abs(item[1])-abs(max_lng))/regular_lng)
        if heat_data[int(_lon)-1][int(_lat)-1] <= 10:
            heat_data[int(_lon)-1][int(_lat)-1] += 1

    lat = np.linspace(extent[0],extent[1],heat_data.shape[0])
    lon = np.linspace(extent[2],extent[3],heat_data.shape[1])
    print(heat_data.shape, lat.shape, lon.shape)
    Lat,Lon = np.meshgrid(lat,lon)
    print(Lat.shape)
    ax.pcolormesh(Lat,Lon,np.transpose(heat_data), alpha=0.5)
    plt.title('Heatmap of Accidents within the United States - %i'%(year))
    return plt

def generateGraphData(accidents, popEst):
    # Graphing accidents per state:
    INTERSTATE_PREFIXES = ['I-']
    HIGHWAY_PREFIXES = ['HWY', 'US-']

    def checkIfPrefix(word, list_fix):
        for fix in list_fix:
            if fix in word:
                return True
        return False

    state_dict = {}
    for state in accidents:
        if state['STATE'] > 0:
            if checkIfPrefix(state['TWAY_ID'], INTERSTATE_PREFIXES):
                if state['STATE'] in state_dict:
                    state_dict[state['STATE']] += 1
                else:
                    state_dict[state['STATE']] = 1
            else:
                if not state['STATE'] in state_dict: 
                    state_dict[state['STATE']] = 0
    # temp:
    state_dict[72] = 0
    INTER_X, INTER_Y, TOTAL_Y = [], [], []

    for item, row in popEst.iterrows():
        INTER_X.append(row[1])
        INTER_Y.append((state_dict[row[0]]/row[2])*(10**5))
        TOTAL_Y.append(state_dict[row[0]])

    # sort it:
    _INTER_X, _INTER_Y = [], []
    INTER_COM = sorted(zip(INTER_Y,INTER_X))
    for y,x in INTER_COM:
        _INTER_X.append(x)
        _INTER_Y.append(y)

    return _INTER_X, _INTER_Y, TOTAL_Y

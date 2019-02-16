import matplotlib
matplotlib.use('Agg')
from mpl_toolkits.basemap import Basemap
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import os

m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

base_path = r'D:\C Disk Transfer\Desktop\AFPD\other_packages\visualization' + os.sep

def get_coordinates(fileName):
    # print location
    # Create Point objects in map coordinates from dataframe lon
    # and lat values
    # I have a dataframe of coordinates
    
    location = pd.read_csv(base_path + fileName)
    lons = list(location.SIMS_LONGITUDE) #assume the variable name of column longitude is SIMS_LONGITUDE
    lats = list(location.SIMS_LATITUDE)
    x, y = m(lons,lats)
    coordinates = [x, y]
    return coordinates

def graph_base(base_map,map_color,county_color):
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg='w', frame_on=False)
    m.readshapefile(base_path + base_map, name='states', drawbounds=False) #read states shape file
    m.drawcounties(linewidth=0.1,color=county_color)
    #color the states
    for nshape,seg in enumerate(m.states):
        poly = Polygon(seg,facecolor=map_color,edgecolor='w')
        ax.add_patch(poly)
    return fig

# Create a scatterplot on the map
def graph_scatter(x,y,like_color):
#     dev = m.scatter(x,y,20, marker='o', lw=.025,facecolor=like_color, edgecolor='w',alpha=0.3,antialiased=True,zorder=3)
    dev = m.scatter(x,y,3, marker='o', lw=.025,facecolor=like_color, edgecolor='w',alpha=0.3,antialiased=True,zorder=3)

#draw the lines, the center is point 0
def graph_edge(x_center,y_center,x,y,like_color):
    for i in range(len(x)):
        plt.plot([x_center, x[i]], [y_center, y[i]], color=like_color)

# coordinates_wachovia = get_coordinates('wachovia_branch_makeup.csv')
coordinates_wellsfargo = get_coordinates('year_2005_air_monitor_coordinates.csv')

fig = graph_base('st99_d00','red','orange')

# graph_scatter(coordinates_wachovia[0],coordinates_wachovia[1],'blue')
graph_scatter(coordinates_wellsfargo[0],coordinates_wellsfargo[1],'darkorange')

fig.savefig(base_path + 'USMapAirMonitorScatter1.png')

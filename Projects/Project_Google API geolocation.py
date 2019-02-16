import pandas as pd
import os, googlemaps, vincenty
from geopy.geocoders import Nominatim
pd.options.display.expand_frame_repr=False

path = r'C:\便捷\工作\Course\MFIN7033 Advanced Financial Programming and Databases\2018 Fall Projects\Google API geolocation\data'

def fun_geolocation(method):
    '''
    :param method: Int, 1 for googlemaps; 2 for geopy
    :return: Dataframe, result
    '''
    # Import data
    df_addresses = pd.read_excel(os.path.join(path, 'coname_addresses.xlsx'),  index_col=None)
    df_addresses[df_addresses.isnull().iloc[:,1]]
    whiteHouse = (38.8976763, 77.0387185)

    # Construct the dataframe, waiting to be updated
    df_addresses.insert(2,'lat',0)
    df_addresses.insert(3,'lng',0)
    df_addresses.insert(4,'distance',0)

    # Geocoding an address using 1st package
    if method == 1:
        gmaps = googlemaps.Client(key='AIzaSyC3cqIksYVIX4QpsggPEG3V45fDgTVtVbs')
        for i in range(df_addresses.__len__()):
            address = df_addresses.iloc[i,1]
            if df_addresses.iloc[i, 2] != 0:
                print (i)
                continue
            try:
                geocode_result = gmaps.geocode(address)
                df_addresses.iloc[i, 2] = geocode_result[0]['geometry']['location']['lat']
                df_addresses.iloc[i, 3] = geocode_result[0]['geometry']['location']['lng']
                df_addresses.iloc[i, 4] =vincenty.vincenty((df_addresses.iloc[i, 2],df_addresses.iloc[i, 3]),whiteHouse)
            except:
                print('Invalid address, use company name')
                geocode_result = gmaps.geocode(df_addresses.iloc[i,0])
                df_addresses.iloc[i, 2] = geocode_result[0]['geometry']['location']['lat']
                df_addresses.iloc[i, 3] = geocode_result[0]['geometry']['location']['lng']
                df_addresses.iloc[i, 4] = vincenty.vincenty((df_addresses.iloc[i, 2], df_addresses.iloc[i, 3]), whiteHouse)
            print (i)
    elif method == 2:
        # Using 2nd package,not recommended because there are too many missing values and too slow!!!
        geolocator=Nominatim()
        for i in range(1,df_addresses.__len__()):
            address = df_addresses.iloc[i,1]
            if df_addresses.iloc[i, 2] != 0:
                print (i)
                continue
            try:
                geocode_result = geolocator.geocode(address)
                df_addresses.iloc[i, 2] = geocode_result.latitude
                df_addresses.iloc[i, 3] = geocode_result.longitude
                df_addresses.iloc[i, 4] =vincenty.vincenty((df_addresses.iloc[i, 2],df_addresses.iloc[i, 3]),whiteHouse)
            except:
                try:
                    print('Invalid address, use company name')
                    geocode_result = geolocator.geocode(df_addresses.iloc[i,0])
                    df_addresses.iloc[i, 2] = geocode_result.latitude
                    df_addresses.iloc[i, 3] = geocode_result.longitude
                    df_addresses.iloc[i, 4] = vincenty.vincenty((df_addresses.iloc[i, 2], df_addresses.iloc[i, 3]), whiteHouse)
                except:
                    continue
            print (i)
    else:
        print ('Wrong method number! ')
    # Export data

    df_addresses.to_csv(os.path.join(path, 'geolocation_output_data.csv'))
    return df_addresses

if __name__ == '__main__':
    fun_geolocation(1)
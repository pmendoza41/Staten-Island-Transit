#Import useful libraries:
import folium
import pandas as pd

def makeCT(row):
    """
    Adds a padded ID for each census tract, matching what's used in 
    the city's geoJSON file.  
    :param row:  a row in the dataframe, assumes column named "Census Tract"
    :return: returns the census tract as a string of length 6 (padded by 0's)
    """
    ct = row["Census Tract"]
    return "{0:0>6}".format(ct)


#Read in the zoning CSV file 
zones = pd.read_csv('New_York_City_Population_By_Census_Tracts.csv', encoding='latin-1')


#zones = zones[zones.Borough == 'Staten Island']
zones['CTmod'] =zones.apply(makeCT, axis = 1)
print (zones['CTmod'])
#Create choropleth map:
mapZones = folium.Map(location=[40.71, -74.00], 
                      zoom_start=11, 
                      tiles = 'Cartodb Positron')

mapZones.choropleth(geo_path='ctSI.json', 
                  data=zones,
                  columns=['CTmod', 'Population'],
                  key_on='feature.properties.CT2010',
                  fill_color='PuBu', fill_opacity=0.7, line_opacity=0.3,
                  legend_name='Population Density'
                  )

#Create the html file with the map:
mapZones.save(outfile='PopulationZonesSI.html')

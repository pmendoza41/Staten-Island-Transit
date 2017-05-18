#Import useful libraries:
import folium
import pandas as pd

#Read in the zoning CSV file 
zones = pd.read_csv('zoneDist.csv')
print(zones)


#Define a function that will filter zone districts into categories:
    
def filterDist(dist):
    #If has a residential designation:
    if "R1" in dist:
        return 0
    if "R2" in dist:
        return 10
    if "R3" in dist:
        return 20
    if "R4" in dist:
        return 30
    if "R5" in dist:
        return 40
    if "R6" in dist:
        return 50
    if "R7" in dist:
        return 60
    if "R8" in dist:
        return 70
    if "R9" in dist:
        return 80
    if "R10" in dist:
        return 90
    
    else:  #everything else, most likely manufacturing
        return 100

        
#Apply the filter to our dataframe to create a new column:
zones['District Type'] = zones['Zoning District'].apply(filterDist)
print(zones)

#Create choropleth map:

mapZones = folium.Map(location=[40.71, -74.00], 
                      zoom_start=11, 
                      tiles = 'Cartodb Positron')
mapZones.geo_json(geo_path='zoningIDs.json', 
                  data=zones,
                  columns=['arbID', 'District Type'],
                  key_on='feature.properties.arbID',
                  fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.3
                  )


#Create the html file with the map:
mapZones.save(outfile='residentialzoning.html')


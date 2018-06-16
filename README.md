# pyMaps
[pyMaps](https://github.com/Shubh96/pyMaps) is a web application developed using [Python](https://www.python.org/) programming language version 3.6.1 in [Anaconda](https://anaconda.org/anaconda/python) environment. To build the webmap two data sets have been used, one is a text file, [Volcanoes_USA](https://github.com/Shubh96/pyMaps/blob/master/Volcanoes_USA.txt), which contains data about the various volcanoes in the USA and other data set is a [JSON](https://www.json.org/) file, [Population](https://github.com/Shubh96/pyMaps/blob/master/Population.json), that contains data about the population of every country in the world as on 2005 along with several other information.

## Dependencies
In the code, we have used two modules viz a viz, [folium](http://folium.readthedocs.io/en/latest/), which is a module used for data manipulation using data wrangling in python and then visualizing it on a Leaflet map and [pandas](https://pandas.pydata.org/), is a library used for data analysis in python.

## Code Snippets
- `map  = fl.Map(location  = [38, -99], tiles  =  "Mapbox Bright", zoom_start  =  6)` Here we create a map object and set its initial location to any random [latitude, longitude], _tiles_ define the looks of the map which is provided by [Leaflet.js](https://leafletjs.com/) and _zoom_start_ sets the initial zoom for the map.
- `volcanoLayer = fl.FeatureGroup(name = "Volcano Layer")` creates a new layer on the map which will contain the volcano points of USA. Similarly the next line `populationLayer = fl.FeatureGroup(name  =  "Population Layer")` defines one more layer on the map which will represent the population information.
- `Lines 10 - 15` contain some key information which is displayed on the popup when volcano points are clicked.
- `Lines 19 - 21` contain a lambda function stored in a variable ``stylefunc`` which defines the color to be filled in countries having a certain range of population, this will be used later on in the code.
- ``returnColor`` method is used to determine the color for the markers used to demarcate the volcanoes.
- ``Line 38`` adds a child to the populationLayer that we created earlier on, this basically loads the population data into the map using the GeoJson method and it creates polygons for the various countries as shown in the images.
- ``Lines 44 - 55`` are used to generate the information string that is shown in the popup upon clicking the volcano markers.
- As you can see ``Lines 35, 36, 42, 54`` are commented, these were used to create the Metropolis.html file which shows the markers for metropolitan cities in India.
- Lastly, I've added all the layers to the map in ``lines 58 and 59`` and ``line 59`` contains the ``LayerControl()`` method which is basically used to generate a control for the user using which the user can choose to display the layer he wants to see in the map, either  volcano information or population information.

## Screenshots

![Markers denoting metropolitan cities in India](https://github.com/Shubh96/pyMaps/blob/master/metropolis.JPG)
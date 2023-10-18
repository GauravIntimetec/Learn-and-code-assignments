import csv

#cluster containing all the countries which falls in the same grid
cluster = []     #list of dictionaries

with open('world_country_and_usa_states_latitude_and_longitude_values.csv', mode = 'r') as file:
    country_longitude_latitude = csv.reader(file)
    for lines in country_longitude_latitude:
        longitude = lines[2]
        latitude = lines[1]

        for i in range(-18,19):     #these for loops are to traverse the grids 36 * 18 
            for j in range(-9,10):
                if float(longitude)<(i)*10 and float(latitude)<(j)*10 and float(longitude)>(i-1)*10 and  float(latitude)>(j-1)*10:
                    # print(f'country name : {lines[0]}, latitude: {latitude}, longitude : {longitude}, cordinates{i,j}')  #printing the country name as Country, LAtitude, and Longitude
                    cluster.append({'country name' : lines[0], 'latitude': latitude, 'longitude' : longitude, 'cordinates' : (i,j) })
      

countries_data  = {}

for country in cluster:
    countries_data[country['country name']] = country['cordinates']

# print(countries_data)

grouped_countries = {}
for country, coordinates in countries_data.items():
    if coordinates in grouped_countries:
        grouped_countries[coordinates].append(country)
    else:
        grouped_countries[coordinates] = [country]
# print(grouped_countries)

num = 0
for coordinates, countries in grouped_countries.items():       #For loop used to print Fancy looking output
    print(f'Coordinates {coordinates}: {countries}')
    num+=1
print(num)








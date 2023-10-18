import csv

def read_country_data(file_path):
    cluster = []  # List of dictionaries containing country data
    with open(file_path, mode='r') as file:
        country_longitude_latitude = csv.reader(file)
        for lines in country_longitude_latitude:
            longitude = float(lines[2])
            latitude = float(lines[1])
            for i in range(-18, 19):      #these for loops are to traverse the grids 36 * 18 
                for j in range(-9, 10):
                    if (i - 1) * 10 < longitude <= i * 10 and (j - 1) * 10 < latitude <= j * 10:
                        cluster.append({'country name': lines[0], 'latitude': latitude, 'longitude': longitude, 'coordinates': (i, j)})
    return cluster

def organize_countries_by_coordinates(cluster):
    countries_coordinates = {}
    for country in cluster:
        countries_coordinates[country['country name']] = country['coordinates']
    grouped_countries = {}
    for country, coordinates in countries_coordinates.items():
        grouped_countries.setdefault(coordinates, []).append(country)
    return grouped_countries

def print_grouped_countries(grouped_countries):
    num = 0
    for coordinates, countries in grouped_countries.items():
        print(f'Coordinates {coordinates}: {countries}')
        num += 1
    return num

def main():
    file_path = 'world_country_and_usa_states_latitude_and_longitude_values.csv'
    cluster = read_country_data(file_path)
    grouped_countries = organize_countries_by_coordinates(cluster)
    num_groups = print_grouped_countries(grouped_countries)
    print(f'Total number of groups: {num_groups}')

if __name__ == "__main__":
    main()

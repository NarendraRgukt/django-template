import csv
import json

csv_file_path = 'restaurants_small.csv'#path to the csv file
fixture_file_path = 'searchapp/fixtures/data.json'# this is the path to the fixtures file for this you have to add directory in settings.py file

def csv_to_dict_list(csv_file_path):#convert the csv file into the list of dictionaries
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            row['model'] = 'searchapp.restaurant'  # Add the model name
            row['fields'] = {                      #these are the fields of the model
                'name': row['name'],
                'location': row['location'],
                'items': json.loads(row['items'].replace('""', '"')),
                'lat_long': row['lat_long'],
                'full_details': row['full_details'],
            }
            data.append(row)
        return data

data = csv_to_dict_list(csv_file_path) #list of dictionaries are stored in the data variable,where each dictionary represent the row of csv file

with open(fixture_file_path, 'w') as file:
    file.write(json.dumps(data, indent=4)) # converting list of dictionaries into json format with indendation of 4 spaces

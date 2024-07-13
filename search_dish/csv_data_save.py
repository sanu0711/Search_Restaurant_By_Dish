import pandas as pd
import json
from .models import Restaurant

def csv_data_to_sqlite():
    df = pd.read_csv('./static/csv_data/restaurants_small.csv')
    # Restaurant.objects.all().delete()
    for index, row in df.iterrows():
        id = row['id']
        name = row['name']
        location = row['location']
        if pd.isna(row['full_details']):
            address = 'NA'
        else:
            address = json.loads(row['full_details'])['location']['address']
        items = json.loads(row['items'])
        Restaurant.objects.create(
            id=id, 
            name=name, 
            location=location, 
            address=address, 
            items=items
            )
       
    print('Data saved to sqlite')
import csv
import json
from django.core.management.base import BaseCommand
from searchapp.models import Restaurant

class Command(BaseCommand):
    help = 'Loads data from CSV file into the Restaurant model'

    def handle(self, *args, **options):
        csv_file = 'restaurants_small.csv'  # Update with the actual CSV file name if different

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                items = json.dumps(eval(row['items']))
                full_details = json.dumps(eval(row['full_details']))
                Restaurant.objects.create(
                    name=row['name'],
                    location=row['location'],
                    items=items,
                    lat_long=row['lat_long'],
                    full_details=full_details
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

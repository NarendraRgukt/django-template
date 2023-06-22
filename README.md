Open the searchproject directory
Navigate to the Scripts folder in the myenv folder and then activate the virtual environment by myenv
Navigate back to the root project
For converting the csv data into fixtures run the csv_to_fixtures.py file 
After running the file run the following command
python manage.py loaddata data.json
Here data.json is the file that stores the fixtures
After running the loaddata it will create the object in the model for each row in csv file
For running the project you can do the following command
python manage.py runserver
Open the searchproject directory<br>
Navigate to the Scripts folder in the myenv folder and then activate the virtual environment by myenv<br>
Navigate back to the root project<br>
For converting the csv data into fixtures run the csv_to_fixtures.py file <br>
After running the file run the following command<br>
python manage.py loaddata data.json<br>
Here data.json is the file that stores the fixtures<br>
After running the loaddata it will create the object in the model for each row in csv file<br>
For running the project you can do the following command<br>
python manage.py runserver<br>
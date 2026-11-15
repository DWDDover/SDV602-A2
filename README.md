To install the required packages use:

``pip install -r requirements.txt``

To run the application in local mode use 

``data_explorer/app.py --local``

To run the applciation in remote mode use 

``data_explorer/app.py --remote``

To run the applications headless testing use 

``data_explorer/app.py --testing``

In order to set up the database the config.py file in data_explorer/data 
needs to have its path match the port of your local computers mongo process

``MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")``

Test data can be found in data_explorer/test_data. This data can be used within all the functionalilty and is in a vlaid format to test the append method.
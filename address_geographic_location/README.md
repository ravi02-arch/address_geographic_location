INTRODUCTION

- This project determines the latitude and longitude of a given address
 
FLASK APP STRUCTURE
 
  app
    - api_manager
			- __init__.py
			- address_details_processing.py

	- blueprints
			- get_address_details.py
			
	- configs
			- security_key_config.py
			- url_config.py
 
	- helper
			- app_logger.py
			
  README.md
  
  requirements.txt
  
  run.py
  
  
GETTING STARTED

- Change to the project directory: cd .\address_geographic_location
- If you want to use virtualenv: virtualenv venv
                                 venv\scripts\activate
- Install dependencies with pip: pip install -r requirements.txt

- Then, run the application:
		- python run.py
		
To test the  application, access this url in postman:

	http://localhost:5000
	
API END POINT(POST)
	- /getAddressDetails# address_geographic_location

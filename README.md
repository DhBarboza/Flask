# Flask
studying the flask framework

### Preparing environment:
Prepare the environment and install initial dependencies
#### Install virtual environment:
- pip install virtualenv

#### Start virtual environment with the version of python you want to use:
- virtualenv -p python3 venv

#### initialization of the virtual environment:
-  . venv/Scripts/activate

#### install Flask:
- venv/Scripts/pip3 install flask

#### install Packages:
- venv/Scripts/pip3 install flask-sqlalchemy

#### Check installed packages:
- venv/Scripts/pip3 freeze

#### command to generate a file with information about the packages used in the application:
- venv/Scripts/pip3 freeze > requirements.txt

#### To install the necessary application dependencies / packages:
- venv/Scripts/pip3 isntall -r requirements.txt
# Development SetUp
1. Install virtualvenv library using this command `pip install virtualvenv`. If pip is not installed in the system then check the link below to install it.<br> 
Link: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

2. Fork this repo and clone it in your system.

3. Start a virual environtment inside your local repo using the following command. `python -m virtualenv {name of the virtualenv}` eg: `python -m virtualenv venv`. <br>
__Note:__ The virtual environment directory should be inside of the project directory.

4. Activate the virtual environment:<br>
__Linux__
`source /path/to/env/bin/activate`<br>
__Windows__
`\path\to\env\Scripts\activate.bat`

5. Once activated, install the required dependencies or libraries using the following command.<br>
`pip install -r requirements.txt`

6. Create a new branch of the repo using the following command.<br>
`git checkout -b <name of the branch>` 

# Run the Server
1. Go to the /src directory, make sure there is a `manage.py` script inside and run the following commands.<br>
  a. `python manage.py makemigrations`<br>
  b. `python manage.py migrate`<br>
  c. `python manage.py createsuperuser`<br>
  d. `python manage.py runserver`<br>

__Note: Make sure to run a and b everytime you fetch the recent changes from original remote repository (aka technical-geeth/Forevision-Digital or ORR)__

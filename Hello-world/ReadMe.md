# First Flask App

Initialize a new virtual environment using this command:
```
python3 -m venv .venv
```
>where the second `.venv` is the environment name.

Generally it is recommended to use a virtual environment while building a Flask application.

After that, change the python interpreter in your IDE to use this environment instead of the default one.

You must activate the virtual environment from the terminal for it to start installing packages. Run the following command in the terminal:
```
source .venv/bin/activate
```

You can now start installing packages to this virtual environment. Lets run this and install Flask:
```
pip3 install flask
```

>You can use `pip3 freeze` to check for the installed packages.

We can create a python file and import Flask as below:
```
from flask import Flask

app = Flask(__name__)
```

Use `pip3 freeze > requirements.txt` to feed all the packages to a file. These can be installed again later by running `pip3 install -r requirements.txt`
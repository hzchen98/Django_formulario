# Django_formulario
Web de publicación de formularios para rellenar dichos documentos

# Getting Started

Used IDE : PyCharm

Requirements: 
   Python 3.+ -> libraries: Django 3.+ , PyPDF2, reportlab, freeze, WhiteNoise
               
# Deployment
* Once you have the project, create the virtual enviroment (venv) for it:
```
python -m venv path_located/Django_formulario
```
* Install all required libraries with the follow command: 
```
pip install -i requirements.txt
```
* Collect all static resources from django: 
```
python manage.py collectstatic
```
* Checkout the master branch and run manage.py with the follow command:
```
python manage.py runserver [Port to establish the server]
```

# Existential issues
ConnectionAbortedError: [WinError 10053] -> due to firewall or antivirus programs, the socket with the client it's shutted down. Mainly it happens when the aplication is running over Windows system. But this issue doesn't affect the performance of the application.


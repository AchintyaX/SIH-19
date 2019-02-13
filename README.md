# SIH 19
this the codebase for our project for SIH 19 
# How to Install
1. create a git clone 
2. create virtual env
3. run the command `python3 -m venv myenv`
4. activate the virtual env using ` . myvenv/bin/activate`
5. run the command `pip install -r requirements.txt`
6. run `python manage.py migrate`
7. run `python manage.py runserver`
8. go to ` http://127.0.0.1:8000` 
9. run `python manage.py makemigrations myapp`
10. run `python manage.py migrate myapp` 
11. run `python manage.py createsuperuser` 
12. fill in the details 

# How to test run it 
1. go to ` http://127.0.0.1:8000/admin`
2. sign in using your superuser credentials
3. then you can add data to the database using the UI 
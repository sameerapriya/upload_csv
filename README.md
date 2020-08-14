For this project python3.8 , Pandas , Django has been used.

To see the working of the Repository :

STEP 1: In your CLI go to the folder you desire to save this repository.
        Clone the Repository with the following command.
        
        `git clone <url of the repository>`
        
STEP 2: After the clone create a virtual environment using the command
        
        `virtualenv -p python3.8 venv`
        
STEP 3: Activate the virtual environment
        
        if Windows use ,
            `venv\Scripts\activate`
        if Linux use,
            `source venv/bin/activate`
            
STEP 4: Create a POSTGRESQL DB in your system with a encrypted user(who has a password)
        pass those values in the settings.py file 
        
        `'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your db name',
        'USER': 'your username',
        'PASSWORD': 'your password',
        'HOST': '127.0.0.1' or 'localhost',
        'PORT': ''
    }`
    
STEP 5: To install the required packages 
        
        `pip install -r requirements.txt`
        
STEP 6: To register the models run the following commands.
       
        `python3 manage.py makemigrations`
        `python3 manage.py migrate`

STEP 7: To see the working of the project, go to the 'upload/' url.
        Run the command
       
        `python3 manage.py runserver`    

        

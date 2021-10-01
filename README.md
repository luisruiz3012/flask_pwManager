# flask_pwManager
This is a similar project to the pwManager project where you can use a terminal visual interface, but it is an improved version whici implement the use of the **Flask** framework, along with **Python** and **MySQL** to create a graphical interface for the password manager project with the purpose of practicing MySQL database management and connection, as well as Flask and backend development with a simple python project that allows you to run a local password manager on your computer, and now with the flask framework, you can also have a more intuitive user interface to manage your password.

## Database Sctipt (Make sure to have MySQL installed)
Copy the following comands on a MySQL RDBMS (MySQL Workbench) or on a Terminal

- **Create the database**
       
      CREATE DATABASE password_manager;
      
- **Access to the database**
    
      USE password_manager;

- **Create the login table**

      CREATE TABLE login(
      id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
      name VARCHAR(100) NOT NULL,
      user VARCHAR(100),
      password VARCHAR(100) NOT NULL,
      email VARCHAR(255)
      );
      
## Installation
You can use the following command in order to copy the github repository and run this program locally on your computer
    
    git clone https://github.com/luisruiz3012/flask_pwManager.git

## After installing
Copy the Github repository on your computer, then install the requirement on the ***requirement.txt*** file with the following command:
      
    pip install requirement.txt

Once you have the requirements installed, your can do one if this 2 thing:

- Run the program with the following command(Keep in mind that this will ask you to enter you DB user and password twice):
    
      python3 app.py
      
- Open the app.py file and change the following lines:

      app.config['MYSQL_USER'] = getpass('Enter your username: ') # This will be asked twice (replace)
      app.config['MYSQL_PASSWORD'] = getpass('Enter the main password: ') # This will be asked twice (replace)
  
  You can replace them with:
      
      app.config['MYSQL_USER'] = 'Your_database_user'
      app.config['MYSQL_PASSWORD'] = 'Your_database_password'

Then, you can finally run the program with the following command:

    python3 app.py

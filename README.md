##  Project 
##
This project uses Flask framework based.  The project is pubished in pythonanywhere.com. 
https://chlau5206.pythonanywhere.com
This Flask project is using Blueprint, Bulma, SQLAlchemy, Login-Manager, Flask-WTF, Logging.

Flask project using:
1. Blueprint , made modular portable and independant
2. Bulma's CSS
3. SQLAlchemy (SQLite3)
4. Login-Manager 
5. Flask-WTF for handling forms.
6. Logging
7. Flask-Mail for email -- not implemented, due to require oAuth.

=====================
= Project structure =
=====================
ChlauApp/
│
├── ChlauApp/
│   ├── __init__.py       # Initializes the Flask app and extensions (SQLAlchemy, Login-Manager, Configuration file for your Flask app (e.g., SECRET_KEY, database URI))
│   ├── models.py         # Defines SQLAlchemy database models
│   ├── FormModels.py     # Contains WTForms for the Login module
│   ├── views.py          # Defines routes for the main application
│   │   
│   ├── static/           # Contains global static files like CSS, JavaScript, and images
│   │   ├── css/
│   │   │   ├── bulma.min.css
│   │   │   ├── NotoSanFonts.css
│   │   │   ├── global_styles_.css
│   │   │   └── ExchangeRates.css
│   │   ├── data/
│   │   │   └── LatesRate.json
│   │   ├── Fonts/
│   │   │   ├── NotoSans-VariableFont_wdth,wght.ttf
│   │   │   ├── NotoSansDisplay-VariableFont_wdth,wght.ttf
│   │   │   └── NotoSansDisplay-Italic-VariableFont_wdth,wght.ttf
│   │   ├── img/
│   │   │   └── logo.jpg
│   │   └── js/
│   │       ├── layout.js
│   │       └── ExchangeRates.js
│   │   
│   ├── templates/        # Contains HTML template files for rendering views
│   │   ├── layout.html 
│   │   ├── home.html 
│   │   ├── exchangeRate.html 
│   │   └── error404.html 
│   │   
│   ├── about/              # about me
│   │   ├── static/           # Contains "about" static files like CSS, JavaScript, and images
│   │   │   └── css/
│   │   │      └── styles.css
│   │   ├── templates/
│   │   │   └── index.html
│   │   ├── __init__.py
│   │   ├── views.py
│   │   └── models.py
│   │   
│   ├── auth/           # user-management authenication
│   │   ├── templates/
│   │   │   ├── auth_first_user.html
│   │   │   ├── auth_login.html
│   │   │   ├── auth_main.html
│   │   │   ├── auth_register.html
│   │   │   └── auth_update.html
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── auth__form.py
│   │   
│   ├── Board/              # Board (Contact me)
│   │   ├── templates/
│   │   │   ├── board.html
│   │   │   ├── board_general_add.html
│   │   │   └── board_reply_.html
│   │   ├── Board.py
│   │   └── BoardModels.py
│   │   
│   ├── members/ 
│   │   ├── templates/
│   │   │   └── members.html
│   │   ├── __init__.py
│   │   └── members.py
│   │   
│   └── test1/    # project template
│       ├── static/           
│       │   └── css/
│       │       └── styles.css
│       ├── templates/
│       │   └── index.html
│       ├── __init__.py
│       ├── views.py
│       ├── models.py
│       └── forms.py
│
├── instance/               # SQLite3 database file
│   ├── sys.db              # Production database file
│   └── dev.db              # Development database file
│
├── migrations/             # Directory for database migrations
│
├── tests/                  # Unit tests for your application
│
├── .env                    # Production environment configuration
├── .env.development        # Production environment configuration
├── README.md               ## This file
├── runapp.py               # Entry point to run the Flask application
└── requirements.txt        # List of Python dependencies for the project





## Note: pythonanywhere need to renew the website every 3 month.

## install ChlauApp with VSCode
1. Create project folder
2. CD to project folder
3. Create virtual environment from VSCode
	>> Ctrl+Shift+P , select create environment
4. Bash >  git clone {github repo}
5. Create launch configuration { launch.json }

## Note: 
1. If SQLite databse needs rebuild.  Delete instance folder, it will recreate.
2. Exchange rate json (LatestRate.json) required from API service.

=====================================

Deploy to Web host

#1. To reset your Git repository to the last commit.
[Bash]
git reset --hard HEAD

#2. Discard local changes -- reset to last commit
	Method 1:
	## discard uncommitted changes
	git checkout -- . 
	## discard changes and remove untracked files
	git clean -fd
	Method 2:
	Reset your local repository to match the remote: This will discard your local changes and overwrite everything with the files from the GitHub repository.
	Bash
	git reset --hard orgin/main

#3. pull repo without commend
git pull origin feature-branch --no-edit

#4. Temporarily saves your local changes, and apply them later.
1$ git stash
2$ git pull origin <feature-branch>
3$ git stash apply

=====================================

Automate this entire process—running Python code, copying files, and committing/pushing to 
a Git repository—using a combination of Python scripting and Git hooks(e.g., pre-push hook).


1. Write the Python Script to Generate the Supplement file
import shutil

def generate_file():
    # Generate the supplementary file (example content)
    with open("supplement.txt", "w") as f:
        f.write("This is the generated supplement file.\n")
    print("Supplement file generated.")

def copy_file():
    source = "supplement.txt"
    destination = "/path/to/specific/folder/supplement.txt"  # Change to your folder
    shutil.copy(source, destination)
    print(f"File copied to {destination}.")

if __name__ == "__main__":
    generate_file()
    copy_file()

2. Set Up a Git Hook (e.g. pre-push)


3. Push Your Changes to the Repository


4. Optional Improvenments


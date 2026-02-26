##  Project: Web Portfolio & Lab Demo
##
Technologies: Python, Flask (Blueprints), Bulma CSS, SQLAlchemy (SQLite), Flask-Login, Flask-WTF, Logging

Modular Architecture: Engineered a modular web application using Flask Blueprints to ensure independent, portable, and scalable component management.

Security & Auth: Implemented secure user authentication and session management using Flask-Login and SQLAlchemy, including protected routes and hashed credentials.

Systems Monitoring: Integrated a robust Logging framework to track application health, user activity, and system errors—essential for root-cause analysis in production environments.

Responsive UI: Developed a clean, professional front-end using Bulma CSS, prioritizing mobile-friendly design and high-performance asset loading.

Data Integrity: Utilized Flask-WTF for secure form handling, including CSRF protection and server-side validation to ensure data quality.

=====================
= Project structure =
=====================
ChlauApp/
│
├── ChlauApp/
│   ├── __init__.py       # Initializes the Flask app and extensions (SQLAlchemy, Login-Manager, Configuration file for your Flask app (e.g., SECRET_KEY, database URI))
│   ├── models.py         # Defines SQLAlchemy database models
│   ├── LoginForms.py     # Contains WTForms for the Login module
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


project/
│
├── static/
│   ├── css/
│   │   ├── bulma.min.css
│   │   ├── global_styles.css
│   │   └── layout.css (optional)
│   ├── js/
│   │   ├── layout.js        <-- global JS
│   │   └── global_utils.js  <-- optional
│   └── img/
│       └── logo.png
│
├── home2/
│   ├── templates/
│   │   └── home2.html
│   └── static/
│       ├── css/
│       └── js/
│
├── about2/
│   ├── templates/
│   │   └── about2.html
│   └── static/
│       ├── css/
│       └── js/
│
├── exchange_rate/
│   ├── templates/
│   └── static/
│
└── boardDemo/
    ├── templates/
    └── static/


project_name/
│
├── __init__.py
├── routes.py
├── models.py          (optional, if project uses DB)
│
├── templates/
│   └── project_name/
│       └── project.html     ← main project page
│
├── static/
│   ├── css/
│   │   └── project.css      ← optional, project-specific styling
│   ├── js/
│   │   └── project.js       ← optional, project-specific JS
│   └── img/
│       ├── screenshot1.png
│       ├── screenshot2.png
│       └── diagram.png
│
└── data/                    ← optional (downloads, sample files)
    └── sample.epub


## Note: pythonanywhere need to renew the website every 3 month.

# Commit the "Skeleton" On your local machine (PC), commit these changes and push to GitHub:
Bash
git add .
git commit -m "Admin: Added WorkDirectory skeleton and updated ignore rules"
git push origin main

# The PAW "Sync" Now, on PythonAnywhere:
Bash
git fetch origin main
git reset --hard origin/main


Optional:
# to reset your Git repository to the last commit (discard every changed, --soft for kept change in staged)
$ git reset --head HEAD     

# update files only, no new file add or delete
$ git fetch

# 9. Temporarily saves your local changes, and apply them later.
$ git stash
$ git pull origin [main | <feature-branch>]
$ git stash [apply | pop]


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


##  Project: Web Portfolio & Lab Demo
Technologies: Python, Flask (Blueprints), Bulma CSS, SQLAlchemy (SQLite), Flask-Login, Flask-WTF, Logging

Modular Architecture: Engineered a modular web application using Flask Blueprints to ensure independent, portable, and scalable component management.

Security & Auth: Implemented secure user authentication and session management using Flask-Login and SQLAlchemy, including protected routes and hashed credentials.

Systems Monitoring: Integrated a robust Logging framework to track application health, user activity, and system errors—essential for root-cause analysis in production environments.

Responsive UI: Developed a clean, professional front-end using Bulma CSS, prioritizing mobile-friendly design and high-performance asset loading.

Data Integrity: Utilized Flask-WTF for secure form handling, including CSRF protection and server-side validation to ensure data quality.

=====================
= Project structure =
=====================
## Updated project structure
ChlauApp
├── ChlauApp/
│   ├── About2/
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── abouts.css
│   │   │   ├── data/
│   │   │   │   └── Current_Resume.pdf
│   │   │   └── js/
│   │   │       └── about2.js
│   │   ├── templates/
│   │   │   └── About21.html
│   │   ├── __init__.py
│   │   ├── about2.py
│   │   └── SelfNotes.txt
│   ├── AppAdmin/
│   │   ├── adminBoard/
│   │   │   ├── static/
│   │   │   ├── templates/
│   │   │   │   ├── _board_admin_add.html
│   │   │   │   ├── _board_reply.html
│   │   │   │   └── board.html
│   │   │   ├── __init__.py
│   │   │   ├── adminBoard.py
│   │   │   └── BoardModels.py
│   │   ├── auth/
│   │   │   ├── static/
│   │   │   │   └── js/
│   │   │   │       └── auth.js
│   │   │   ├── templates/
│   │   │   │   ├── auth_first_user.html
│   │   │   │   ├── auth_login.html
│   │   │   │   ├── auth_main.html
│   │   │   │   ├── auth_register.html
│   │   │   │   └── auth_update.html
│   │   │   ├── __init__.py
│   │   │   ├── auth_form.py
│   │   │   └── auth.py
│   │   ├── members/
│   │   │   ├── templates/
│   │   │   │   └── members.html
│   │   │   ├── __init__.py
│   │   │   ├── LoginForms.py
│   │   │   ├── members.py
│   │   │   └── models.py
│   │   ├── .gitignore
│   │   ├── LICENSE
│   │   └── README.md
│   ├── Board/
│   │   ├── static/
│   │   │   └── css/
│   │   │       └── board_add.css
│   │   ├── templates/
│   │   │   └── board_general_add.html
│   │   ├── __init__.py
│   │   └── Board.py
│   ├── Home2/
│   │   ├── static/
│   │   │   └── css/
│   │   │       └── home2.css
│   │   ├── templates/
│   │   │   └── home2.html
│   │   ├── __init__.py
│   │   └── home2.py
│   ├── logs/
│   │   └── app.log
│   ├── Projects/
│   │   ├── BoardDemo/
│   │   │   ├── static/
│   │   │   │   ├── css/
│   │   │   │   │   ├── board_add.css
│   │   │   │   │   └── demo.css
│   │   │   │   └── img/
│   │   │   │       ├── DemoAddMsg2026-03-15.jpg
│   │   │   │       └── DemoShowMsg2026-03-15.jpg
│   │   │   ├── templates/
│   │   │   │   ├── boardDemo_add.html
│   │   │   │   ├── boardDemo.html
│   │   │   │   └── project_board.html
│   │   │   ├── __init__.py
│   │   │   ├── BoardDemoModels.py
│   │   │   ├── demoBoard.py
│   │   │   └── routes_boardDemo.py
│   │   ├── ePubConverter/
│   │   │   ├── static/
│   │   │   │   └── img/
│   │   │   │       └── ePubConverterScreenShot.jpg
│   │   │   ├── templates/
│   │   │   │   └── project_conv.html
│   │   │   ├── __init__.py
│   │   │   ├── LICENSE
│   │   │   └── routes_ePubConverter.py
│   │   ├── ExchangeRates/
│   │   │   ├── data/
│   │   │   │   ├── Archive/
│   │   │   │   │   └── ExchangeRate_2026-03-17.json
│   │   │   │   ├── ExchangeRate_2026-03-19.json
│   │   │   │   ├── ExchangeRate_2026-03-24.json
│   │   │   │   └── LatestRate.json
│   │   │   ├── static/
│   │   │   │   ├── css/
│   │   │   │   │   ├── demo.css
│   │   │   │   │   └── ExchangeRates.css
│   │   │   │   ├── img/
│   │   │   │   │   ├── ExcRateViewer2026-03-25_dark.jpg
│   │   │   │   │   └── ExcRateViewer2026-03-25_light.jpg
│   │   │   │   └── js/
│   │   │   │       └── ExchangeRates.js
│   │   │   ├── templates/
│   │   │   │   ├── exchangeRate.html
│   │   │   │   └── project_exch.html
│   │   │   ├── __init__.py
│   │   │   ├── API_ExchangeRate.py
│   │   │   ├── ExchangeRate_DevNote.txt
│   │   │   ├── ExchangeRates.py
│   │   │   └── routes_exch_rate.py
│   │   └── Proj_template/
│   │       ├── statics/
│   │       │   ├── css/
│   │       │   ├── data/
│   │       │   ├── img/
│   │       │   └── js/
│   │       ├── templates/
│   │       │   └── project_page.html
│   │       ├── __init__.py
│   │       └── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── _table_old.css
│   │   │   ├── bulma.min.css
│   │   │   ├── global_styles.css
│   │   │   ├── Noto_lang.css
│   │   │   ├── NotoSansFonts.css
│   │   │   └── table.css
│   │   ├── data/
│   │   │   └── LICENSE
│   │   ├── Fonts/
│   │   │   ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
│   │   │   ├── NotoSans-VariableFont_wdth,wght.ttf
│   │   │   ├── NotoSansDisplay-Italic-VariableFont_wdth,wght.ttf
│   │   │   └── NotoSansDisplay-VariableFont_wdth,wght.ttf
│   │   ├── img/
│   │   │   └── logo.jpg
│   │   └── js/
│   │       ├── _autoFlash.js
│   │       └── layout.js
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

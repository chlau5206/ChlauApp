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
│   │   └── layout.html
│   ├── utils/
│   │   ├── data/
│   │   │   ├── ePubConverter_Source.zip
│   │   │   ├── ePubConverter.zip
│   │   │   └── Test_参加奥运.epub
│   │   └── obsolete.py
│   ├── __init__.py
│   ├── extensions.py
│   ├── LICENSE
│   ├── ReleaseNote.txt
│   ├── SelfNotes.txt
│   └── views.py
├── instance/ 			--> SQLite3 database file
│   ├── sys.db   --> Production database file		
│   ├── demo.db   --> Demo database file (in momery)
│   └── dev.db  	--> Development database file	
├── migrations/
│   └── versions/
├── .env		
├── .env.dev 
├── .env.keys	  	--> dummie env.keys
├── .env.seckeys    --> Real secret keys
├── .gitattributes
├── .gitignore
├── BugReport.txt
├── README.md
├── requirements.txt
└── runapp.py


## Note: pythonanywhere need to renew the website every 3 month.
# directly replace your local files in PythonAnywhere with the remote repository's files, use:
$ git fetch origin    # Fetch remote changes
$ git reset --hard origin/<branch-name>    # Reset your branch

- This will ensure that your local branch exactly matches the remote branch, including adding or deleting files as necessary.

Optional:
# to reset your Git repository to the last commit (discard every changed, --soft for kept change in staged)
$ git reset --head HEAD     

# update files only, no new file add or delete
$ git fetch

# 9. Temporarily saves your local changes, and apply them later.
$ git stash
$ git pull origin <feature-branch>
$ git stash apply


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


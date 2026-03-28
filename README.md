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



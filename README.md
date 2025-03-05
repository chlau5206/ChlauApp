## Project 
This project uses Flask framework based.  The project is posted in pythonanywhere.com. 
https://chlau5206.pythonanywhere.com

## Note: pythonanywhere need to renew the website every 3 month.

## install ChlauApp with VSCode
1. Create project folder
2. CD to project folder
3. Create virtual environment from VSCode
	>> Ctrl+Shift+P , select create environment
4. Bash >  git clone {github repo}
5. Create launch configuration { launch.json }

## Note: Update codes
1. SQLite databse needs rebuild.  Delete instance folder, it will recreate.


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


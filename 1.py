import os
import datetime
import shutil

path = input("Give A Path To Clear Files And Folders : ")
days = int(input("For Clearing The Files And Folders Give The Number Of Days Limit : "))

exist = os.path.exists(path)

if(exist == False):
    print("Please provide a valid path")
    path = input("Give A Path To Clear Files And Folders : ")
    
if(os.path.isfile(path)):
    print("Please provide a path of directory")
    path = input("Give A Path To Clear Files And Folders : ")
    
for root, dirs, files in os.walk(path, topdown=False):
    for file in files:
        full_path = os.path.join(root, file)
        presentTime = datetime.datetime.now()
        file_cre_time = datetime.datetime.fromtimestamp(os.path.getctime(full_path))
        no_of_days = (presentTime - file_cre_time).days
        if(no_of_days >= days):
            os.remove(full_path)
            print("Congratulations!! Yor pc is now clean with unwanted files")
    for i in dirs:
        fol_path = os.path.join(root, i)
        if len(os.listdir(fol_path)) == 0:
            shutil.rmtree(fol_path)
            print("Congratulations!! Yor pc is now clean with unwanted files")
        
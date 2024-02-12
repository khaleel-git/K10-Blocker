import os
import datetime,shutil

# working dir
working_dir = 'C:\\Users\\emahkah\\OneDrive - Ericsson\\Documents\\GitHub\\K10-Blocker\\'
source_exe = "C:\\Users\\emahkah\\OneDrive - Ericsson\\Documents\\GitHub\\K10-Blocker\\dist\K10_Blocker.exe"
dest_exe = "C:\\Program Files (x86)\\K10_Blocker\\K10_Blocker.exe"
# Change directory
repo_path = working_dir
os.chdir(repo_path)

# Git commands
# {datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}
try:
    os.system("pyinstaller --onefile K10_Blocker.py -y")
    os.system("git add .")
    os.system(f"git commit -m {datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}")
    os.system("git pull")
    os.system("git fetch")
    os.system("git push -u origin master")
    print("Git operations completed successfully")
except Exception as e:
    print("Error during git operations:", e)

try:
    shutil.copy(source_exe, dest_exe)
    print("File copied successfully.")
# If source and destination are same
except shutil.SameFileError:
    print("Source and destination represents the same file.")


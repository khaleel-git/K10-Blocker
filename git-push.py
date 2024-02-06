import os
import datetime,shutil

# working dir
working_dir = 'C:\\Users\\emahkah\\OneDrive - Ericsson\\Documents\\GitHub\\K10-Blocker\\'
# Change directory
repo_path = working_dir
os.chdir(repo_path)

# Git commands
# {datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}
try:
    os.system("git add .")
    os.system(f"git commit -m {datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}")
    os.system("git pull")
    os.system("git fetch")
    os.system("git push -u origin master")
    print("Git operations completed successfully")
except Exception as e:
    print("Error during git operations:", e)

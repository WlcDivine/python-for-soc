from pathlib import Path 


log_folder = Path("Security_log")


if not  log_folder.exists():

    print("file not exists")


elif(not log_folder.is_dir):

    print("file is not a dir")

else:
    log_files = list(log_folder.glob("*.log"))
    # here rglob is use recursive which is used to check subfolders also 
    print("log were found:  ",len(log_files),"log files")
    for file_path in log_files:
        print(file_path.name) 
    
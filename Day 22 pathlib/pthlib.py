from pathlib import Path
file_path = Path("alert.txt")
print(file_path)
print(type(file_path))
# it doest help to now about the path actually exists or not 



# their fore we use five essential pathlib opertation 

#  1> exists()  - to check if the path exists or not
if file_path.exists():
    print("File exists")
else:
    print("Path doesn't exist")

# 2> is_file() - to check if the path is a file or not
# to check dir we use is_dir() method
print(file_path.is_file())


#3> check file name and their extension 
path = Path("/log/firewall.log")
print(path.name)
print(path.suffix)
# suffices help to get extension stem use to get file name without extension

#4> create a dir 
log_folder =Path("Security_log")
log_folder.mkdir(exist_ok=True) 
# exist_ok=True will not raise error if dir already exists
print("dir is formed ")


# 5> join path correctly
folder = Path("Security_log")
file_in_folder = folder / "alert.txt"
print(file_in_folder)
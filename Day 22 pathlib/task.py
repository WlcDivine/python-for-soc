from  pathlib import Path


folder = Path("soc_log")

if folder.exists():

    print("Path is exist")
    print("It is a directory ",folder.is_dir)


else :

    folder.mkdir(exist_ok=True)
file_path = folder/"new_log.log"


with file_path.open("w") as file:
    file.write("Hellow world")

log = list(folder.glob("*.log"))


for lo in log :
    print(f"log name : {lo.stem} their extension are {lo.suffix}")

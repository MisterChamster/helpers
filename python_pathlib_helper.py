from pathlib import Path

my_path = Path("/path/to")
my_path = my_path / "file.txt"

#Strings
#                         dir example | file example
print(my_path.name) #     Desktop     | file.txt
print(my_path.parent) #   /path/to    | /path/to
print(my_path.suffix) #   ''          | .txt
print(my_path.stem)   #   Desktop     | file

#Stats object with metadata and stuff
my_path.stat()

# Returns text that is contained in path
print(my_path.read_text()) #Only on file!

#Booleans
print(my_path.is_dir())
print(my_path.is_file())
print(my_path.exists())

#Generators of Pathlib objects
print(my_path.iterdir()) #Only on dir! Can iterate over to fill list

#Pathlib objects
print(Path.cwd())     #cwd
print(Path.home())    #User home dir
print(my_path.read_text()) #Returns absolute path

#Ints
#Creates if doesn't exist and writes (not appends!). Only files
my_path.write_text("cibi cibi")

#Opening Path objects!
with my_path.open("w", encoding="utf-8") as f:
    f.write("Meowwwww meow\n")

from pathlib import Path

my_path = Path("/path/to")
my_path = my_path / "file.txt"

#Fields
                       #   dir example | file example
print(my_path.name)    #   Desktop     | file.txt
print(my_path.parent)  #   /path/to    | /path/to
print(my_path.suffix)  #   ''          | .txt
print(my_path.stem)    #   Desktop     | file

print(my_path.parents) #   [Path(/path/to), Path(/path)]
print(my_path.parts)   #   ('/', 'path', 'to', 'file.txt')

print(my_path.anchor)  #   '/' (POSIX), 'C:\\' (Windows)
print(my_path.drive)   #   ''  (POSIX), 'C:'   (Windows)
print(my_path.root)    #   '/'


#String
print(my_path.owner())   # Return user present in path


#Stats object with metadata and stuff
my_path.stat()

# Returns text that is contained in file
print(my_path.read_text())   # 'Hello\n'
print(my_path.read_bytes())  # b'Hello\n'

#Booleans
print(my_path.is_dir())
print(my_path.is_file())
print(my_path.exists())

#Generators of Pathlib objects
print(my_path.iterdir()) #Only on dir! Can iterate over to fill list

#Pathlib objects
print(Path.cwd())     #cwd
print(Path.home())    #User home dir
print(my_path.home()) #Return home path (Path('home/user'))
print(my_path.expanduser()) #Replace ~ with home dir
print(my_path.resolve())    #Print full path

#Ints
#Creates if doesn't exist and writes (not appends!). Only files
my_path.write_text("cibi cibi")
my_path.stat().st_size #Returns file size in bytes

#Opening Path objects!
with my_path.open("w", encoding="utf-8") as f:
    f.write("Meowwwww meow\n")

#Return changed instance
my_path.with_name("textfile.jpg")  # "/path/to/textfile.jpg"
my_path.with_stem("textfile")      # "/path/to/textfile.txt"
my_path.with_suffix(".jpg")        # "/path/to/file.jpg"

my_path.absolute()  # Returns absolute if my_path is relative


#File operations
newpath = my_path.with_stem("stem2")  # Renaming node
my_path.rename(newpath)

newpath = Path('new/path') / my_path.name
my_path.replace(newpath)
           # Renames or moves the file, replacing the destination
           # if it already exists (subject to OS restrictions,
           # e.g., replacing a non-empty directory).

my_path.chmod() # For files and dirs!
                # 777 Read, write, execute for everyone
                # 444 Read-only for everyone
                # 755 Owner: rwx, Group: rx, Others: rx
                # 700 Owner: rwx only
                # 644 Owner: rw, Group: r, Others: r
                # 600 Owner: rw only
mode = oct(my_path.stat().st_mode)[-3:] #Check perms

my_path.touch() #Creates file
                #mode=777        perms
                #exist_ok=True   doesn't raise error if already exists

my_path.mkdir() #Creates directory
                #mode=777        perms
                #parents=True    creates parent (nested) dirs if true
                #exist_ok=True   doesn't raise error if already exists

my_path.write_text("Helloooo")
        # Creates the file if it doesn't exist.
        # Overwrites the file if it already exists.
        # Returns the number of characters written.
my_path.write_bytes(b"\x41\x42\x43")     #ABC
my_path.write_bytes(bytes([41, 42, 43])) #ABC

my_path.unlink(missing_ok=True)  #Remove file or link
Path('path/to/emptydir').rmdir() #Remove empty directory

import shutil
shutil.rmtree(Path("non/empty/dir")) #Remove non empty directory

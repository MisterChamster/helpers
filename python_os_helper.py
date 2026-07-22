import os


os.getcwd()
os.chdir("C:/Users/John/Documents")

os.mkdir("data")
os.makedirs("project/images/icons")

os.rmdir("data")
os.removedirs("project/images/icons")

print(os.listdir())
print(os.listdir("Documents"))

os.rename("old.txt", "new.txt")
os.remove("new.txt")

print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
print(os.path.abspath(path))
print(os.path.basename(path))
print(os.path.dirname(path))

path = os.path.join("folder", "file.txt")

for root, dirs, files in os.walk("."):
    print("Folder:", root)
    print("Subfolders:", dirs)
    print("Files:", files)

print(os.environ)
print(os.getenv("USERNAME"))
print(os.getenv("HOME"))

print(os.getpid())      # Current process ID
print(os.getppid()) 

size = os.path.getsize("example.txt")
print(size)
modified = os.path.getmtime("example.txt")
print(modified)

print(os.name)



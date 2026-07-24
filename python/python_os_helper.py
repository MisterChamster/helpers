import os


# ==========================================================
# ======================== RETURNS =========================
# ==========================================================

os.getcwd()

os.listdir()
os.listdir("Documents")

os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)

os.path.abspath(path)      # Returns the absolute path
os.path.basename(path)     # Returns the file/folder name
os.path.dirname(path)      # Returns the parent directory
os.path.join("folder", "file.txt")  # For the operating system

# Walk through directories
for root, dirs, files in os.walk("."):
    print(root, dirs, files)    # root  - current directory
                                # dirs  - list of subdirectories
                                # files - list of files


os.environ               # All environment variables dict
os.getenv("USERNAME")    # Value of an environment varable
os.getenv("HOME")        # HOME environment variable (Linux/macOS)

os.getpid()    # Current process ID
os.getppid()   # Parent process ID

os.path.getsize("example.txt")    # File size in bytes.
os.path.getmtime("example.txt")   # Last modification time (timestamp)

os.name    # Operating system type
           # 'nt'   - Windows
           # 'posix'- Linux/macOS


# ==========================================================
# ======================== FILE OPS ========================
# ==========================================================

os.chdir("C:/Users/John/Documents")
os.mkdir("data")
os.makedirs("project/images/icons")   # Nested

os.rmdir("data")
os.removedirs("project/images/icons") # Nested

os.rename("old.txt", "new.txt")
os.remove("new.txt")

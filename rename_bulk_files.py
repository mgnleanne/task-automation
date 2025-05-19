import os

# Uses script's current folder as path
folder = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(folder):
    if filename.endswith('.txt'):
        # Modify file name (change _backup string as needed)
        old_path = os.path.join(folder, filename)
        new_name = filename.replace('.txt','_backup.txt')
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)

# Prints out all files in dir to the console
for filename in os.listdir(folder):
        print(filename)

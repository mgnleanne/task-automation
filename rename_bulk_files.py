import os

# Uses script's current folder as path
folder = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(folder):
    if filename.endswith('.txt'):
        # print(f"Found text file: {filename}")
        old_path = os.path.join(folder, filename)
        new_name = filename.replace('.txt','_backup.txt')
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)

for filename in os.listdir(folder):
        print(filename)

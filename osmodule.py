import os

count = 0
for filename in os.listdir():
    _, ext = os.path.splitext(filename)
    new_file_name = f'{count}{ext}'
    os.rename(filename, new_file_name)
    print(f'{count}{ext}')
    count += 1
import os
from PIL import Image


folder_path = './assets/'
items = items = os.listdir(folder_path)

for item in items:
    if os.path.isdir(os.path.join(folder_path, item)):
        print(item)





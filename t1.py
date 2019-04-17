import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("<"+BASE_DIR+">")
image_dir = os.path.join(BASE_DIR, "images")
print("<"+image_dir+">")

for root, dirs,files in os.walk(image_dir):
        for file in dirs:
            print("<"+file+">")

import sys
import os
from PIL import Image

# grab first and second argument
from_dir = sys.argv[1]
to_dir = sys.argv[2]

# check is new/ exists if not create it
if os.path.exists(from_dir):
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
        print(f"{to_dir}/ created")
else:
    print('directory of JPGs doesn\'t exist. please provide valid directory')
    exit()
dir_path = os.path.dirname(os.path.realpath(__file__))
from_dir = os.path.join(dir_path, from_dir)
to_dir = os.path.join(dir_path, to_dir)
# loop through the entire folder
for file in os.listdir(from_dir):
    if file.endswith('.jpg'):
        source_path = os.path.join(from_dir, str(file))
        jpg = Image.open(source_path)
        destination_path = os.path.join(to_dir, str(file)[:-4])
        # convert images to png save to the new folder
        jpg.save(destination_path + ".png", "png")
        print(f"successfuly converted: {str(file)} to {str(file)[:-4] + '.png'}")



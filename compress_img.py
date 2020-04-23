from PIL import Image
import os
import sys
import requests
from io import BytesIO

img_filename = sys.argv[1]
url_flag = int(sys.argv[2])

script_folder=os.path.dirname(os.path.abspath(__file__))+"/"

opt_files=[
  ".gif",
  ".jpg",
  ".jpeg",
  ".jpe",
  ".jfif",
  ".png"
]

filetype=img_filename[img_filename.rfind("."):]
if (filetype.lower() in opt_files):
  if url_flag:
      response = requests.get(img_filename)
      im = Image.open(BytesIO(response.content))
      img_filename = script_folder+img_filename[img_filename.rfind("/")+1:]
  else:
    im = Image.open(img_filename)
  im.save(img_filename,optimize=True)
else:
  print("Filetype {0} not supported".format(filetype))

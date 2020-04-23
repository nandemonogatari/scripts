from PIL import Image
import os
import sys
import requests
from io import BytesIO

img_filename = sys.argv[1]
out_filetype = "."+sys.argv[2]
url_flag = int(sys.argv[3])

script_folder=os.path.dirname(os.path.abspath(__file__))+"/"

filetypes=[
  ".bmp",
  ".dib",
  ".eps",
  ".gif",
  ".ico",
  ".im",
  ".jpg",
  ".jpeg",
  ".jpe",
  ".jfif",
  ".pcx",
  ".png",
  ".ppm",
  ".sgi",
  ".tiff",
  ".webp"
]

opt_files=[
  ".gif",
  ".jpg",
  ".jpeg",
  ".jpe",
  ".jfif",
  ".png"
]

if (out_filetype.lower() in filetypes):
  src_filetype=img_filename[img_filename.rfind("."):]
  if (src_filetype.lower() in filetypes):
    if url_flag:
      response = requests.get(img_filename)
      if (src_filetype.lower()==".png"):
        im = Image.open(BytesIO(response.content)).convert("RGB")
      else:
        im = Image.open(BytesIO(response.content))
      new_p = script_folder+img_filename[img_filename.rfind("/")+1:img_filename.rfind(src_filetype)]+out_filetype
      user_in=0
    else:
      im = Image.open(img_filename)
      user_in=input("Delete old file?(Y/N)\n").lower()
      new_p = img_filename[:img_filename.lower().rfind(src_filetype)]+out_filetype
    if (out_filetype in opt_files):
      im.save(new_p,optimize=True)
    else:
      im.save(new_p,out_filetype[1:])
    if (user_in=="y"):
      os.remove(img_filename)
  else:
    print("Filetype {0} not supported".format(src_filetype))
else:
  print("Wrong output filetype")

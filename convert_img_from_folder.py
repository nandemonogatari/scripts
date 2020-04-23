from PIL import Image
import os
import sys

img_folder = sys.argv[1]
src_filetype = "."+sys.argv[2]
out_filetype = "."+sys.argv[3]

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
  if (src_filetype.lower() in filetypes):
    to_delete=[]
    c=0
    for p in os.listdir(img_folder):
      if (src_filetype in p.lower()):
        im = Image.open(img_folder+p)
        new_p = p[:p.lower().rfind(src_filetype)]+out_filetype
        if (out_filetype in opt_files):
          im.save(img_folder+new_p,optimize=True)
        else:
          im.save(img_folder+new_p,out_filetype[1:])
        to_delete.append(img_folder+p)
        c=c+1
    if (c>0):
      print("{0} files were converted".format(c))
      user_in=input("Delete old files?(Y/N)\n").lower()
      if (user_in=="y"):
        for p in to_delete:
          os.remove(p)
    else:
      print("Found no {0} files in the Folder".format(src_filetype))
  else:
    print("Wrong input filetype")
else:
  print("Wrong output filetype")
import os
import base64
import json
from pathlib import Path

directory = Path('r',os.getcwd()+'\\Input\\')
for filename in os.listdir(directory):
    ThemeName = filename.replace(".png","")
    p = Path('r',os.getcwd()+'\\Input\\'+ThemeName+'.png')
    t = Path('r',os.getcwd()+'\\Templates\\Template.json')
    o = Path('r',os.getcwd()+'\\Output\\'+ThemeName+".json")

    with p.open("rb") as image_file:
        data = str(base64.b64encode(image_file.read()))
        data = data.replace("b'","")
        data = data.replace("'","")
    
        with t.open("r") as template, open(o, "w+") as themejson:
            themejson.write(template.read())
            #o.open is already open as themejson

#edit the created output json o.open


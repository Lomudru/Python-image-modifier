import os
import shutil
from Story1 import *
from Story2 import *
from Story3 import *
from Story4 import *
from Story5 import *
from Story6 import *
from logger import *

def modificationFiles(Files,output):
    TabFile = os.listdir(Files)
    os.mkdir('temps')
    log(f"Dossier temps/ créé.")
    for i in TabFile:
        filePath = BlackAndWhite(f'{Files}/{i}',output,0)
        filePath = Blurred(filePath,output,0)
        filePath = Dilatation(filePath,output,0)
        filePath = WriteText(filePath,output,'teste',20,20,5,0)
        filePath = RotateImage(filePath,45,output,0)
        filePath = Resize(filePath,output,2,2)
        os.rename(f'{filePath}',f'img/Modified_{i}')
    shutil.rmtree('temps')
    log(f"Dossier temps/ suprimé.")

modificationFiles('imageAModif','img')
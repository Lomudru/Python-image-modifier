import os
import shutil
from Story1 import *
from Story2 import *
from Story3 import *
from Story4 import *
from Story5 import *
from Story6 import *
from Story14 import *
from Story16 import *
from Story15 import *
from logger import *
import sys

args = sys.argv[1:]
virgule=False
Caract = ""
Larg = ""
Long = ""
Text = ""
PosX = ""
PosY = ""
Size = ""

def filterFonction(image,output,argsOption,virgule=False,Caract = "",Larg = "",Long = "",Text = "",PosX = "",PosY = "",Size = ""):
    if '--filters' in argsOption:
        FilterIndex=argsOption.index('--filters')
        Filter = argsOption[FilterIndex+1]
        NameImage=image
        for i in range(len(image)):
            if image[i]=='/':
                NameImage=image[i+1:]
        if os.path.exists('temps'):
            shutil.rmtree('temps')
        os.mkdir('temps')
        if 'WT:' in Filter:
            IndexWT = Filter.index('WT:')+3
            Filter+='"'
            while not(virgule):
                if Filter[IndexWT]==',' or Filter[IndexWT]=='"' or Filter[IndexWT]=='&':
                    virgule=True
                else:
                    Text += Filter[IndexWT]
                    if IndexWT<len(Filter)-1:
                        IndexWT += 1
            virgule=False
            IndexWT += 1
            while not(virgule):
                if Filter[IndexWT]==',' or Filter[IndexWT]=='"' or Filter[IndexWT]=='&':
                    virgule=True
                else:
                    PosX += Filter[IndexWT]
                    if IndexWT<len(Filter)-1:
                        IndexWT += 1
            virgule=False
            IndexWT += 1
            while not(virgule):
                if Filter[IndexWT]==',' or Filter[IndexWT]=='"' or Filter[IndexWT]=='&':
                    virgule=True
                else:
                    PosY += Filter[IndexWT]
                    if IndexWT<len(Filter)-1:
                        IndexWT += 1
            virgule=False
            IndexWT += 1
            while not(virgule):
                if Filter[IndexWT]==',' or Filter[IndexWT]=='"' or Filter[IndexWT]=='&':
                    virgule=True
                else:
                    Size += Filter[IndexWT]
                    if IndexWT<len(Filter)-1:
                        IndexWT += 1
            image = WriteText(image,output,str(Text),int(PosX),int(PosY),int(Size),0)
            virgule=False
        if 'Face' in Filter:
            image = FaceDetection(image, output, 0)
        if 'Aqua' in Filter:
            image = Aquarelle(image, output, 0)
        if 'BAW' in Filter:
            image = BlackAndWhite(image,output,0)
        if 'GIF' in Filter:
            image = Make_gif(image,output)
        if 'Blur' in Filter:
            image = Blurred(image,output,0)
        if 'Dila' in Filter:
            image = Dilatation(image,output,0)
        if 'Rotate:' in Filter:
            IndexRotate = Filter.index('Rotate:')+7
            Filter+='"'
            while not(virgule):
                if Filter[IndexRotate]==',' or Filter[IndexRotate]=='"' or Filter[IndexRotate]=='&':
                    virgule=True
                else:
                    Caract += Filter[IndexRotate]
                    if IndexRotate<len(Filter)-1:
                        IndexRotate += 1
            image = RotateImage(image,int(Caract),output,0)
            virgule=False
        if 'Resize:' in Filter:
            IndexResize = Filter.index('Resize:')+7
            Filter+='"'
            while not(virgule):
                if Filter[IndexResize]==',' or Filter[IndexResize]=='"' or Filter[IndexResize]=='&':
                    virgule=True
                else:
                    Larg += Filter[IndexResize]
                    if IndexResize<len(Filter)-1:
                        IndexResize += 1
            virgule=False
            IndexResize += 1
            while not(virgule):
                if Filter[IndexResize]==',' or Filter[IndexResize]=='"' or Filter[IndexResize]=='&':
                    virgule=True
                else:
                    Long += Filter[IndexResize]
                    if IndexResize<len(Filter)-1:
                        IndexResize += 1
            image = Resize(image,output,float(Larg),float(Long),0)
            virgule=False
        
        if 'GIF' in Filter:
            None
        else:
            os.rename(f'{image}',f'img/Modified_{NameImage}')
            log(f"L'image {image} est totalement modifié et sauvegardé dans {output}")
        shutil.rmtree('temps')
        log("Le dossier temps/ est supprimé")

f = open('imageModifie.log', 'w')
f.close()

if '-log' in args:
    f=open("imagemodifie.log", "r")
    print(f.read())

if '--config' in args:
    config_index = args.index('--config')
    configpath = args[config_index+1]
    config = open(configpath,'r')
    temps = config.readlines()
    args2=[]
    for i in temps:
        args2+=i.split()
    max=len(args2)
    for i in range(len(args2)):
        if i<max:
            if args2[i] == "==":
                del args2[i]
                max-=1
    for i in range(len(args2)):
        if '"' in args2[i]:
            args2[i]=args2[i][1:-1]
    for i in range(len(args2)):
        if '--i' in args2[i]:
            imagepath = args2[i+1]
        if '--o' in args2[i]:
            output = args2[i+1]
    for j in range(len(args2)):
        if '--filters' or '--i' or '--o' in args2[j]:
            if '--filters' in args2[j]:
                filterPath = args2[j+1]
                if os.path.isdir(imagepath):
                    TabFile = os.listdir(imagepath)
                    for i in TabFile:
                        ipath=f"{imagepath}/{i}"
                        filterFonction(ipath,output,args2)
                else:
                    filterFonction(imagepath,output,args2)

if '--i' and '--o' in args:
    image_index = args.index('--i')
    imagepath = args[image_index+1]
    ImageFile = args[image_index+1]
    output_index = args.index('--o')
    output = args[output_index+1]
    try:
        GIFFiles = "GIF" in args
        if os.path.isdir(imagepath) and GIFFiles==False:
            TabFile = os.listdir(imagepath)
            for i in TabFile:
                ipath=f"{imagepath}/{i}"
                filterFonction(ipath,output,args)
        else:
            filterFonction(imagepath,output,args)
    except:
        print("Erreur dans les données donnée")

else:
    print('Donner une image avec \'--i\'et un output avec \'--o\'')
    
if '--help' in args:
    print("Aide pour utiliser ce programme :")
    print("Options disponibles :")
    print("--i Path/Of/image.png: Chemin d'accès de l'image en entrée")
    print("--o Path/Of/Output: Chemin d'accès de l'image de sortie")
    print("--filters : Filtres disponibles (ex : \"WT:Texte,PosX,PosY,Size&Blur&Dila\")")
    print("--config Path/Of/config.txt : execute un fichier config")
    print("\"WT:Texte,PosX,PosY,Size\" ecrit du texte sur l'image")
    print("\"BAW\" transforme en noir et blanc")
    print("\"Blur\" Rend l'image flou")
    print("\"GIF\" transforme un dossier en GIF")
    print("\"Dila\" Dilate l'image")
    print("\"Aqua\" Met un filtre aquarelle sur l'image")
    print("\"Face\" Détecte les visages et met un rectangle autour")
    print("\"Resize:longueur,largueur\" Redimentionne l'image")
    print("\"Rotate:degre\" pivote l'image")
    print("-log : Afficher le contenu du fichier 'movie.log'")
    print("Exemple d'utilisation :")
    print("python script.py --i chemin/vers/mon_image.jpg --o chemin/vers/sortie.jpg --filters \"WT:Hello,100,100,20&Blur\"")
    print("Ceci appliquera un filtre de texte ('Hello') avec certaines coordonnées et flou à l'image en entrée.")
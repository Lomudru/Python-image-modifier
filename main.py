import os
import shutil
from Story1 import *
from Story2 import *
from Story3 import *
from Story4 import *
from Story5 import *
from Story6 import *
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

if '-log' in args:
    f=open("movie.log", "r")
    print(f.read())

if '--i' and '--o' in args:
    image_index = args.index('--i')
    image = args[image_index+1]
    ImageFile = args[image_index+1]
    output_index = args.index('--o')
    output = args[output_index+1]
    # try:
    if '--filters' in args:
            FilterIndex=args.index('--filters')
            Filter = args[FilterIndex+1]
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

            if 'BAW' in Filter:
                image = BlackAndWhite(image,output,0)
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
                image = Resize(image,output,int(Larg),int(Long),0)
                virgule=False

            os.rename(f'{image}',f'img/Modified_{ImageFile}')
            shutil.rmtree('temps')
            
    # except:
    #     print("Erreur dans les données donnée")
else:
    print('Donner une image avec \'--i\'et un output avec \'--o\'')



# if '-fv' in args:
#     print(a.get_favorites())

# if '-g' in args:
#     genre_index = args.index('-g')
#     genre = args[genre_index + 1]
#     print(a.get_names_by_genre(genre))

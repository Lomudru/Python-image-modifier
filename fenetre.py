from main import filterFonction
import os
import tkinter as tk
from PIL import ImageTk, Image

# Fonction pour afficher le contenu des champs de texte
def afficher_contenu():
    try:
        # Chargement de l'image
        image_path = ImagesPath.get()
        if os.path.isdir(image_path):
            TabFile = os.listdir(image_path)
            for i in TabFile:
                image = Image.open('dossier.png')  # Mettez le chemin de votre image
                image = image.resize((300, 300))  # Redimensionnez l'image selon vos besoins
                photo = ImageTk.PhotoImage(image)
                imageModif = Image.open('dossier_MODIFIER.png')  # Mettez le chemin de votre image
                imageModif = imageModif.resize((300, 300))  # Redimensionnez l'image selon vos besoins
                photoModif = ImageTk.PhotoImage(imageModif)

                # Affichage de l'image dans un label
                image_label.config(image=photo)
                image_label.image = photo  # Garde une référence à l'image pour éviter la suppression par le garbage collector 
                image_labelModif.config(image=photoModif)
                image_labelModif.image = photoModif  # Garde une référence à l'image pour éviter la suppression par le garbage collector 
                ipath=f"{image_path}/{i}"
                filterFonction(ipath,Output.get(),['--filters',FiltreImg.get()])
        else:
            image = Image.open(image_path)  # Mettez le chemin de votre image
            image = image.resize((300, 300))  # Redimensionnez l'image selon vos besoins
            photo = ImageTk.PhotoImage(image)
            imageModif = Image.open(f'{Output.get()}/Modified_{image_path}')  # Mettez le chemin de votre image
            imageModif = imageModif.resize((300, 300))  # Redimensionnez l'image selon vos besoins
            photoModif = ImageTk.PhotoImage(imageModif)

            # Affichage de l'image dans un label
            image_label.config(image=photo)
            image_label.image = photo  # Garde une référence à l'image pour éviter la suppression par le garbage collector 
            image_labelModif.config(image=photoModif)
            image_labelModif.image = photoModif  # Garde une référence à l'image pour éviter la suppression par le garbage collector 
                
            filterFonction(image_path,Output.get(),['--filters',FiltreImg.get()])
    except Exception as e:
        print(f"Erreur : {e}")  # Affiche l'erreur en cas d'échec du chargement de l'image

    contenu_label.config(text=f"Lien Image: {ImagesPath.get()} \nOutput: {Output.get()} \nFiltre: {FiltreImg.get()}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Affichage d'une image avec des champs de texte")

# Champs de texte pour le ImagesPath, Output et FiltreImg
ImagesPath_label = tk.Label(root, text="Lien Image : ")
ImagesPath_label.pack()
ImagesPath = tk.Entry(root)
ImagesPath.pack()

Output_label = tk.Label(root, text="Output : ")
Output_label.pack()
Output = tk.Entry(root)
Output.pack()

FiltreImg_label = tk.Label(root, text="Filtre : ")
FiltreImg_label.pack()
FiltreImg = tk.Entry(root)
FiltreImg.pack()

# Bouton pour afficher le contenu des champs de texte
afficher_button = tk.Button(root, text="Afficher contenu", command=afficher_contenu)
afficher_button.pack()

# Label pour afficher le contenu des champs de texte
contenu_label = tk.Label(root, text="")
contenu_label.pack()

# Label pour afficher l'image
image_label = tk.Label(root)
image_label.pack()
image_labelModif = tk.Label(root)
image_labelModif.pack()

root.mainloop()

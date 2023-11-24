# Python Image Modifier

## Les différentes librairies nécéssaires
```
pip3 install -r requirements.txt
```

## Les différente modification disponible

- Transformer votre image en noir et blanc
- Rendre votre image floue
- La dilatation de votre image
- Changer l'orientation de votre image
- La redimension de votre image
- Ecrire du texte sur votre image
- Rendre votre image avec un filtre aquarelle
- Détecter des visages sur une image
- Créer un gif a partir d'un dossier

## Les différentes commandes

```
python3 main.py --filters "votreFiltre:donnéeDemanderParLeFirltre&AutreFiltre (ou pas)" --i votre image / dossier d'image --o votre dossier qui vas recevoir le résultat
```
Les nom des différents filtre possible sont :
- BAW
- Blur
- Dila
- Rotate: le degrer de rotation
- Resize: multiplicateur de largeur, multiplicateur de longueur
- Aqua
- Face
- GIF

En cas de besion vous pouver effectuer la commande
```
python3 main.py --help
```

## Vous pouvez accedez a une fenêtre permetant de faire les action citée ci dessus

```
python3 fenetre.py
```

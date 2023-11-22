def log(message):
    with open('imageModifie.log', 'a') as f:
        f.write(message + '\n')
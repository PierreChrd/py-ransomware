# RANSOMWARE PYTHON
``` 
 ____      _    _   _ ____   ___  __  __   ______   __
|  _ \    / \  | \ | / ___| / _ \|  \/  | |  _ \ \ / /
| |_) |  / _ \ |  \| \___ \| | | | |\/| | | |_) \ V / 
|  _ <  / ___ \| |\  |___) | |_| | |  | |_|  __/ | |  
|_| \_\/_/   \_\_| \_|____/ \___/|_|  |_(_)_|    |_|  
```

## Présentation
Script Python (réalisé par Pierre Chaussard) comprend un rançon-logiciel ainsi qu'un serveur python pour récupérer les clés publiques des cibles infectées.

Cet outil ne peut être utilisé qu'à des fins légales. Les utilisateurs assument l'entière responsabilité de toute action effectuée à l'aide de cet outil. L'auteur décline toute responsabilité pour les dommages causés par cet outil. Si ces termes ne vous conviennent pas, n'utilisez pas cet outil.

## Installation

1. Clonez le `repository`.


## Utilisation
1. Lancez le script `ransom.py` à l'aide de la commande `py ransom.py` sur la machine où vous voulez que les fichiers soient chiffrés.

**/!\ ATTENTION /!\\** lors de l'exécution du code, il vous sera demandé un mot de passe (`safeguard password`). 
Le mot de passe par défaut est **`enter`**.
C'est une sécurité intégrée qui empêche le script de chiffrement de se lancer en cas d'un double-clic accidentel par exemple.

Si vous désirez retirer cette protection, il suffit de retirer le code suivant de `ransom.py` :
```py
safeguard = input("Please enter the safeguard password :\n>")
if safeguard != 'enter':
    quit()
```

2. Sur votre machine, lancer `server.py` à l'aide de la commande `py server.py`.

##### Développé par Pierre Chaussard.
# Exécuter ce code dans une console cmd ou terminal intégré de VSCode (cmd)
# Ne fonctionne pas dans PowerShell. Certaines variables d'environnement sont manquantes.

print('Hello, World!')
import os

venv = os.environ.get('VIRTUAL_ENV')
conda_env = os.environ.get('CONDA_DEFAULT_ENV')

python_path = os.environ.get('PYTHONPATH')
print ("Chemin de l'exécutable Python :", python_path)

if venv:
    print("Environnement virtuel (venv/virtualenv) :", os.path.basename(venv))
elif conda_env:
    print("Environnement virtuel (conda) :", conda_env)
else:
    print("Aucun environnement virtuel détecté.")
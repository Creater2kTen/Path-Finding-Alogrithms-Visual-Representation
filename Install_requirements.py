import subprocess

def install(name):
    subprocess.call(['pip', 'install', '--upgrade', 'pip'])
    subprocess.call(['pip', 'install', name])

with open("requirements.txt") as file: 
    data = file.readlines()
    for package in data:
        install(package)
    

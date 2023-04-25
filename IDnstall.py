from subprocess import run
from os import system, path, startfile
from sys import argv

system('title IDbreak Installer V0.1')
run(['pip', 'install', 'requests'])
run(['pip', 'install', 'py-cpuinfo'])
run(['pip', 'install', 'gpustat'])

# get the path of the current script
script_path = path.abspath(argv[0])

# get the path of the file you want to start
file_path = path.join(path.dirname(script_path), "IDbreak.py")

# start the file
startfile(file_path)

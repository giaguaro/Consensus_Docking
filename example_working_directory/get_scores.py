import sys
import pybel 
import yaml

stream = open("config.yaml", 'r')
dictionary = yaml.load(stream, Loader=yaml.FullLoader)



score=str(dictionary.get(str(sys.argv[3])))
f=open(sys.argv[2],'w')
f.write(sys.argv[4]+'\n')
for mol in pybel.readfile("sdf", sys.argv[1]):
    f.write(mol.title+','+mol.data[score]+'\n')

f.close()


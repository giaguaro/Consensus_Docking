import argparse
import pybel as pb

parser =  argparse.ArgumentParser(description = 'Python script to clean the databases from compounds that fail to be docked by one of the software, useful for using mol_rmsd.svl. Remove compound duplicates in the original sdf or from the resulting sdf files as the program does not do that. Currently supports two software only.') 
parser.add_argument('-i1', dest='input_1', help='First input SDF file')
parser.add_argument('-i2', dest='input_2', help='Second input SDF file') 
parser.add_argument('-o1', dest='output_1', help='Name of first output SDF file') 
parser.add_argument('-o2', dest='output_2', help='Name of second output SDF file') 
args = parser.parse_args()

info = open("info.dat", 'w')
mols_1 = list(pb.readfile('sdf', args.input_1))
mols_2 = list(pb.readfile('sdf', args.input_2))
names_1 = list([mol.title for mol in mols_1])     #get names of compounds
names_2 = list([mol.title for mol in mols_2]) 

dkd = list(set(names_1) & set(names_2))    #names of compounds docked by both programs   
n_dkd = list((set(names_1) | set(names_2)) - (set(names_1) & set(names_2)))    #names of compounds not docked by both programs
len_dkd = len(dkd)
len_n_dkd = len(n_dkd)

info.write("compounds in 1: %i\nunique compounds in 1: %i\n\ncompounds in 2: %i\nunique compounds in 2: %i\n\nunique compounds docked by both programs: %i\nunique compounds not docked by both programs: %i\n\n"%(len(names_1), len(set(names_1)), len(names_2), len(set(names_2)), len_dkd, len_n_dkd))
info.close()

names_1 *= 0    #list cleaning to not occupy memory                  
names_2 *= 0

if len_dkd >= len_n_dkd:    #choose most efficient list to go through depending on the size of n_dkd and dkd
    mols_1_dkd = [mol for mol in mols_1 if mol.title not in n_dkd]
    mols_2_dkd = [mol for mol in mols_2 if mol.title not in n_dkd]
else:
    mols_1_dkd = []
    mols_2_dkd = []
    for mol in mols_1:
        if mol.title in dkd:
            mols_1_dkd.append(mol)
#            print "%s %s"%(args.input_1, mol.title)
    for mol in mols_2: 
        if mol.title in dkd:
            mols_2_dkd.append(mol)
#           print "%s %s"%(args.input_2, mol.title

out_1 = pb.Outputfile('sdf',args.output_1,overwrite=True)
out_2 = pb.Outputfile('sdf',args.output_2,overwrite=True)

for i in mols_1_dkd:
    out_1.write(i)

for j in mols_2_dkd:
    out_2.write(j)

out_1.close()
out_2.close()

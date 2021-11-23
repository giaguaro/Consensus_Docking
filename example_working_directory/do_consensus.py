import pandas as pd
import pybel as pb
import sys
import argparse
import re
#import time

parser =  argparse.ArgumentParser(description = 'get consensus docking poses')
parser.add_argument('-rms', dest='file_rms', help='file with rmsd values')
parser.add_argument('-rms_c', dest='rms_cutoff', help='rmsd cutoff')
parser.add_argument('-i1', dest='file_1', help='first file with docking poses')
parser.add_argument('-i2', dest='file_2', help='second file with docking pose')
parser.add_argument('-of', dest='output_folder', help='output_folder')
args = parser.parse_args()

#start = time.time()

rms_cutoff = float(args.rms_cutoff)
mols_1 = list(pb.readfile('sdf', args.file_1))
mols_2 = list(pb.readfile('sdf', args.file_2))

with open(args.file_rms, 'r') as f_in:
    df = pd.DataFrame(re.findall(r'([^\s]+)\s(.*)[\r\t\f\ ](.+)', f_in.read()), columns=['dummy', 'name', 'rmsd'])
print(len(df))    
#sys.exit()
df['rmsd'] = pd.to_numeric(df['rmsd'],downcast='float')
cons_mol = list(df.loc[df['rmsd']<=rms_cutoff,'name'])

print('%i consensus molecules'%len(cons_mol))
#sys.exit()

mols_cons_1 = [mol for mol in mols_1 if mol.title in cons_mol]
mols_cons_2 = [mol for mol in mols_2 if mol.title in cons_mol]

out_1 = pb.Outputfile('sdf','%s/consensus_%s'%(args.output_folder,args.file_1.split('/')[-1]),overwrite=True)
out_2 = pb.Outputfile('sdf','%s/consensus_%s'%(args.output_folder,args.file_2.split('/')[-1]),overwrite=True)

for mol in mols_cons_2:
   mol.data['rmsd'] = df.loc[df['name'] == mol.title, 'rmsd'].iloc[0]
#   print(mol.title)
   out_2.write(mol)

for i in mols_cons_1:
    out_1.write(i)

#print('Execution time %.2f'%(time.time()-start))

out_1.close()
out_2.close()

# Author: Francesco Gentile

import argparse
import pybel as pb

parser =  argparse.ArgumentParser(description = 'Extract molecules based on a range for a particular field (docking scores, ligand efficiency,...') 
parser.add_argument('-in', dest='input_sdf', help='Input SDF file')
parser.add_argument('-o', dest='output_sdf', help='Output SDF file') 
parser.add_argument('-f', dest='field', help='Field used to rank (need to match the field name in the SDF')
parser.add_argument('-min', dest='min_value', help='min value') 
parser.add_argument('-max', dest='max_value', help='max value') 
args = parser.parse_args()

cpds = list(pb.readfile('sdf', '%s'%args.input_sdf))
field = args.field
min = args.min_value
max = args.max_value
cpds_ok = [mol for mol in cpds if (float(mol.data[field])>=float(min)) & (float(mol.data[field])<=float(max))]
print("%i compounds selected"%len(cpds_ok))

output = pb.Outputfile('sdf', '%s'%args.output_sdf, overwrite=True)


for i in cpds_ok:
    output.write(i)

output.close()


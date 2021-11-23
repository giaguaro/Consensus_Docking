import sys
import numpy as np
import pandas as pd
from functools import reduce
import statistics
import collections
import argparse

# required arg
#list_csv=[str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[5]),str(sys.argv[6]),str(sys.argv[7]),str(sys.argv[8]),str(sys.argv[9]),str(sys.argv[10])]

parser = argparse.ArgumentParser()
   
parser.add_argument('-f1', action="store", dest="ab", type=str, help='name of csv file containing RMSD between pair 1')
parser.add_argument('-f2', action="store", dest="ac", type=str, help='name of csv file containing RMSD between pair 2')
parser.add_argument('-f3', action="store", dest="cb", type=str, help='name of csv file containing RMSD between pair 3')
parser.add_argument('-f4', action="store", dest="ad", type=str, help='name of csv file containing RMSD between pair 4')
parser.add_argument('-f5', action="store", dest="cd", type=str, help='name of csv file containing RMSD between pair 5')
parser.add_argument('-f6', action="store", dest="bd", type=str, help='name of csv file containing RMSD between pair 5')
parser.add_argument('-f7', action="store", dest="ae", type=str, help='name of csv file containing RMSD between pair 7')
parser.add_argument('-f8', action="store", dest="ec", type=str, help='name of csv file containing RMSD between pair 8')
parser.add_argument('-f9', action="store", dest="eb", type=str, help='name of csv file containing RMSD between pair 9')
parser.add_argument('-f10', action="store", dest="ed", type=str, help='name of csv file containing RMSD between pair 10')
parser.add_argument('-cons', '--consensus_type', type=int, default=5, help='cross consensus: example - two way (2), three way (3), etc..')
parser.add_argument('-rmsd','--RMSD_cuttoff', action="store", type=float, default=2.0, help='Cuttoff at which RMSD to be considered a consensus')

args = parser.parse_args()

#print(len(vars(args)))
#print(len(sys.argv))
if len(sys.argv) == 7:
    prefix=str(args.ab.split('.')[0])
if len(sys.argv) == 11:
    print('success')
    prefix1=str(args.ab.split('.')[0])
    prefix2=str(args.ac.split('.')[0].split('_')[1])
    prefix=str(prefix1+'_'+prefix2)
if len(sys.argv)==17:
    prefix1=str(args.ab.split('.')[0])
    prefix2=str(args.cd.split('.')[0])
    prefix=str(prefix1+'_'+prefix2)
if len(sys.argv)==25:
    prefix1=str(args.ab.split('.')[0])
    prefix2=str(args.cd.split('.')[0])
    prefix3=str(args.ae.split('.')[0].split('_')[1])
    prefix=str(prefix1+'_'+prefix2+'_'+prefix3)
#Read csv contADning the pADrwise consensused programs which contADn the RMSD values written - outputs into datACrames
try:
    AB = pd.read_csv(f'{args.ab}', sep=' ', names=['dummy', 'name', 'AB'], usecols=['name', 'AB'])
except:
    AB = pd.DataFrame()
try:
    AC = pd.read_csv(f'{args.ac}', sep=' ', names=['dummy', 'name', 'AC'], usecols=['name', 'AC'])
except:
    AC = pd.DataFrame()
try:
    CB = pd.read_csv(f'{args.cb}', sep=' ', names=['dummy', 'name', 'CB'], usecols=['name', 'CB'])
except:
    CB = pd.DataFrame()
try:
    AD = pd.read_csv(f'{args.ad}', sep=' ', names=['dummy', 'name', 'AD'], usecols=['name', 'AD'])
except:
    AD = pd.DataFrame()
try:
    CD = pd.read_csv(f'{args.cd}', sep=' ', names=['dummy', 'name', 'CD'], usecols=['name', 'CD'])
except:
    CD = pd.DataFrame()
try:
    BD = pd.read_csv(f'{args.bd}', sep=' ', names=['dummy', 'name', 'BD'], usecols=['name', 'BD'])
except:
    BD = pd.DataFrame()
try:
    AE = pd.read_csv(f'{args.ae}', sep=' ', names=['dummy', 'name', 'AE'], usecols=['name', 'AE'])
except:
    AE = pd.DataFrame()
try:
    EC = pd.read_csv(f'{args.ec}', sep=' ', names=['dummy', 'name', 'EC'], usecols=['name', 'EC'])
except:
    EC = pd.DataFrame()
try:
    EB = pd.read_csv(f'{args.eb}', sep=' ', names=['dummy', 'name', 'EB'], usecols=['name', 'EB'])
except:
    EB = pd.DataFrame()
try:
    ED = pd.read_csv(f'{args.ed}', sep=' ', names=['dummy', 'name', 'ED'], usecols=['name', 'ED'])
except:
    ED = pd.DataFrame()


columns=['AB', 'AC', 'CB', 'AD', 'CD', 'BD', 'AE', 'CE', 'EB', 'ED']
data_frames_clumns=[]
pre_data_frames=[AC, AB, AD, AE, CB, CD, BD, EC, EB, ED]
data_frames=[i for i in pre_data_frames if len(i)!=0]
print (data_frames)
#Merge dataFrames
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['name'],
                                            how='outer'), data_frames).fillna('')

#df_merged.to_csv('all.csv', index=False)

#DeCDnes the type of consensus evalation to be carried out and the corresponding permutations (taking into account all variations without duplications)
duplets_set=[['AC'],['AB'],['CB'],['AD'],['CD'],['AE'],['CE'],['BD'],['EB'],['ED']]
triplets_set=[['AC','AB','CB'],['AC','AD','CD'],['AC','AE','CE'],['AB','AD','BD'],
             ['AB','AE','EB'],['AD','AE','ED'],['CB','CE','EB'],['CB','CD','BD'],
             ['CD','CE','ED'],['BD','EB','ED']]
quadruplets_set=[['AC','AB','CB','AD','CD','BD'],['AC','AB','CB','AE','CE','EB'],
                ['CB','CD','BD','ED','CE','EB'],['AB','AD','AE','BD','EB','ED'],
                ['AC','AD','AE','CD','CE','ED']]
quintet_set=[['AC','AB','AD','AE','CB','CD','BD','CE','EB','ED']]

df_merged_list=list(df_merged.columns.values)

duplets_set=[[pair for pair in groups if pair in df_merged_list] for groups in duplets_set]
triplets_set=[[pair for pair in groups if pair in df_merged_list] for groups in triplets_set]
quadruplets_set=[[pair for pair in groups if pair in df_merged_list] for groups in quadruplets_set]
quintet_set=[[pair for pair in groups if pair in df_merged_list] for groups in quintet_set]

#loops over all the merged datACrame and retADns the Mols with correspondng RMSD less than/equal to threshold set by user
def thresh_RMSD_across_consensus(type_set, thresh):
    thresh_lists=[]
    
    for index, row in df_merged.iterrows():
        molecule_name=str(row['name'])
        for groups_set in type_set:
            pairs_rmsd=[row[str(pairs)] for pairs in groups_set]
            pairs_rmsd_nonempty_values = [float(x) for x in pairs_rmsd if x]
            
            if pairs_rmsd_nonempty_values:
                pairs_thresh_rmsd=[i for i in pairs_rmsd_nonempty_values if i<=thresh]
                if len(pairs_thresh_rmsd)==len(type_set[0]):
                    thresh_lists.append(molecule_name)
                    break
                else:
                    continue
            else:
                continue
    return thresh_lists


if args.consensus_type==2:
    type_set=duplets_set
elif args.consensus_type==3:
    type_set=triplets_set
elif args.consensus_type==4:
    type_set=quadruplets_set
elif args.consensus_type==5:
    type_set=quintet_set
else:
    type_set=quintet_set

cons_list=thresh_RMSD_across_consensus(type_set, args.RMSD_cuttoff)
df_consensus=pd.DataFrame()
df_consensus['name']=cons_list

df_consensus.to_csv(f'{prefix}_consensus_mol_names.csv', index=False)
print(df_consensus)

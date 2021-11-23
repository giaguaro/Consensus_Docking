import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import pearsonr
import os, sys
import glob
from functools import reduce

prefix=str('_'.join(str(sys.argv[1]).split('.')[0].split('_')[:-3]))

scores=[pd.read_csv(scorefile) for scorefile in glob.glob('./*_scores.txt')]
scores.append(pd.read_csv(f'{str(sys.argv[1])}'))
data = reduce(lambda  left,right: pd.merge(left,right,on=['name'],
                                            how='outer'), scores).fillna('')

len_columns=range(len(list(data.columns)))

cmap = 'coolwarm'
cmap_r = 'coolwarm_r'

r = {"ticks":[0.00,0.50,1.00]}
r_corr = {"ticks":[-1.00,0.00,1.00]}

vmin_h = 0
vmax_h = 1

vmin_s = -1
vmax_s = 1

std = 1.0
column_names=['name']
for i in range(1,len(list(data.columns)) ):
    column_names.append(f'dock{i}')
data.columns =column_names

for l in range(1,len(list(data.columns))):
    data=data.dropna(subset=[f'dock{l}'])
    data[f'dock{l}'] = pd.to_numeric(data[f'dock{l}'])
    data_filtered = data.copy()
    data_filtered[f'dock{l}_st'] = (data_filtered[f'dock{l}'] - data_filtered[f'dock{l}'].mean())/data_filtered[f'dock{l}'].std()
    #To plot, use the percentile ranks of each column (based on scores) as color range
    data_filtered[f'dock{l}_r'] = data_filtered[f'dock{l}_st'].rank(pct=True, ascending=False)

st_columns=list(data_filtered.filter(regex='_st$',axis=1).columns)  
#But overall ranks are assigned based on average standardized scores
data_filtered['avg_st_score'] = data_filtered[st_columns].mean(axis=1)
data_filtered = data_filtered.reset_index(drop=True)

data_filtered['rank'] = data_filtered.index
data_filtered = data_filtered.set_index('rank')

r_columns=list(data_filtered.filter(regex='_r$',axis=1).columns)  
set_plot = data_filtered[r_columns]

g = sns.heatmap(set_plot, vmin=vmin_h, vmax=vmax_h, cmap=cmap_r)
g.set_xticklabels(g.get_xticklabels(), rotation = 90)

plt.savefig(f'{prefix}_docking_consensus_plot.png', bbox_inches='tight', dpi=600)

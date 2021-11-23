#!/bin/bash
#SBATCH --cpus-per-task=60
#SBATCH --partition=normal
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=consensus

source ~/.bashrc

#make sure the sdfs are contained within directories that bears the name of the docking program

f1=${1%/}"/"*
f2=${2%/}"/"*
f3=${3%/}"/"*
f4=${4%/}"/"*
f5=${5%/}"/"*

sf1=$(cd ${1%/} && ls)
sf2=$(cd ${2%/} && ls)
sf3=$(cd ${3%/} && ls)
sf4=$(cd ${4%/} && ls)
sf5=$(cd ${5%/} && ls)

mkdir consensus_results/

if [ $# -eq 0 ]
  then
    echo "No arguments supplied, please supply name of directories (which are named after the docking program used) that contains the sdf of docked molecules"
fi

if [ $# -eq 1 ]
  then
    echo "Not all arguments supplied - please supply at least two names of directories (which are named after the docking program used) that contains the sdf of docked molecules"
fi

if [ $# -eq 2 ]
  then
    bash consensus.sh $f1 $f2 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${2%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf2 ${1%/}_${2%/}_${2%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${2%/}.csv
    python get_scores.py $f1 ${1%/}_scores.txt docking_software1 ${1%/}_scores.txt
    python get_scores.py $f2 ${2%/}_scores.txt docking_software2 ${2%/}_scores.txt
    echo "done ${1%/} and ${2%/}"
fi

if [ $# -eq 3 ]
  then
    bash consensus.sh $f1 $f2 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${2%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf2 ${1%/}_${2%/}_${2%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${2%/}.csv
    echo "done ${1%/} and ${2%/}"

    bash consensus.sh $f1 $f3 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${3%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf3 ${1%/}_${3%/}_${3%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${3%/}.csv
    echo "done ${1%/} and ${3%/}"

    bash consensus.sh $f3 $f2 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf3 ${3%/}_${2%/}_${3%/}_poses.sdf
    cp consensus_results/consensus_common_$sf2 ${3%/}_${2%/}_${2%/}_poses.sdf
    cp consensus_files/rmsd.csv ${3%/}_${2%/}.csv
    echo "done ${3%/} and ${2%/}"
    python get_scores.py $f1 ${1%/}_scores.txt docking_software1 ${1%/}_scores.txt
    python get_scores.py $f2 ${2%/}_scores.txt docking_software2 ${2%/}_scores.txt
    python get_scores.py $f3 ${3%/}_scores.txt docking_software3 ${3%/}_scores.txt
    
    touch ${1%/}_${2%/}_${3%/}.csv
fi

if [ $# -eq 4 ]
  then
    bash consensus.sh $f1 $f2 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${2%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf2 ${1%/}_${2%/}_${2%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${2%/}.csv
    echo "done ${1%/} and ${2%/}"

    bash consensus.sh $f1 $f3 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${3%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf3 ${1%/}_${3%/}_${3%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${3%/}.csv
    echo "done ${1%/} and ${3%/}"

    bash consensus.sh $f3 $f2 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf3 ${3%/}_${2%/}_${3%/}_poses.sdf
    cp consensus_results/consensus_common_$sf2 ${3%/}_${2%/}_${2%/}_poses.sdf
    cp consensus_files/rmsd.csv ${3%/}_${2%/}.csv
    echo "done ${3%/} and ${2%/}"

    bash consensus.sh $f1 $f4 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${4%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf4 ${1%/}_${4%/}_${4%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${4%/}.csv
    echo "done ${1%/} and ${4%/}"

    bash consensus.sh $f3 $f4 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf3 ${3%/}_${4%/}_${3%/}_poses.sdf
    cp consensus_results/consensus_common_$sf4 ${3%/}_${4%/}_${4%/}_poses.sdf
    cp consensus_files/rmsd.csv ${3%/}_${4%/}.csv
    echo "done ${3%/} and ${4%/}"

    bash consensus.sh $f2 $f4 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf2 ${2%/}_${4%/}_${2%/}_poses.sdf
    cp consensus_results/consensus_common_$sf4 ${2%/}_${4%/}_${4%/}_poses.sdf
    cp consensus_files/rmsd.csv ${2%/}_${4%/}.csv
    echo "done ${2%/} and ${4%/}"
    python get_scores.py $f1 ${1%/}_scores.txt docking_software1 ${1%/}_scores.txt
    python get_scores.py $f2 ${2%/}_scores.txt docking_software2 ${2%/}_scores.txt
    python get_scores.py $f3 ${3%/}_scores.txt docking_software3 ${3%/}_scores.txt
    python get_scores.py $f4 ${4%/}_scores.txt docking_software4 ${4%/}_scores.txt


   touch ${1%/}_${2%/}_${3%/}_${4%/}.csv
fi

if [ $# -eq 5 ]
  then
    bash consensus.sh $f1 $f2 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${2%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf2 ${1%/}_${2%/}_${2%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${2%/}.csv
    echo "done ${1%/} and ${2%/}"

    bash consensus.sh $f1 $f3 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${3%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf3 ${1%/}_${3%/}_${3%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${3%/}.csv
    echo "done ${1%/} and ${3%/}"

    bash consensus.sh $f3 $f2 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf3 ${3%/}_${2%/}_${3%/}_poses.sdf
    cp consensus_results/consensus_common_$sf2 ${3%/}_${2%/}_${2%/}_poses.sdf
    cp consensus_files/rmsd.csv ${3%/}_${2%/}.csv
    echo "done ${3%/} and ${2%/}"

    bash consensus.sh $f1 $f4 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${4%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf4 ${1%/}_${4%/}_${4%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${4%/}.csv
    echo "done ${1%/} and ${4%/}"

    bash consensus.sh $f3 $f4 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf3 ${3%/}_${4%/}_${3%/}_poses.sdf
    cp consensus_results/consensus_common_$sf4 ${3%/}_${4%/}_${4%/}_poses.sdf
    cp consensus_files/rmsd.csv ${3%/}_${4%/}.csv
    echo "done ${3%/} and ${4%/}"

    bash consensus.sh $f2 $f4 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf2 ${2%/}_${4%/}_${2%/}_poses.sdf
    cp consensus_results/consensus_common_$sf4 ${2%/}_${4%/}_${4%/}_poses.sdf
    cp consensus_files/rmsd.csv ${2%/}_${4%/}.csv
    echo "done ${2%/} and ${4%/}"

    bash consensus.sh $f1 $f5 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf1 ${1%/}_${5%/}_${1%/}_poses.sdf
    cp consensus_results/consensus_common_$sf5 ${1%/}_${5%/}_${5%/}_poses.sdf
    cp consensus_files/rmsd.csv ${1%/}_${5%/}.csv
    echo "done ${5%/} and ${1%/}"

    bash consensus.sh $f5 $f3 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf5 ${5%/}_${3%/}_${5%/}_poses.sdf
    cp consensus_results/consensus_common_$sf3 ${5%/}_${3%/}_${3%/}_poses.sdf
    cp consensus_files/rmsd.csv ${5%/}_${3%/}.csv
    echo "done ${5%/} and ${3%/}"

    bash consensus.sh $f5 $f2 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf5 ${5%/}_${2%/}_${5%/}_poses.sdf
    cp consensus_results/consensus_common_$sf2 ${5%/}_${2%/}_${2%/}_poses.sdf
    cp consensus_files/rmsd.csv ${5%/}_${2%/}.csv
    echo "done ${5%/} and ${2%/}"

    bash consensus.sh $f5 $f4 consensus_results/ 2.0
    sleep 5
    cp consensus_results/consensus_common_$sf5 ${5%/}_${4%/}_${5%/}_poses.sdf
    cp consensus_results/consensus_common_$sf4 ${5%/}_${4%/}_${4%/}_poses.sdf
    cp consensus_files/rmsd.csv ${5%/}_${4%/}.csv
    echo "done ${5%/} and ${4%/}"

    python get_scores.py $f1 ${1%/}_scores.txt docking_software1 ${1%/}_scores.txt
    python get_scores.py $f2 ${2%/}_scores.txt docking_software2 ${2%/}_scores.txt
    python get_scores.py $f3 ${3%/}_scores.txt docking_software3 ${3%/}_scores.txt
    python get_scores.py $f4 ${4%/}_scores.txt docking_software4 ${4%/}_scores.txt
    python get_scores.py $f5 ${5%/}_scores.txt docking_software5 ${5%/}_scores.txt

    touch ${1%/}_${2%/}_${3%/}_${4%/}_${5%/}.csv
fi
for i in *scores*txt; do sed -i '1s/^/name,/' $i; done
#rm *__* *_.* _*


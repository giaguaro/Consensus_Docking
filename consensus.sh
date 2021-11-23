
input_1_all=$1
input_2_all=$2
output_f=$3
cutoff=$4

#HELP

if [ "$1" == "-h" ]; then
	echo "

EVALUATE CONSENSUS: given two sdf docking files and a rmsd cutoff, returns docking poses of common compounds with a rmsd less or equal to the cutoff. Run one folder above where the docking results are. Requires pybel python package. Usage:

	    bash `basename $0` folder_1/sdf_1 folder_2/sdf_2 output_folder cutoff
	    
This will create two consensus sdf files in output_folder, with names linked to the original input files. RMSDs are stored in a 'rmsd' field in the second consensus file. Previous sdf files with same names are overwritten so be careful about defining names.

"
        exit 0

fi

if [ "$1" != "-h" ] && [ $# -lt 4 ]; then
	echo "Not all the arguments were supplied; type 'bash `basename $0` -h' for help"

	exit 0

fi	    

mkdir -p consensus_files
mkdir -p $output_f
rm consensus_files/rmsd.csv

start=`date +%s`

fold_1="$(cut -d'/' -f1<<<"$input_1_all")"
input_1="$(cut -d'/' -f2<<<"$input_1_all")"
fold_2="$(cut -d'/' -f1<<<"$input_2_all")"
input_2="$(cut -d'/' -f2<<<"$input_2_all")"

obabel -isdf $fold_1/$input_1 -O consensus_files/unique_$input_1 --unique title
obabel -isdf $fold_2/$input_2 -O consensus_files/unique_$input_2 --unique title

python sdf_overlap.py -i1 consensus_files/unique_$input_1 -i2 consensus_files/unique_$input_2 -o1 consensus_files/common_$input_1 -o2 consensus_files/common_$input_2

obabel -isdf consensus_files/common_$input_1 -O consensus_files/sorted_$input_1 --sort title
obabel -isdf consensus_files/common_$input_2 -O consensus_files/sorted_$input_2 --sort title

obrms consensus_files/sorted_$input_1 consensus_files/sorted_$input_2>>consensus_files/rmsd.csv

python do_consensus.py -rms consensus_files/rmsd.csv -rms_c $cutoff -i1 consensus_files/common_$input_1 -i2 consensus_files/common_$input_2 -of $output_f

end=`date +%s`
runtime=$((end-start))
echo $runtime

Automated pipeline for running consensus scoring between docking programs. Highest number of programs supported is five.

Inputs required: 1) SDF format file from the docking program (put that into a directory named after the dockign program - one word) within the working directory. 2) All utilities that come with this package.

Example syntax for running Snakefile for five docking programs consensus of poses scoring (RMSD of 2 Angstroms):

snakemake --cores 1 --snakefile Snakefile autodock_glide_fred_icm_vina_docking_consensus_plot.png --config number='five'

-where Autodock, Glide, Fred, Icm, and Vina are docking programs.

Another example for three docking programs:

snakemake --cores 1 --snakefile Snakefile autodock_glide_fred_docking_consensus_plot.png --config number='three'

* As you can see the '--config number' has to be changed accordingly 


You will Need numerous Dependencies for executing this code.. most importantly:
Openbabel 2.4.1 and its pybel wrapper
-> conda install -c conda-forge/label/cf202003 openbabel=2.4.1

.....................................................................................................................

Prior to it all, Make sure to install SnakeMake into your conda environment (i.e. activate it first before installing).
Instructions on installing SnakeMake can be found here:
https://snakemake.readthedocs.io/en/stable/getting_started/installation.html

NOTE: change 'base' to your conda enviroment name (in the installation procedure).

ALSO, you need to change the config.yaml file to contain the score field name in the sdf file containing the docked poses and scores.
.....................................................................................................................


Some variables can be introduced here. Most relevant are:

Consensus type (i.e. two way consensus, three way way consensus, four way consensus, etc... say for an input of five docking programs)- perhaps you want the consensus between only at least two programs. 

-> This can be changed by setting the -cons flag in the Snakefile to the desired number (highest is 5).

Consensus RMSD (how much agreement between two poses between the two corresponding docking programs)

-> This can be changed by setting the -rmsd flag in the Snakefile to the desired float.

Otherwise, the numbers are default: three way consensus and 2.0 Angstrom RMSD pose agreement.

docking_original.png

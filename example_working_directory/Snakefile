
#ruleorder: pre_consensus_2>pre_consensus_3>pre_consensus_4>pre_consensus_5 
if config['number'] == 'five':
    rule plot_consensus_5:
        input:
            "{file1}_{file2}_{file3}_{file4}_{file5}_consensus_mol_names.csv"
        output:
            "{file1}_{file2}_{file3}_{file4}_{file5}_docking_consensus_plot.png"
        shell:
            "python plot_consensus.py {input}"

    rule consensus_5:
        input:
            "{file1}_{file2}_{file3}_{file4}_{file5}.csv"
        output:
            "{file1}_{file2}_{file3}_{file4}_{file5}_consensus_mol_names.csv"
        shell:
            "python consensus_typing.py -f1 {wildcards.file1}_{wildcards.file2}.csv -f2 {wildcards.file1}_{wildcards.file3}.csv -f3 {wildcards.file3}_{wildcards.file2}.csv -f4 {wildcards.file1}_{wildcards.file4}.csv -f5 {wildcards.file3}_{wildcards.file4}.csv -f6 {wildcards.file2}_{wildcards.file4}.csv -f7 {wildcards.file1}_{wildcards.file5}.csv -f8 {wildcards.file5}_{wildcards.file3} -f9 {wildcards.file5}_{wildcards.file2}.csv -f10 {wildcards.file5}_{wildcards.file4}.csv -cons 3 -rmsd 2.0"

    rule pre_consensus_5:
        input:
            "{file1}",
            "{file2}",
            "{file3}",
            "{file4}",
            "{file5}"
        output:
            "{file1}_{file2}_{file3}_{file4}_{file5}.csv"
        shell:
            "set +o pipefail;bash consensus_script.sh {input}"

elif config['number'] == 'four':
    rule plot_consensus_4:
        input:
            "{file1}_{file2}_{file3}_{file4}_consensus_mol_names.csv"
        output:
            "{file1}_{file2}_{file3}_{file4}_docking_consensus_plot.png"
        shell:
            "python plot_consensus.py {input}"

    rule consensus_4:
        input:
            "{file1}_{file2}_{file3}_{file4}.csv"
        output:
            "{file1}_{file2}_{file3}_{file4}_consensus_mol_names.csv"
        shell:
            "python consensus_typing.py -f1 {wildcards.file1}_{wildcards.file2}.csv -f2 {wildcards.file1}_{wildcards.file3}.csv -f3 {wildcards.file3}_{wildcards.file2}.csv -f4 {wildcards.file1}_{wildcards.file4}.csv -f5 {wildcards.file3}_{wildcards.file4}.csv -f6 {wildcards.file2}_{wildcards.file4}.csv -cons 3 -rmsd 2.0"

    rule pre_consensus_4:
        input:
            "{file1}",
            "{file2}",
            "{file3}",
            "{file4}"
        output:
            "{file1}_{file2}_{file3}_{file4}.csv"

        shell:
            "set +o pipefail;bash consensus_script.sh {input}"

elif config['number'] == 'three':
    rule plot_consensus_3:
        input:
            "{file1}_{file2}_{file3}_consensus_mol_names.csv"
        output:
            "{file1}_{file2}_{file3}_docking_consensus_plot.png"
        shell:
            "python plot_consensus.py {input}"

    rule consensus_3:
        input:
            "{file1}_{file2}_{file3}.csv"

        output:
            "{file1}_{file2}_{file3}_consensus_mol_names.csv"
        shell:
            "python consensus_typing.py -f1 {wildcards.file1}_{wildcards.file2}.csv -f2 {wildcards.file1}_{wildcards.file3}.csv -f3 {wildcards.file3}_{wildcards.file2}.csv -cons 3 -rmsd 2.0"

    rule pre_consensus_3:
        input:
            "{file1}",
            "{file2}",
            "{file3}"
        output:
            "{file1}_{file2}_{file3}.csv"

        shell:
            "set +o pipefail;bash consensus_script.sh {input}"

elif config['number'] == 'two':            
    rule plot_consensus_2:
        input:
            "{file1}_{file2}_consensus_mol_names.csv"
        output:
            "{file1}_{file2}_docking_consensus_plot.png"
        shell:
            "python plot_consensus.py {input}"

    rule consensus_2:
        input:
            "{file1}_{file2}.csv"

        output:
            "{file1}_{file2}_consensus_mol_names.csv"
        shell:
            "python consensus_typing.py -f1 {input} -cons config['way'] -rmsd 2.0"

    rule pre_consensus_2:
        input:
            "{file1}",
            "{file2}",
        output:
            "{file1}_{file2}.csv"
        shell:
            "set +o pipefail;bash consensus_script.sh {input}"



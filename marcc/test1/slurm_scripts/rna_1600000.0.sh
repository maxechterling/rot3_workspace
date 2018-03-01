#!/bin/bash -l

#SBATCH
#SBATCH --job-name=rna_1600000.0
#SBATCH -o myjob.%j.out
#SBATCH -e myerr.%j.err
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --time=10:00:00
#SBATCH --mem=5G

perl ../NFsim_v1.10//BNG/BNG2.pl test1/bngl_files/rna_1600000.0.bngl > results/rna_1600000.0.out

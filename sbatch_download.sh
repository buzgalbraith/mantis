#!/bin/bash
#SBATCH -J download_nf_data                           # Job name
#SBATCH -N 1                                # Number of nodes
#SBATCH -n 4                                # Number of tasks
#SBATCH --mem=32G  
#SBATCH -o ./outputs/%x-%j.out
#SBATCH -e ./outputs/%x-%j.err
#SBATCH --time=1-12:00:00 # 1 day 12 hours zero minutes

## run code etc
source /scratch/w.galbraith/CS7800_group_4/mantis/.venv/bin/activate
python ./scripts/pull_data_from_synapse.py

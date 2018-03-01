#!/usr/bin/env python

"""
Script for submitting batches of slurm scripts for parameter sweeps of the Gag
assembly model using NFsim

Usage:
    template.bngl is the file containing base model parameters for running NFsim, 
    outdir is the path to the output directory that will contain the generated slurm
    scripts and simulation outputs. NFsim is the path to the BNG2.pl file. the parameters 
    to sweep through must be hard coded in the variable 'sweep_dic' with the name of the 
    parameter to change as the key and the values to iterate through as values.
        $ ./batch_slurm.py template.bngl NFsim outdir
"""

import sys
import os

## Can do a sweep with a maximum of two different parameters
#sweep_dic = {'rna': [1, 100, 1000, 10000], 'psi': [11, 12, 13]}
sweep_dic = {'rna': [1.6e6]}

def combo_gen(sweep_dic):
    """Create all combinations of sweep parameters if multiple values are being changed
    """
    par = sweep_dic.values()
    if len(sweep_dic.keys()) == 2:
        return [[x,y] for x in par[0] for y in par[1]]
    else:
        return [[x] for x in sweep_dic.values()[0]]
    
def write_bngls(comboes, sweep_dic):
    """Writes bngl files for each parameter combination desired
    Files are written into outdir/bngl_files/ with filename parA_valA_parB_valB.bngl"""
    bnglFiles = []
    os.system('mkdir %s/bngl_files' % (sys.argv[3]))
    for combo in comboes:
        if len(combo) == 2:
            outName = '%s_%s_%s_%s.bngl' % (sweep_dic.keys()[0], combo[0],\
                                            sweep_dic.keys()[1], combo[1])
        else:
            outName = '%s_%s.bngl' % (sweep_dic.keys()[0], combo[0])
        bnglFiles.append(outName)
        template = open(sys.argv[1], 'r')
        outfile = open('%s/bngl_files/%s' % (sys.argv[3], outName), 'w')
        if len(combo) == 2:
            for line in template:
                if '\t%s ' % (sweep_dic.keys()[0]) in line:
                    outfile.write('\t%s\t%s\n' % (sweep_dic.keys()[0], combo[0]))
                elif '\t%s ' % (sweep_dic.keys()[1]) in line:
                    outfile.write('\t%s\t%s\n' % (sweep_dic.keys()[1], combo[1]))
                else:
                    outfile.write(line)
        else:
            for line in template:
                if '\t%s ' % (sweep_dic.keys()[0]) in line:
                    outfile.write('\t%s\t%s\n' % (sweep_dic.keys()[0], combo[0]))
                else:
                    outfile.write(line)
        template.close()
        outfile.close()
    return bnglFiles
    
def write_script(fname, task, outdir, ntasks=1, name='', partition='shared', \
                 options=[], modules=[], time="4:0:0"):
    """Writes a slurm script to run """
    output = open(fname, 'w')
    print >> output, "#!/bin/bash -l"
    print >> output, ""
    print >> output, "#SBATCH"
    print >> output, "#SBATCH --job-name=%s" % name
    print >> output, "#SBATCH -o myjob.%j.out"
    print >> output, "#SBATCH -e myerr.%j.err"
    print >> output, "#SBATCH --partition=shared"
    print >> output, "#SBATCH --nodes=1"
    print >> output, "#SBATCH --time=10:00:00"
    print >> output, "#SBATCH --mem=5G"
    print >> output, ""
    print >> output, task
    output.close
    
def batch_scripts(bnglFiles, outdir):
    os.system('mkdir %s/slurm_scripts' % (outdir))
    os.system('mkdir %s/error' % (outdir))
    os.system('mkdir %s/results' % (outdir))
    for bngl in bnglFiles:
        fname = '%s/slurm_scripts/%ssh' % (outdir, bngl.rstrip('bngl'))
        task = 'perl %sBNG/BNG2.pl %s/bngl_files/%s > %s/results/%s' % \
                    (sys.argv[2], outdir, bngl, outdir, bngl.rstrip('.bngl') + '.out')
        write_script(fname, task, outdir, name=bngl.rstrip('.bngl'))
        os.system('sbatch %s' % (fname))
        #print 'sbatch %s' % (fname)
        
def main(sweep_dic):
    template, outdir = sys.argv[1], sys.argv[3]
    os.system('mkdir %s' % (outdir))
    comboes = combo_gen(sweep_dic)
    bnglFiles = write_bngls(comboes, sweep_dic)
    batch_scripts(bnglFiles, outdir)

if __name__ == "__main__":
    main(sweep_dic)
    
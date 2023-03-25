#!/home/jinho93/mambaforge/bin/python
import sys, os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("core", default = 24, type = int, \
                          help = "data-file to process")
parser.add_argument("name", default = "test", type = str, \
                          help = "data-file to process")
parser.add_argument("-s", default = "std", type = str, \
                          help = "data-file to process")
parser.add_argument("-v", default = "std", type = str, \
                          help = "data-file to process")

core = parser.parse_args().core
name = parser.parse_args().name
system = parser.parse_args().s
ver = parser.parse_args().v

lines = ["#$ " + r + '\n' for r in [f'-pe mpi_{core} {core}', f'-N {name}', '-cwd', '-q 6248.q', '-V', '-S /bin/bash']]
lines.append('#$ -o $JOB_NAME.o$JOB_ID\n')
lines.append('#$ -j Y\n')

if ver == 'oop' or ver == 'neb':
    lines.append(f'''mpirun -machinefile $TMPDIR/machines -n $NSLOTS /opt/vasp/vasp.6.4.0/bin/vasp_{system} > report.vasp
touch complete
pwd >> /home/jinho93/.qhistory
''')
else:
    lines.append(f'''mpirun -machinefile $TMPDIR/machines -n $NSLOTS /opt/vasp/vasp.6.4.0/bin/vasp_{system} > report.vasp
touch complete
pwd >> /home/jinho93/.qhistory
''')


with open('queue_script', 'w') as f:
    f.writelines(lines)

os.system('qsub queue_script')

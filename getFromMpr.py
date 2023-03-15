#!/home/jinho93/mambaforge/envs/phon/bin/python
from pymatgen.core.structure import Structure
from mp_api.client import MPRester
import sys
with MPRester("s1uN13V7Ia4ID3gGER0m38fSi8IuvnMq") as mpr:
    s: Structure = mpr.get_structure_by_material_id(sys.argv[1], conventional_unit_cell=True)
    s.to('POSCAR', 'POSCAR')

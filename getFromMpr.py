#!/home/jinho93/mambaforge/envs/phon/bin/python
from pymatgen.core.structure import Structure
from mp_api.client import MPRester
import argparse
with MPRester("s1uN13V7Ia4ID3gGER0m38fSi8IuvnMq") as mpr:
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', help='Example) save', default='', dest='mp')
    parser.add_argument('-f', nargs='+', help='formula ex Si-O', default='', dest='formula')
    parser.add_argument(nargs='*' ,help='chemsys Si O', dest='chemsys', default=[])

    mp = parser.parse_args().mp
    chemsys = parser.parse_args().chemsys
    formula = parser.parse_args().formula
    if mp:
        s: Structure = mpr.get_structure_by_material_id(mp, conventional_unit_cell=True)
        s.to('POSCAR', 'POSCAR')
    elif chemsys:
        docs = mpr.summary.search(chemsys="-".join(chemsys), 
                                  fields=["structure"])
        for n, doc in enumerate(docs):
            doc.structure.to(f'POSCAR-{n}', 'POSCAR')

    elif formula:
        docs = mpr.summary.search(elements=formula,
                                  fields=["structure"])
        for n, doc in enumerate(docs):
            doc.structure.to(f'POSCAR-{n}', 'POSCAR')

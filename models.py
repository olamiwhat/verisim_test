import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def saveData(name, iupac_name, canonical_smiles, molecular_formula, cas_number,  molecular_weight, drug_class, superclass, rotable_bond_count, complexity):
    con = sql.connect(path.join(ROOT, drugs.db))
    cur = con.cursor()
    cur.execute('insert into drugs (name, iupac_name, canonical_smiles, molecular_formula, cas_number,  molecular_weight, drug_class, superclass, rotable_bond_count, complexity) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)' (name, iupac_name, canonical_smiles, molecular_formula, cas_number,  molecular_weight, drug_class, superclass, rotable_bond_count, complexity))
    con.commit()
    con.close()


def getDrugs():
    con = sql.connect(path.join(ROOT, 'drugs.db'))
    cur = con.cursor()
    cur.execute('select * from drugs')
    drugs = cur.fetchall()
    return drugs
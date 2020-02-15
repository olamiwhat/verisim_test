drop table if exists drugs;
	create table drugs (
		id integer not null,
		name varchar (20) not null,
		iupac_name char (25),
		canonical_smiles char (20),
		molecular_formular varchar (20),
		cas_number varchar (20),
		molecular_weight varchar (20),
		drug_class char,
		superclass char,
		rotable_bond_count char,
		complexity char,
		primary key (id)
);
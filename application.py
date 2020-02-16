from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from models import saveData, getDrugs


app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        pass


    if request.method == 'POST':
        name = request.form.get('name')
        iupac_name = request.form.get('iupac_name')
        canonical_smiles = request.form.get('canonical_smiles')
        molecular_formula = request.form.get('molecular_formula')
        cas_number = request.form.get('cas_number')
        molecular_weight = request.form.get('molecular_weight')
        drug_class = request.form.get('class')
        superclass = request.form.get('super_class')
        rotable_bond_count = request.form.get('rotable_bond_count')
        complexity = request.form.get('complexity')

        saveData(name, iupac_name, canonical_smiles, molecular_formula, cas_number,  molecular_weight, drug_class, superclass, rotable_bond_count, complexity)

    drugs = getDrugs()

    return render_template('home.html', drugs=drugs)

# still working on - complete later
@app.route('/<drug_name>/edit', methods=['GET', 'POST'])
def editDrug(drug_name):
    
    if request.method == 'POST':
        return redirect(url_for('home'))
        
    else:
        return render_template('edit_drug.html')


#still working on - complete later
@app.route('/<drug_name>/delete', methods=['GET', 'POST'])
def deleteDrug(drug_name):
    
    if request.method == 'POST':
        return redirect(url_for('home'))
        
    else:
        return render_template('delete_drug.html')


if __name__ == '__main__':
    app.run(debug=True)
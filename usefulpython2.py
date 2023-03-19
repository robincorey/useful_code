# Follow up tips for better coding

# f strings for printing strings

a = 'there'
b = 'ugly'

print(f"hi {a} you are very {b}")

# better looping

a = [1, 2, 3]

# old and ugly
for i in range(len(a)):
	print(i)

# new and swish
for i in a:
	print(i)


# classes

class Employee:
	def __init__(self, first, last, email, pay): # make instance first arg
		# define attributes
		self.first = first
		self.last = last
		self.email = first + ‘.’ last + ‘@companyname.com’
		self.pay = pay
	def full_name(self):
		return ‘{} {}’.format(self.first, self.last) # def method

emp_1 = Employee(‘doodie’, ‘poodie’, 50000)
print(emp_1.full_name())

# RDKit

# load the data and look at them
df= pd.read_csv('../input/mlchem/logP_dataset.csv', names=['smiles', 'logP'])
df.head()

#Importing Chem module
from rdkit import Chem 

#Method transforms smiles strings to mol rdkit object
df['mol'] = df['smiles'].apply(lambda x: Chem.MolFromSmiles(x)) 

from rdkit.Chem import Draw
mols = df['mol'][:20]

#MolsToGridImage allows to paint a number of molecules at a time
Draw.MolsToGridImage(mols, molsPerRow=5, useSVG=True, legends=list(df['smiles'][:20].values))

df['mol'] = df['mol'].apply(lambda x: Chem.AddHs(x))
df['num_of_atoms'] = df['mol'].apply(lambda x: x.GetNumAtoms())
df['num_of_heavy_atoms'] = df['mol'].apply(lambda x: x.GetNumHeavyAtoms())

#settle the function that searches patterns and use it for a list of most common atoms only
def number_of_atoms(atom_list, df):
    for i in atom_list:
        df['num_of_{}_atoms'.format(i)] = df['mol'].apply(lambda x: len(x.GetSubstructMatches(Chem.MolFromSmiles(i))))

# gets the number of C, O, N and C1 atoms per mol
# allows one to plot against each other, total atoms, logp etc
number_of_atoms(['C','O', 'N', 'Cl'], df)

# train a model using sklern 
#  use ridge regression ; a model tuning method that is used to analyse any data that suffers from multicollinearity.
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import train_test_split

#Leave only features columns (i.e. remove smiles, mol and logpm keep num of each atom type)
train_df = df.drop(columns=['smiles', 'mol', 'logP'])
y = df['logP'].values

print(train_df.columns)

#Perform a train-test split. Use 10% of the data to evaluate the model while training on 90%
X_train, X_test, y_train, y_test = train_test_split(train_df, y, test_size=.1, random_state=1)
Index(['num_of_atoms', 'num_of_heavy_atoms', 'num_of_C_atoms',
       'num_of_O_atoms', 'num_of_N_atoms', 'num_of_Cl_atoms'],
      dtype='object')

# evaluation using MAE or MSE. 
from sklearn.metrics import mean_absolute_error, mean_squared_error
def evaluation(model, X_test, y_test):
    prediction = model.predict(X_test)
    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    
    plt.figure(figsize=(15, 10))
    plt.plot(prediction[:300], "red", label="prediction", linewidth=1.0)
    plt.plot(y_test[:300], 'green', label="actual", linewidth=1.0)
    plt.legend()
    plt.ylabel('logP')
    plt.title("MAE {}, MSE {}".format(round(mae, 4), round(mse, 4)))
    plt.show()
    
    print('MAE score:', round(mae, 4))
    print('MSE score:', round(mse,4))
	
#Train the model
ridge = RidgeCV(cv=5)
ridge.fit(X_train, y_train)
#Evaluate results
evaluation(ridge, X_test, y_test)

# RDKit atoms, bonds and rings
# GetRingInfo(), GetAtoms() and GetBonds() yield corresponding generators over rings and atoms in molecule.

atp = Chem.MolFromSmiles('C1=NC2=C(C(=N1)N)N=CN2[C@H]3[C@@H]([C@@H]([C@H](O3)COP(=O)(O)OP(=O)(O)OP(=O)(O)O)O)O')

# Getting number of rings with specified number of backbones
print('Number of rings with 1 backbone:', atp.GetRingInfo().NumAtomRings(1))
print('Number of rings with 2 backbones:', atp.GetRingInfo().NumAtomRings(2))

m = Chem.MolFromSmiles('C(=O)C(=N)CCl')
#Iterating through atoms to get atom symbols and explicit valencies 
for atom in m.GetAtoms():
    print('Atom:', atom.GetSymbol(), 'Valence:', atom.GetExplicitValence())

#rdkit.Chem.Descriptors provides a number of general molecular descriptors that can also be used to featurize a molecule.
from rdkit.Chem import Descriptors
df['tpsa'] = df['mol'].apply(lambda x: Descriptors.TPSA(x))
df['mol_w'] = df['mol'].apply(lambda x: Descriptors.ExactMolWt(x))
df['num_valence_electrons'] = df['mol'].apply(lambda x: Descriptors.NumValenceElectrons(x))
df['num_heteroatoms'] = df['mol'].apply(lambda x: Descriptors.NumHeteroatoms(x))

# followup mol2vec
# Mol2vec is an unsupervised machine learning approach to obtain high dimensional embeddings of chemical substructures
# 1. A molecule is divided into substructures of a fixed radius e.g. a group of closest atoms around a heavy atom)
# 2. These  substructures are fed to Word2vec yielding vector representations of substructures 
# 3. Summing up substructure vectors we get vector representations of whole molecules.

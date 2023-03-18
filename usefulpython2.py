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


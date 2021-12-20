# =============================================================================
# Dict which represents the genetic code.
# the keys are codons and the values are amino acids.
# =============================================================================
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# =============================================================================
# Functions
# =============================================================================
def rho_to_protein(content):
    
   
    rho=[]
    for i in range(0, int(len(content)/3)):
        codon = content[i*3:i*3+3]
        rho.append(codon)
        
        
    protein=""

    for i in rho:
        for j in gencode:
            if i==j:
                protein+=gencode[j]
            
    
    return protein

def list_to_string(rho_as_list):
    str_content=""
    for i in rho_as_list:
        str_content += i
    return str_content
    

def compare_protein(prot_1,prot_2):
    prot_1_list=[]
    prot_2_list=[]
    for prot in prot_1:
        prot_1_list.append(prot)
    for prot in prot_2:
        prot_2_list.append(prot)
        
    iteration=0
    mutation_count=0
    for i in prot_1_list:
        if prot_1_list[iteration] != prot_2_list[iteration]:
            print("MUTATION AT "+str(iteration)+".amino acid.\n"
                  +prot_1_list[iteration]+">>" +prot_2_list[iteration])
            mutation_count +=1
        iteration +=1
        
        
    if mutation_count >3:
        print("#\n#\n Most likely a frame shift mutation... ")
    if mutation_count ==0:
        print("Possible silent mutation or no mutation at all. ")
    print ("----------------------------------------------------------------")
    
# =============================================================================
# Opens file and formats the data. 
# =============================================================================

content = open("rho.fasta")
var1= content.read()
rho_content=var1.replace("\n","")

given_protein = rho_to_protein(rho_content)
            
# =============================================================================
# Turns rho string into a list for easier operation. And produces copies.
# =============================================================================
rho_list=[]
for nuc in rho_content:
    rho_list.append(nuc)
    
copy1=rho_list.copy()
copy2=rho_list.copy()
copy3=rho_list.copy()
copy4=rho_list.copy()
# =============================================================================
# Makes changes on the copies.
# =============================================================================

if copy1[328] == "G":
    copy1[328]="T"
        
if copy2[329]=="C":
    copy2[329]="T"
        
if copy3[1020]=="G" and copy3[1022]== "G":
    copy3[1020]="T"
    copy3[1022]="T"
    
copy4.insert(441,"C")  
# =============================================================================
# Edited copies are turned into strings. 
# =============================================================================
copy1_str= list_to_string(copy1)
copy2_str= list_to_string(copy2)
copy3_str= list_to_string(copy3)
copy4_str= list_to_string(copy4)
# =============================================================================
# Strings of rho's are written as a sequence of amino acids.
# =============================================================================
new_protein_1=rho_to_protein(copy1_str)
new_protein_2=rho_to_protein(copy2_str)
new_protein_3=rho_to_protein(copy3_str)
new_protein_4=rho_to_protein(copy4_str)

# =============================================================================
# Prints the result of comparison of proteins.
# =============================================================================

compare_protein(given_protein,new_protein_1)
compare_protein(given_protein,new_protein_2)
compare_protein(given_protein,new_protein_3)
compare_protein(given_protein,new_protein_4)

    
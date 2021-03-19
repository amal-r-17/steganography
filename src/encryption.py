steg = np.asarray(Image.open(r"C:\Users\amalr\OneDrive\Desktop\Backgrounds\jonatan-pie-3l3RwQdHRHg-unsplash.jpg"))
steg1 = copy.deepcopy(steg)

#taking messag efrom user
data = input("Enter the text to be encrypted: ")
binlist = []
hlist = []
for i in data:
    h = ord(i)
    hlist.append(h)
    
    
n = len(hlist)
hlist.insert(0,n)

#encrypting
j = 0
for i in hlist:
    steg1[j,j,0] = i
    j = j+1
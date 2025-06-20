def add(fName:str,LName:str):
    fName.capitalize()
    return fName+" "+LName

fname = "Sawamura"
lname = "Egin"

name = add(fname.capitalize(),lname)
print(name)
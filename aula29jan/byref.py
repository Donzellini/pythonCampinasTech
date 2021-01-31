# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print("Values inside the function: ", mylist)
   

# Now you can call changeme function
minha_lista = [10,20,30]
changeme( mylist=minha_lista )
print("Values outside the function: ", minha_lista)

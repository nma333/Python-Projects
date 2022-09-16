#Create a product and price for three items
p1i,p1r="orange",5.9
p2i,p2r="mango",9.8
p3i,p3r="apple",10.8

#Create a company name information
cn="Carrige boult"
ca="Cross 3 Ilkal"
cc="Ilkal"

#Declare anding message
message="Thanks for shoping with us"

#Create a top border
print("*" * 50)

#Company information
print(f"\t\t{cn}")
print(f"\t\t{ca}")
print(f"\t\t{cc}")

#Product information
print("="*50)
print("\tProduct name \t Product price")
print("\t%s\t\t\t%d"%(p1i,p1r))
print("\t%s\t\t\t%d"%(p2i,p2r))
print("\t%s\t\t\t%d"%(p3i,p3r))

print("="*50)
#Total price
print(f"\t\t\tTotal Price\n\t\t\t${p1r+p2r+p3r}")

print("="*50)

#Greeting 
print("\tThank you for shopping with US")
print()

print("*" *50)

#OUTPUT:
# **************************************************
#                 Carrige boult
#                 Cross 3 Ilkal
#                 Ilkal
# ==================================================
#         Product name     Product price
#         orange                  5
#         mango                   9
#         apple                   10
# ==================================================
#                         Total Price
#                         $26.5
# ==================================================
#         Thank you for shopping with US

# **************************************************

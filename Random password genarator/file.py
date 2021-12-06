import random


length=int(input("Enter the length of the password:"))

using="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*?/|"

generated_password="".join(random.sample(using,length))

print("generated_password is : "+ generated_password)


Output:
      Enter the length of the password:4
      generated_password is : iI|S
      Enter the length of the password:6
      generated_password is : J58CFd
      Enter the length of the password:8
      generated_password is : A%sGClHx
      Enter the length of the password:2
      generated_password is : 5C
      Enter the length of the password:8
      generated_password is : yWtn7K#2

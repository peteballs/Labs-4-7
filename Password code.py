
import random
print ("Welcome to our unique password generation exercise!!")
s_number = int(input("Please indicate how many lower case letters you require for your password (1-34). Please use number.........."))
n_number = int(input("Please indicate how many upper case letters you require for your password (1-34). Please use number.........."))
cs_number = int(input("Please indicate how many numbers you require for your password (1-34). Please use number.........."))
sc_number = int(input("Please indicate how many special characters you require for your password (1-34). Please use number.........."))
s = "abcdefghijklmnopqrstuvwxyz"
cs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = "01234567890"
sc = "!@#$%^&*()?"
passlen = s_number
p =  "".join(random.sample(s,passlen ))
passlen = n_number
q =  "".join(random.sample(n,passlen ))
passlen = cs_number
r =  "".join(random.sample(cs,passlen ))
passlen = sc_number
s =  "".join(random.sample(sc,passlen ))
h = (p+q+r+s)
h_number = (s_number + n_number + cs_number + sc_number)
passlen = h_number
final_password = "".join(random.sample(h, passlen ))
print (final_password)
print("Outstanding!! Now you have a password that is strong and can prevent fraud!!")
print ("Please come back and recommend us to your friends")
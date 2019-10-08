import random
print("Welcome to our site!")
print("We generate different emoticons")
while True:
  play = input ("Do you want to continue?...(yes or no)...").lower()
  if play == "yes":
    eyes =['*', ':', ';', 'B']
    eye =random.choice(eyes)
    print(eye)
    mouths =['(', ')', ']', '[']
    mouth =random.choice(mouths)
    print(mouth)
    noses =['-', '>', '<', 'o']
    nose =random.choice(noses)
    print(nose)
    print ("This is the finished product. We know it does not look much like a face, but it is the best that we can do!!")
    print(eye+nose+mouth)
    print("Let's Keep Going")
  else:
    print("Thank you for visiting our site!")
    break
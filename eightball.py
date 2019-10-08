# filename: eightball.py
# Print a welcome screen to the user.
# Use the random module's random.choice() to choose a prediction.
# Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
# Display the result of the 8 ball.
import random
eightball_answers = ["It is certain", "As I see it", " My reply is no", "Outlook not so good", "Cannot predict now"]
print("Welcome to the Eight Ball Experience of a Lifetime!")
response = input ("Do you have input for the Magic Eight Ball? (yes/no)...")
while True:
    response = input("Would you like some advice? (yes/no) ...").lower()
    print(f"You replied: {response}")
    if response == "yes":
    # run this line
        print(f"Outstanding! Eight Ball time! There are {len(eightball_answers)} answers. The Eight Ball response is {random.choice(eightball_answers)}. Enjoy!")
    else:
        print("Get out of here. This is not your best day. Please take time off!")
        break
     

#Greeting
print("Welcome to the Tip Calculator!")
#bill amount input by user
bill = float(input("How much was the bill? $"))
#precentage of tip
tip = int(input("How much tip would you like to give? 15, 18, 20?"))
#amount of people
people=int(input("How many people are you splitting the bill with?"))
#how much each person should pay
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people
final = "{:.2f}".format(bill_per_person)

print(f"Each person will need to pay ${final}")
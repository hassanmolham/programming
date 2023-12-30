import os
import subprocess

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls' if os.name == 'nt' else 'echo -e "\\033c"')

clear_terminal()

#print(int(8/3))
#----------------------------------------------------------------
#print(round(8/3,2)) round function can be adjusted based on aprameter that u give it to 
#----------------------------------------------------------------
#print(8//3) floor divesion it  devieds and removes the nums after the dcimal point
#----------------------------------------------------------------
#score=0 ; user scores a point we can manipulatethe var with += or -=
#score+= 1
#score=0
#height =1.68
#iswinning = False
#f- string without it i will have to go change each num type to str by hand to print it 
#print(f"your score is {score}, your height is {height}, you are winning {iswinning}")
#--------------------------------------------------
# user_age=int(input("what is ur current age :"))
# user_age_left=90-user_age
# age_in_days=user_age_left*365
# age_in_weeks=user_age_left*52
# age_in_month=user_age_left*12
# print(f"ur days left is {age_in_days}, ur weeks left is {age_in_weeks}, ur month left is {age_in_month}")
#------------------------------------------------
print("welcome to the tip calculator")
bill_total=float(input("what was the total bill?: $ "))
tip=int(input("what tip percent would u like to give ? 10,12,15: "))
bill_total_with_tip=(tip/100)*bill_total+bill_total
print(f" this is the total of the bill {bill_total_with_tip}")
num_of_people=int(input("how many people will split the bill?: "))
each_person_cost=round(bill_total_with_tip/num_of_people,2)
print(f"how much each will pay :{each_person_cost}")

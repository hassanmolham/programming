height=float(input("enter your height: "))
weight=int(input("enter your weight in kg: "))
BMI=round(weight/height**2, 2)
if BMI<=18.5:
    print(f"ur BMI is {BMI} ur under weight")
elif 18.5<BMI<=25:
    print(f"ur BMI is {BMI}ur normal weight")
elif 25<BMI<=30:
    print(f" ur BMI is {BMI} ur over weight")
elif 30<BMI<=35:
    print(f" ur BMI is {BMI} ur obese")
else:
    print(f" ur BMI is {BMI} ur clinicaly obese")
   
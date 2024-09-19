#1.  find the age in year using python when birth year given
birth_year=2003
current_year=2024
print("age is",int(current_year-birth_year))

#2. Create BMI calculator in python
height=float(input("enter your height in m"))
weight=float(input("enter your weight in kg"))

#bmi=weight(kg)/height^2(m)
bmi_index=weight/height**2
if bmi_index<=18.4:
    print("underweight")
elif bmi_index>=18.4 and bmi_index<=24.9:
    print("normal")
elif bmi_index>=25.0 and bmi_index<=39.9:
    print("overweight")
elif bmi_index>=40.0:
    print("obesity")
else:
    pass

#3. Create currency convertor in python
#rupees into dollars
rsamout=int(input("enter the amount in rs."))
rsintosollars=(rsamout/84)
print(rsamout,"rs in dollars is",rsintosollars)
# dollars into rupees
dollarsamout=int(input("enter the amount in dollars."))
dollarsintors=(dollarsamout*84)
print(dollarsamout," dollars in rs is",dollarsintors)

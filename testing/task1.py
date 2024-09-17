#TASK-1: CALCULATE AGE IN DAYS

from datetime import *
today=date.today()
born_date=date(2003,12,1)

#age in years
print("age in years:",today.year-born_date.year)

#age in days
age=today-born_date
print("age in days:",age.days)

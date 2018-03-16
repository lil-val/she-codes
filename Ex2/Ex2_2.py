from datetime import datetime
now = datetime.now()
current_year = now.year

def name_age():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    year_of_birth = input("what is your year of birth?")
    initials = first_name[0].upper() + last_name[0].upper()
    age = current_year - int(year_of_birth)
    print("Your initials are %s and you are %s years old" % (initials, age))
name_age()

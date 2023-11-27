# age: int
# name: str
# height: float
# is_human: bool

#Declaring the age as an int will give users data type hints if they use the wrong type
#Arrows shows us the expecting return value of the function has to be a boolean

def police_check(age: int) -> bool: 
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")








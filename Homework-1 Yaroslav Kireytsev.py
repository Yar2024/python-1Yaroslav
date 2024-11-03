#from random import randint
#rand_value=randint(1,10)
#print(rand_value)
#user_input=print("Я загадав число від 1 до 10 спробуй його вгадати")
#input("Веди своє число")
#while input==rand_value: user_input=print("You won!")
#Я не розумію чому воно не працює як треба
#################################


from random import randint
rand_value=randint(1,12)
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
random_months_number = randint(1, 12)
month_name = months[random_months_number]
print(f"{random_months_number} - {month_name}")
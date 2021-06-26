print("                      The programe to convert all unites of time into minuts\n")
print ("                     After giving the value please specify the Unit like 'day,week,hour,year'\n")

   
def cal ():
    value = int (input("Enter a value in Numbers to convert in minutes : "))
    unit = input("Enter Unit name : ")
    if unit =='day':
        value_minutes= (value*24)*60
        print(value_minutes,"minutes")
        cal()
    elif unit=='hour':
        value_minutes=value*60
        print(value_minutes,"minutes")
        cal()
    elif unit=='week':
        value_minutes=(value*7)*60
        print(value_minutes,"minutes")
        cal()
    elif unit=='year':
        leap_value=input("Is there any leap year please Give input in only 'yes'or'no' : ")
        if leap_value=='yes':
            leap_year= int(input("how many leap year in the ginven years : "))
            non_leap_year=value - leap_year
            value_minutes=(((leap_year*366)*24)*60)+(((non_leap_year*365)*24)*60)
            print(value_minutes, 'minutes')
        else:
            value_minutes= ((value*365)*24)*60
            print(value_minutes,"minutes")
        cal()
    else: 
        print("wrong input try again..")
        cal()
cal()

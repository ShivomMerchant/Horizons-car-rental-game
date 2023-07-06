 ###########################################################
    #  Project #2
    #
    #  Algorithm
    #    Print welocome messages
    #    Excute while loop
    #       Excute while loop for invaild code
    #       Prompt for customer code, odemeter start and end, and number of days
    #        Declare varibles money, miles
    #        Create if statement if customer code "BD"
    #           Calculate money
    #        Create if statement if customer code "D"
    #           Calculate money
    #        Create if statement if customer code "W"
    #           Calculate money
    #        Print customer summary
    #        If prompt closed, excute closing message 
    ###########################################################
#Import math modulus 
import math
#Print welcome messages 
print("\nWelcome to Horizons car rentals. \n")
print("At the prompts, please enter the following: ")
print("\tCustomer's classification code (a character: BD, D, W) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)\n")

#Prompt user to continue
#If user does not continue, print thank you message
prompt_str = input("Would you like to continue (A/B)? \n")
if prompt_str == "B":
    print("Thank you for your loyalty.")

#Start while loop if user chooses to continue
#Prompt user for customer code
while prompt_str == "A":
    code_str = input("Customer code (BD, D, W): \n")

#Nested while loop, if customer code is invaild
#If customer code is invalid then print statement and prompt again for customer code
    while code_str !="BD" and code_str !="D" and code_str !="W":
        print("\t*** Invalid customer code. Try again. ***\n")
        code_str = input("Customer code (BD, D, W): \n")
    
#Declare money varible as float
#Prompt for number of days and odemeter at start and end
#Declare miles varible, divide by 10 to get decimal
    money_float = float(0.0)
    numdays_int = int(input("Number of days: \n"))
    odemstart_int = int(input("Odometer reading at the start: \n"))
    odemend_int = int(input("Odometer reading at the end:   \n"))
    miles = (odemend_int-odemstart_int)/10

    #If odemeter start value larger than end value then add a million
    #The odemeter more than six digits
    if odemend_int < odemstart_int:
        mileend_tot = odemend_int + 1000000
        miles = (mileend_tot-odemstart_int)/10

#If statement for "BD" customer code
#Calculate money for "BD" by multipying base cost per day, then add cost for every mile driven
    if code_str == "BD":
            money = float(40*numdays_int+0.25*miles)

#Else if statement for "D" customer code
#Calculate money base price times number of days
#If statement for if number of miles driven more than a 100
#If over 100 miles driven by calculating miles driven per day remainder
#tThen multipy by cost per mile and number of days
    elif code_str == "D":
        money = float(60*numdays_int)
        if miles/numdays_int > 100:
            money += .25*(((miles/numdays_int)%100)*numdays_int)

#Else if statement for "W" customer code
#Calculate money by using math.ceil to move to next integer if between weeks
#Decalre weeks varible uses math.ceil to move to next integer if between weeks
#Declare milesperweek varible by dividing miles by number days then multiply by 7
#If statement to determine if milesperweek is less than 900 if then base charge
#Else if to determine miles per week between 900 and 1500
#If true then multipy 100 by number of weeks, and add orginal base charge
#Use else statement if above 1500 miles
#Multiply 200 times weeks, add base charge, and add extra charge per mile
    elif code_str == "W":
        money = math.ceil(numdays_int/7)*190
        weeks = math.ceil(numdays_int/7)
        milesperweek = (miles/numdays_int)*7
        if milesperweek<=900:
            money=float(money)
        elif milesperweek > 900 and milesperweek<1500:
            money = float((100 * weeks) + money)
        else:
            money = float((200*weeks) +((miles-(1500 * weeks))*0.25) + money)
            
#Print customer summary with calculated charge based on customer code imputed    
    print("\nCustomer summary:")
    print("\tclassification code: " + code_str)
    print("\trental period (days): " + str(numdays_int))
    print("\todometer reading at start: " + str(odemstart_int))
    print("\todometer reading at end:   " + str(odemend_int))
    print("\tnumber of miles driven:  " + str(miles))
    print("\tamount due: $ " + str(money))

#Prompt to ask if continue 
#Use if statement if not continued to print thank you message
    prompt_str = input("\nWould you like to continue (A/B)? \n")
    if prompt_str == "B":
        print("Thank you for your loyalty.")



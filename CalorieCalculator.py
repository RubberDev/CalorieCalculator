import sys
import time

br2 = "\n\n"

### CALCULATOR ###
def calculator():
    # Vars
    num_BigMacs : int
    num_MedFries : int
    num_SmallShakes : int
    
    Mac_Cal = 563
    Fry_Cal = 378
    Shake_Cal = 530
    
    max_mac_cal : int
    max_fry_cal : int
    max_shake_cal : int
    
    total_calories : int
    
    # Calc macs
    mac_Amnt = int(input("How many Big Macs did you eat?: "))
    num_BigMacs = mac_Amnt
    max_mac_cal = Mac_Cal * num_BigMacs
    print(str(num_BigMacs) + " Big Macs")
    
    # Calc fries
    fry_Amnt = int(input("How many Medium Fries did you eat?: "))
    num_MedFries = fry_Amnt
    max_fry_cal = Fry_Cal * num_MedFries
    print(str(num_MedFries) + " Medium Fries")
    
    # Calc shakes
    shake_Amnt = int(input("How many Shakes did you drink?: "))
    num_SmallShakes = shake_Amnt
    max_shake_cal = Shake_Cal * num_SmallShakes
    print(str(num_SmallShakes) + " Small Shakes")
    
    total_calories = max_mac_cal + max_fry_cal + max_shake_cal
    
    print(br2)
    print("You've eaten " + str(max_mac_cal) + " calories worth of Big Macs")
    print("You've eaten " + str(max_fry_cal) + " calories worth of Medium Fries")
    print("You've eaten " + str(max_shake_cal) + " calories worth of Small Shakes")
    print("Your total calorie intake was " + str(total_calories) + "\n")
    
    if total_calories > 30000:
        print("You should see a doctor!")
    elif total_calories > 20000:
        print("It will take you at least twenty hours of jogging to burn off your calories!")
    elif total_calories > 10000:
        print("It will take you at least ten hours of jogging to burn off your calories!")
    elif total_calories > 5000:
        print("It will take you at least five hours of jogging to burn off your calories!")
    elif total_calories > 1000:
        print("It will take you at least an hour of jogging to burn off your calories!")
    
    Application()
    
    
    
    
    
### STARTUP MENU ###
def Application():
    while True:
        try:
            begin = str(input("Would you like to begin the program? (Y or N)\n"))
            
            break
        except ValueError:
            print("Error: Field can only contain letters!")
            Application()

    if begin.capitalize() == "Y":
        calculator()
    elif begin.capitalize() == "N":
        print("Exiting program...")
        time.sleep(2.0)
        sys.exit(0)
    else:
        print("Error: Use Y or N to begin or exit!")
        Application()

Application()
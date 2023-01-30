def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    while True:
        try:
            hours = float(input("Enter Hours: "))
            break
        except:
            print('Please only enter a numeric value.')
            continue
    while True:
        try:
            hourly_rate = float(input('Enter Rate: '))
            break
        except:
            print('Please only enter a numberic value.')
            continue
    totalpay = hours*hourly_rate
    print(totalpay)    



    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()

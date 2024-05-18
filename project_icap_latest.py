def startup():
    print("Welcome to UNITEN Sports Facility Booking System")
    print("************************************************************")
    print("Please choose a station by entering the appropriate number")
    for courts in ["1. Futsal","2. Takraw","3. Basketball","4. Badminton"]:
        print(courts)
    validation()
    stations()


def validation():
    #Loop repeats until condition is false
    while True:
        try:
            global court
            global selectCourt
            court = input("Please enter appropriate number for the corresponding station: ")
            selectCourt = int(court)
            break
        except:
            print("Incorrect, please enter correct value")
    while True:
        try:
            while selectCourt > 4:
                REcourt = input("Station does not exist. Please re-enter appropriate number: ")
                selectCourt = int(REcourt)
            break
        except:
            print("Incorrect, please enter correct value")
def stations():
    global student_weekday,public_weekday,student_weekend,public_weekend
    #Stations
    if selectCourt == 1:
        print("You have chosen Futsal")
        
    elif selectCourt == 2:
        print("You have chosen Takraw")
        
    elif selectCourt == 3:
        print("You have chosen Basketball")
        
    else:
        print("You have chosen Badminton")
        
   
    
    
def uniten():
       global student
       global yesChoice
       global noChoice
       student = input("Are you a UNITEN student? (Type Yes or No)\n")
       yesChoice = ["Yes","yes","Y","y"]
       noChoice = ["No","no","N","n"]
       while student not in yesChoice and student not in noChoice:
           print("Incorrect value, please re-enter")
           student = input("Are you a UNITEN student? (Type Yes or No)\n")
       if student in yesChoice:
           student_id = input("Enter your student ID:\n")
           
       else:
           phone = input("Enter your Number phone:\n")
           while phone.isnumeric() == False:
               print("Wrong value")
               phone = input("Enter your Number phone:\n")

def day():
    global days
    days = input("What day would you like to book the court?\n")
    daysChoice = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    daysChoice_lower = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    while days not in daysChoice and days not in daysChoice_lower:
        print("Invalid days")
        days = input("What day would you like to book the court?\n")

def hours():
    while(True):
        try:
            global hoursChoice
            hoursChoice = int(input("Please Enter your hours to play:\n"))
            break
        except:
            print("Incorrect, please enter correct value")
    while True:
        try:
            while hoursChoice > 5:
                hoursChoice = int(input("Hours exceed limit.\nPlease Enter your hours to play:\n"))
            break
        except:
            print("Incorrect, please enter correct value")
            
def calculate_price():
    global student_weekday,public_weekday,student_weekend,public_weekend,weekday,weekend
    weekday=["Monday","Tuesday","Wednesday","Thursday","Friday","monday","tuesday","wednesday","thursday","friday"]
    weekend=["Saturday","Sunday","saturday","sunday"]
    if student in yesChoice and days in weekday:
        print("Price for your court is RM",student_weekday)
    elif student in yesChoice and days in weekend:
        print ("Price for your court is RM",student_weekend)
    elif student in noChoice and days in weekday:
        print("Price for your court is RM",public_weekday)
    elif student in noChoice and  days in weekend:
        print("Price for your court is RM",public_weekend)
        
def prices_stations(x):
    global student_weekday,public_weekday,student_weekend,public_weekend
    if x == 1:
        student_weekday = 50 * hoursChoice
        public_weekday = 60 * hoursChoice
        student_weekend = 50* hoursChoice
        public_weekend=80*hoursChoice
    elif x == 2:
        student_weekday=20*hoursChoice
        public_weekday=60*hoursChoice
        student_weekend=25*hoursChoice
        public_weekend=65*hoursChoice
    elif x == 3:
        student_weekday=55*hoursChoice
        public_weekday=65*hoursChoice
        student_weekend=55*hoursChoice
        public_weekend=85*hoursChoice
    else:
        student_weekday=30*hoursChoice
        public_weekday=60*hoursChoice
        student_weekend=35*hoursChoice
        public_weekend=65*hoursChoice
    

def payment():
    global pay_get
    pay_price=[1,5,10,50,100]
    print("We only Accept RM1,Rm5,RM10,rm50 and RM100")
    while(True):
        try:
            pay_get=int(input("Please insert amount of payment :RM"))
            break
        except:
            print("Incorrect, please enter correct value")
    while True:
        try:
            while pay_get not in pay_price:
                pay_get = int(input("amount invalid.\nPlease Enter correct amount:RM"))
            break
        except:
            print("Incorrect, please enter correct value")
        

def pay_process():
    if student in yesChoice and days in weekday:
        changes=student_weekday
        while changes>0:
            payment()
            changes=changes-pay_get
            if changes<=0:
                print("your payment are finished")
            else:
                print("rm",changes,"left to finish the payment")
        else:
            print("your payment is done!! yayyy")
        if changes<0:
            print("please take your change RM",abs(changes))
            
    elif student in yesChoice and days in weekend:
        changes=student_weekend
        while changes>0:
            payment()
            changes=changes-pay_get
            if changes<=0:
                print("your payment are finished")
            else:
                print("rm",changes,"left to finish the payment")
        else:
            print("your payment is done!! yayyy")
        if changes<0:
            print("please take your change RM",abs(changes))
            
    elif student in noChoice and days in weekday:
        changes=public_weekday
        while changes>0:
            payment()
            changes=changes-pay_get
            if changes<=0:
                print("your payment are finished")
            else:
                print("rm",changes,"left to finish the payment")
        else:
            print("your payment is done!! yayyy")
        if changes<0:
            print("please take your change RM",abs(changes))
            
    elif student in noChoice and  days in weekend:
        changes=public_weekend
        while changes>0:
            payment()
            changes=changes-pay_get
            if changes<=0:
                print("your payment are finished")
            else:
                print("rm",changes,"left to finish the payment")
        else:
            print("###################################")
        if changes<0:
            print("please take your change RM",abs(changes))

    
        
    
       
   
    



startup()       
uniten()
day()
hours()
prices_stations(selectCourt)
print("Uniten student :", student)
print("Day :",days)
print("Hours:",hoursChoice )
calculate_price()
pay_process()
print("Thank You For Using Our Service")

input("Press ENTER to escape")
           



                
            


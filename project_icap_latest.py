def startup():
    print("Welcome to UNITEN Sports Facility Booking System")
    print("************************************************************")
    print("Please choose a station by entering the appropriate number")
    for stations in ["1. Futsal","2. Takraw","3. Basketball","4. Volleyball","5. Badminton"]:
        print(stations)
    validation()


def validation():
    #Loop repeats until condition is false
    while (True):
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
            while selectCourt > 5:
                REcourt = input("Station does not exist. Please re-enter appropriate number: ")
                selectCourt = int(REcourt)
            break
        except:
            print("Incorrect, please enter correct value")
def stations():
    #Stations
    if selectCourt == 1:
        print("You have chosen Futsal")
        global student_weekday = 50*hoursChoice
        global public_weekday = 60*hoursChoice
    elif selectCourt == 2:
        print("You have chosen Takraw")
    elif selectCourt == 3:
        print("You have chosen Basketball")
    elif selectCourt == 4:
        print("You have chosen Voleyball")
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
    if student in yesChoice:
        print(student_weekday)
    
startup()            
uniten()
day()
hours()

input("Press ENTER to escape")
           



                
            



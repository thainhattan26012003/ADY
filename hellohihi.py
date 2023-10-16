
# Author: Dinh Dang Khoa, Tran

#create the list of close restarant and open restaurant in summer
open_in_sum = ["Chick-fil-A", "United Table", "Dunkin' Donuts", "Market @ Halsted", "Moe's Southwest Grill" ]
close_in_sum = ["Panda Express", "Crave Chicago", "Subway", "Circle Burger", "Sbarro", "Wow Bao"]
#dictionary for MS2
link_dict = {"WICS": "https://wics.students.uic.edu/", "LOGICA": "https://logica.students.uic.edu/", "ACM": "https://acm.cs.uic.edu/about/", "LUG": "https://lug.cs.uic.edu/about.html"}
active_dict = {"WICS": True, "LOGICA": True, "ACM": True, "LUG": False}
org_dict = {"WICS": "Women in Computer Science", "LOGICA": "Latinx Organization for Growth in Computing and Academics", "ACM": "Association for Computing Machinery", "LUG": "Linux User Group"}
#create a list of org that out of CS
out_cs_list = ["AIAA", "AICHE", "ASCE", "ASHRAE", "ASME", "BMES", "BSJ", "CMAA", "ECS", "EDT", "EMBS", "EWH", "ESW", "GDSC", "IEEE", "IISE", "NSBE", "OSTEM", "SAE", "SASE", "SHPE", "SSBC", "SWE", "VESE", "AHMB", "HKN"]
#list of degree type
degree_list = ["CSMinor", "CSMajor", "CS+DesignMajor", "DSMajor"]
#cs major dict
cs_major = {"ENGR100": 1, "CS111": 3, "CS141": 3, "CS151": 3, "CS211": 2, "CS251": 4, "CS261": 3, "CS301": 3,"CS341": 3, "CS342": 3, "CS361": 3, "CS362": 3,"CS377": 3,"CS401": 3, "CS461": 3, "CS499": 0}
cs_design_major = {"ENGR100": 0, "CS111": 3, "CS141": 3, "CS151": 3, "CS211": 2, "CS251": 4, "CS261": 3, "CS427": 3, "CS301": 3, "CS342": 3}
cs_minor = {"CS111": 3, "CS141": 3, "CS151": 3, "CS211": 2, "CS251": 4, "CS342": 3}
ds_major = {"ENGR100": 0, "CS111": 3, "CS141": 3, "CS151": 3, "CS211": 2, "CS251": 4, "CS261": 3, "CS377": 3, "CS418": 3, "CS480": 3}
#academic calendar (new function)
calendar_dict_fall = {"Instruction begins": "August 21, M", "Labor Day holiday": "September 4, M", "Thanksgiving holiday": "November 23–24, Th–F", "Instruction ends": "December 1, F"}
calendar_dict_summer = {"Instruction begins": "January 8, M", "Martin Luther King Jr. Day": "January 15, M", "Spring vacation": "March 18-22, M-F", "Instruction ends": "April 26, F"} 
#MS1
def student_center(res_name):
    if res_name in open_in_sum:
        print(res_name, "is open this summer.")
    elif res_name in  close_in_sum:
        print(res_name, "is not open this summer.")
    else:
        print("There's no information for you restaurant, please retype!")
#MS2
def cs_club_info(org): #create the function
    if org.upper() in org_dict: #CS org
        org = org.upper()
        message = f"The club's full name is {org_dict[org]} and here {link_dict[org]} is the link"
        return message
    elif org.upper() in out_cs_list: #out of CS org
        error = "COE"
        link = "https://engineering.uic.edu/undergraduate/student-groups/"
        message = f"{error}: the club is not belong to CS major, see CS club at {link}"
        return message
    else: #other input
        error = "Not a recognized club."
        return error
#MS3
def contacts(phone_dict, friends_list):
    if len(friends_list) > 1: #remove empty list
        friend_name, friend_phone = friends_list[0], friends_list[1] #define var
        #Error handling 2, 4; and remove already name
        if isinstance(friend_name, str) and isinstance(friend_phone, str) and friend_name not in phone_dict and friend_phone[3] == friend_phone[7] == "-":
        #add name and phone into dict    
            phone_dict[friends_list[0]] = friends_list[1] #add name and phone into dict
            a = "You successfully add your contact!"                        
        else:            
            a = "Cannot add your information! Please try again"                   
    else:
        a = "Please type contact information!"
    return a
#MS4
def iadvise(degree, course_list):
    sum1 =0 #earn credit
    total = 0 #total credit of program
    if degree.lower() == "csminor":
        for i in course_list:
            if i in cs_minor:
                sum1 += cs_minor[i]  
        for i in cs_minor.values():
            total += i
        remain_course = [i for i in cs_minor.keys() if i not in course_list] #course remaining

    elif degree.lower() == "csmajor":
        for i in course_list:
            if i in cs_major:
                sum1 += cs_major[i]
        for i in cs_major.values():
            total += i
        remain_course = [i for i in cs_major.keys() if i not in course_list]

    elif degree.lower() == "dsmajor":
        for i in course_list:
            if i in ds_major:
                sum1 += ds_major[i]
        for i in ds_major.values():
            total += i
        remain_course = [i for i in ds_major.keys() if i not in course_list]

    elif degree.lower() == "cs_designmajor":
        for i in course_list:
            if i in cs_design_major:
                sum1 += cs_design_major[i]
        for i in cs_design_major.values():
            total += i
        remain_course = [i for i in cs_design_major.keys() if i not in course_list]
    message = f"You earned {sum1} credit hours on total {total}. Here is your remain course list: {remain_course}"
    return message
#new function 5th, user input season and event they wanna see they day it begin/happen, then the ouput gives when is this event, if user's event not in the event dictionary -> error
def Search_calendar(season, event):
    if season.lower() == "fall":
        if event in calendar_dict_fall:
            message = f"Your event starts at {calendar_dict_fall[event]}.\nMore events at https://catalog.uic.edu/ucat/academic-calendar/"
        else:
            message ="Please try again or see more infomation at https://catalog.uic.edu/ucat/academic-calendar/"
    elif season.lower() == "summer":
        if event in calendar_dict_summer:
            message = f"Your event starts at {calendar_dict_summer[event]}.\nMore events at https://catalog.uic.edu/ucat/academic-calendar/"
        else:
            message = "Please try again or see more infomation at https://catalog.uic.edu/ucat/academic-calendar/"
    else:
        message = "Please try again or see more infomation at https://catalog.uic.edu/ucat/academic-calendar/"
    return message
#6th function 
#user is asked to type the number of credit hours they get per grade (A-F), then the output calculate their final GPA, final deficit point and give them advise/encouragement.
def gpa_calculator(grade_a, grade_b, grade_c, grade_d, grade_f): #take number of credit hours they get at every grade as parameters
    total = grade_a + grade_b + grade_c + grade_d + grade_f #total credit earned
    final_gpa = (grade_a*4 + grade_b*3 + grade_c*2 + grade_d*1)/total #final gpa
    deficit_point = grade_a*2 + grade_b*1 + grade_d*(-1) + grade_f*(-2) #final deficit point
    print(f"You took totally {total} credit hours for this sem!")
    print(f"Your final GPA is {final_gpa}!")
    print(f"Your final deficit point is {deficit_point}")
    if 3.5 <= final_gpa <= 4:
        print("Congratulation! You did an exellent work in this sem!!!")
    elif 3.0 <= final_gpa < 3.5:
        print("You did a good job, keep working hard for next sem!!")
    elif 2.0 <= final_gpa < 3.0:
        print("You should meet your academic advisor to find a solution for next sem.")
    else:
        print("You must meet your academic advisor!! Your score is alarmingly low!")
    print("See more information at https://las.uic.edu/advising/gpa-calculator/")
#7th function. The function will take user's last name as parameter and then base of the first letter of that name -> find their advisor. 
def finding_advisor(lastname):
    lastname = lastname.upper()
    if 65 <= ord(lastname[0]) < 67: #find advisor based on name (convert name to int)
        advisor = "Your advisor is EJ Baker."
    elif ord(lastname[0]) == 67:
        advisor = "Your advisor can be EJ Baker or Riley Carroll. See https://cs.uic.edu/undergraduate/cs-advising/ for more information."
    elif 68 <= ord(lastname[0]) <= 72:
        advisor = "Your advisor is Riley Carroll."
    elif 73 <= ord(lastname[0]) <= 75 or 87 <= ord(lastname[0]) <= 90:
        advisor = "Your advisor is Akangkha Khan."
    elif 76 <= ord(lastname[0]) < 78:
        advisor = "Your advisor is Melissa Bryant."
    elif ord(lastname[0]) == 78:
        advisor = "Your advisor can be Melissa Bryant or Bryant Hill. See https://cs.uic.edu/undergraduate/cs-advising/ for more information."
    elif 79 <= ord(lastname[0]) <= 82:
        advisor = "Your advisor is Bryant Hill."
    elif 83<= ord(lastname[0]) <= 86:
        advisor = "Your advisor is Lahney Vilayhong"
    return advisor

if __name__ == '__main__':
    print("***********************************")
    print("     Welcome to CS student app!    ")
    print("***********************************")
    print("Menu:\nRestaurant\nClubs\nContact\niAdvise\nAcademic Calendar\nGPA calculator\nMy advisor")
    user_choice = input("Type what you need (Restaurant/ Clubs/ Contact/ iAdvise/ Academic Calendar/ GPA calculator/ My advisor) or 'exit' to exit: ")
    user_choice = user_choice.lower()
    while(user_choice != "exit"):
        #MS1
        if user_choice == "restaurant": 
            print("All the restaurant: ")
            for i in (open_in_sum + close_in_sum): #i in list of all restaurants
                print(i)
            restaurant_name = input("\nEnter your restaurant or exit: ") #if wanna stop searching for restaurant
            if restaurant_name.lower() == "exit": 
                user_choice = input("Type what you need (Restaurant/ Clubs/ Contact/ iAdvise/ Academic Calendar/ GPA calculator/ My advisor) or 'exit' to exit: ")
            else:
                print("Loading........")
                student_center(restaurant_name) #call function ms1
        #MS2    
        elif user_choice == "clubs":
            print("See our organizations/clubs at https://engineering.uic.edu/undergraduate/student-groups/")
            your_club = input("What club's information you are finding or exit: ") #if they wanna stop searching for clubs, else they can continue
            if your_club.lower() == "exit": 
                user_choice = input("Type what you need (Restaurant/ Clubs/ Contact/ iAdvise/ Academic Calendar/ GPA calculator/ My advisor) or 'exit' to exit: ")            
            else:
                your_club = your_club.upper()
                print("Loading........")
                print(cs_club_info(your_club)) #call function ms2           
        #MS3    
        elif user_choice == "contact":
            contact_dict = {}
            user_information = input("Type name and phone number (name, ***-***-***) or exit: ")
            print("Loading........")                
            contact_list = [user_information] #add input into list
            print(contacts(contact_dict, contact_list)) #call function ms3
            user_choice = input("Type what you need (Restaurant/ Clubs/ Contact/ iAdvise/ Academic Calendar/ GPA calculator/ My advisor) or 'exit' to exit: ")
        #MS4           
        elif user_choice == "iadvise":
            program = input("Type your program (CSMinor/CSMajor/CS_DesignMajor/DSMajor): ")
            course = input("Type your course (course1 course2 course 3): ")
            course = course.upper()
            print("Loading........")
            course_new = course.split() #change input into list
            print(iadvise(program, course_new)) #call function ms4
            user_choice = input("Type what you need (Restaurant/ Clubs/ Contact/ iAdvise/ Academic Calendar/ GPA calculator/ My advisor) or 'exit' to exit: ")
        #5th function call
        elif user_choice == "academic calendar": #new function
            academic_season = input("Which season of your event (fall/ summer) or exit: ") #season they wanna find academic calendar
            if academic_season.lower() == "exit": #if they wanna stop searching for calendar
                user_choice = input("Type what you need (Restaurant/ Clubs/ Contact/ iAdvise/ Academic Calendar/ GPA calculator/ My advisor) or 'exit' to exit: ")
            else:
                print("Loading........") 
                if academic_season.lower() == "fall":
                    print("Available event you can see on app")
                    for i in calendar_dict_fall.keys(): #print all the events in fall
                        print(i)                        
                    events = input("Type one of event above (Please type exactly to see the result): ")
                elif academic_season.lower() == "summer":
                    print("Available event you can see on app")
                    for i in calendar_dict_summer.keys(): #all events in summer
                        print(i)                     
                print(Search_calendar(academic_season, events))
        #6th function call
        elif user_choice == "gpa calculator":
            total_A = int(input("How many credit hours you get grade A: "))
            total_B = int(input("How many credit hours you get grade B: "))
            total_C = int(input("How many credit hours you get grade C: "))   
            total_D = int(input("How many credit hours you get grade D: "))
            total_F = int(input("How many credit hours you get grade F: "))
            gpa_calculator(total_A, total_B, total_C, total_D, total_F)
            user_choice = input("Type what you need (Restaurant/ Clubs/ Contact/ iAdvise/ Academic Calendar/ GPA calculator/ My advisor) or 'exit' to exit: ") 
        #7th function call
        elif user_choice == "my advisor":
            user_major = input("What is your major: ")
            #finding advisor only available for cs major
            if user_major.lower() != "cs" and user_major.lower()!= "computer science":
                print("We only support for computer science major")                 
            else:
                user_last_name = input("Type your last name: ")
                print(finding_advisor(user_last_name))
            user_choice = input("Type what you need (Restaurant/ Clubs/ Contact/ iAdvise/ Academic Calendar/ GPA calculator/ My advisor) or 'exit' to exit: ")
        else:
            print("Error, please try again!")
            user_choice = input("Type what you need (Restaurant/ Clubs/ Contact/ iAdvise/ Academic Calendar/ GPA calculator/ My advisor) or 'exit' to exit: ")
        
    print("***********************************")
    print("   Thank you for using my app ^.^  ")
    print("***********************************")
            
        




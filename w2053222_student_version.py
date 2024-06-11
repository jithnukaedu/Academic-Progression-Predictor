# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student IIT ID    :   20222123
# UoW ID            :   w2053222
# Date              :   25 / 12 / 2023

# Initialize variables

pro_lvl_1="Progress"
pro_lvl_2="Progress (module trailer)"             
pro_lvl_3="Module retriever"                    
pro_lvl_4="Exclude"

# Giving user instructions

print("************************* Welcome *************************")
print(" Follow the instructions to predict your progression outcome.")

# Getting user inputs

def input_valid_number(progression_level="PASS"):
    while True:
        try:
            user_respond = int(input(f"\nEnter your total {progression_level} credits : "))
            if 0 <= user_respond <= 120 and user_respond % 20 == 0:
                return user_respond
            else:                       # Part 1 - B (Validation)
                print("Out of range")
        except ValueError:              # Part 1 - B (Validation)
            print("Integer required") 

# create a function to handle main calculations in the program.

def main():  
    pass_credit = input_valid_number("PASS")
    defer_credit = input_valid_number("DEFER")
    fail_credit = input_valid_number("FAIL")
    
    check_valid_total(pass_credit, defer_credit, fail_credit)

def check_valid_total(pass_credit, defer_credit, fail_credit):  # Part 1 - A (Outcomes) Check the total and display progression levels.
    total = pass_credit + defer_credit + fail_credit
    if(total==120):
        progress_level = sort_progression_outcome(pass_credit,fail_credit)
        print(f"\n{progress_level}")
    else:
        print("\nTotal incorrect")                                  
        main()                                                      

# create a function which accepts three parameters Pass,Defer and Fail (Sorting progression levels)

def sort_progression_outcome(Pass,Fail):                                 
    if(Pass==120):                                      
        return pro_lvl_1       
    elif(Pass==100):     
        return pro_lvl_2   
    elif(Fail>=80):                                        
        return pro_lvl_4                                   
    else:                                                  
        return pro_lvl_3                                                                   

# Part 1 - C (Multiple Outcomes) Infinite while loop to handle entire looping process.

while True:
    main()
    user_option = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    if user_option.lower() == "y":
         print("")
         continue
    elif user_option.lower() == "q":
        break
    else:
        print("Not a valid option")
        break                                     

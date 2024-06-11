# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID        :   20222123
# UoW ID            :   w2053222
# Date: 25,26,27 / 11 / 2023

# Import libraries from graphics.py

from graphics import *

# Giving user instructions

print("************************* Welcome *************************")
print(" Follow the instructions to predict your progression outcome.")
print("(Ensure that the 'graphics.py' library is available in the same directory as this script)")

# Initialize variables

progression_data = []
progress = [0]
trailer = [0]
retriever = [0]
excluded = [0]
pro_lvl_1 = "Progress"
pro_lvl_2 = "Progress (module trailer)"
pro_lvl_3 = "Do not progress - Module retriever"
pro_lvl_4 = "Exclude"

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

    total = pass_credit + defer_credit + fail_credit            # calculate the total
    check_valid_total(pass_credit, defer_credit, fail_credit)   # call the check_valid_total function

def check_valid_total(pass_credit, defer_credit, fail_credit):              # Part 1 - A (Outcomes) Check the total and display progression levels.
    total = pass_credit + defer_credit + fail_credit
    if total == 120:
        progress_level = sort_progression_outcome(pass_credit, fail_credit) # call "sort_progression_outcome" function to get the progression level,store it in progress_level.
        print(f"\n{progress_level}")
        insert_to_the_list(progression_data, progress_level, pass_credit, defer_credit, fail_credit)
    else:       # Part 1 - B (Validation)
        print("\nTotal incorrect")
        
# create a function which accepts three parameters Pass,Defer and Fail (Sorting progression levels)

def sort_progression_outcome(Pass, Fail):
    if Pass == 120:
        progress[0] += 1
        return pro_lvl_1
    elif Pass == 100:
        trailer[0] += 1
        return pro_lvl_2
    elif Fail >= 80:
        excluded[0] += 1
        return pro_lvl_4
    else:
        retriever[0] += 1
        return pro_lvl_3

# create a function save all progression data to a list (Related to Part 2,3)

def insert_to_the_list(progression_data, progress_level, pass_credit, defer_credit, fail_credit):
    progression_data.append([progress_level, pass_credit, defer_credit, fail_credit])

# Part 2 | Extend the program with list (Display the progression data)

def display_progression_data():
    for data_set in progression_data:
        print(data_set[0],"-",data_set[1],",",data_set[2],",",data_set[3])

# Part 3 | Extend the program with text file (Saving the progression data)

def write_text_file(progression_data):
    with open("Progression Data.txt", "w") as progression_data_file:
        progression_data_file.write("Part 3\n\n")
        for data_set in progression_data:
            ready_to_write = f"{data_set[0]} - {data_set[1]} , {data_set[2]} , {data_set[3]}\n"
            progression_data_file.write(ready_to_write)

# Part 1 - D (Histogram) Creating a histogram with use of graphics.py <Simple object oriented graphics library> <Python Programming: An Introduction to Computer Science><Franklin, Beedle & Associates>

def draw_histogram():
    win = GraphWin("Histogram", 760, 600)
    win.setBackground(color_rgb(238,243,238))
    title = Text(Point(180,30), "Histogram Results")
    title.setSize(18)
    title.setFace("arial")
    title.setStyle("bold")
    title.draw(win)
    categories = ["Progress", "Trailer", "Retriever", "Exclude"]

    # Using RGB for match bar colors *same as coursework specification* (to match I used - https://www.rapidtables.com/web/color/RGB_Color.html)

    colorR = [176,129,143,216]
    colorG = [255,182,158,179]
    colorB = [176,129,113,203]
    
    counts = [progress[0], trailer[0], retriever[0], excluded[0]]

    for i in range(len(categories)):
        # Draw bars of histogram
        box = Rectangle(Point(90 + i * 150, 499 - counts[i] * 20), Point(220 + i * 150, 499))
        box.setFill(color_rgb(colorR[i],colorG[i],colorB[i]))
        box.draw(win)

        # Draw & customize the count texts of histogram
        text = Text(Point(150 + i * 150, 490 - counts[i] * 20), counts[i])
        text.setSize(14)
        text.setTextColor(color_rgb(90,90,90))
        text.setFace("arial")
        text.setStyle("bold")
        text.draw(win)
    
        # Draw & customize the labels of histogram
        label = Text(Point(150 + i * 150, 520), categories[i])
        label.setSize(14)
        label.setTextColor(color_rgb(90,90,90))
        label.setFace("arial")
        label.setStyle("bold")
        label.draw(win)

    # Draw the total count in bottom of histogram
    total = sum(counts)
    total_text = Text(Point(200,560),f"{total} outcomes in total.")
    total_text.setSize(16)
    total_text.setTextColor(color_rgb(80,80,80))
    total_text.setFace("arial")
    total_text.setStyle("bold")
    total_text.draw(win)
    
    # Draw x-axis of the Histogram
    xline = Line(Point(20,500),Point(740,500))
    xline.draw(win)

    try:
        win.getMouse()
    except GraphicsError:
        pass
    win.close()

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

# Calling Functions

print("\nPart 2\n")
write_text_file(progression_data)
display_progression_data()
draw_histogram()

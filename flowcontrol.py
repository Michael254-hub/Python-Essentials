# Control Flow - Making Decisions! 🧠

# Python can make decisions based on certain conditions, using if-else statements. This is called control flow—it helps us control how our code runs.

# 📝 Example:

temperature = 30

if temperature > 25:
    print("It’s a hot day! ☀️")
else:
    print("It’s a cool day! ❄️")




# 💡 You can also add elif for multiple conditions:

# Control flow example for grading student marks
# This will ask the user for input and grade the student's performance

# Prompt the user for student marks
marks = int(input("Enter the student's marks (0-100): "))

# Grading system based on the marks
if marks > 70:
    print("Grade: Distinction 🏆")
elif marks >= 60:
    print("Grade: Credit 🎖️")
elif marks >= 50:
    print("Grade: Pass 👍")
else:
    print("Grade: Fail ❌")


# How this code works:
# The code first prompts the user to input the student's marks.
# Based on the marks, the program uses if, elif, and else to determine the student's grade:
# If the marks are greater than 70, it prints "Distinction 🏆".
# If the marks are between 60 and 70 (inclusive), it prints "Credit 🎖️".
# If the marks are between 50 and 59 (inclusive), it prints "Pass 👍".
# If the marks are less than 50, it prints "Fail ❌".

# 💡 Python reads the condition and decides which block of code to run. Just like choosing what to do based on the weather—if it’s raining, take an umbrella! ☔
import numpy

import math
from math import *

import os
import sys

os.chdir("C:\\Users\\justi_jtw\\OneDrive\\Documents\\GitHub\\Coding\\Python\\Python Tutorials\\FreeCodeCamp Tutorial\\python")

send = print
say = print

# input("Enter anything to continue ")


# class hello_world:
#     print(f"Hello World")


# class drawing_a_shape:
#     print(f"""   /|\n  / |\n /  |\n/___|""")


# class variables_and_data_types:
#     name = f"John"
#     age = 70
#     message = f"""There once was a man named {name},\nHe was {age} years old.\nHe really liked the name {name},\nbut didn't like being {age}."""
#     print(message)


# class working_with_strings:
#     phrase = f"Hello Python"
#     print("Hello \nPython")
#     print(phrase)
#     print(phrase.lower())
#     print(phrase.upper())
#     """Len returns the number of of characters in a string"""
#     print(len(phrase))
#     print(phrase[0])
#     """For index, caps matter, phrase.index(f"P") and phrase.index(f"p") will give different responces"""
#     print(phrase.index(f"P"))
#     phrase1 = phrase
#     print(phrase1.replace("Python", "JavaScript"))


# class working_with_numbers:
#     my_number = 7
#     print(my_number)
#     my_negative_number = -7
#     """abs stands for absolute"""
#     print(abs(my_negative_number))
#     """pow stands for power"""
#     print(pow(2, 3))
#     """Max returns the largest number of any amount of numbers"""
#     print(max(6, 8, 5))
#     """Min returns the smallest number of any amount of numbers"""
#     print(min(6, 8, 5))
#     """Round rounds a number. NOTE: .5 will wound down"""
#     print(round(2.6))
#     """Floor will always round a number down"""
#     print(floor(2.6))
#     """Ceil will always round a number up"""
#     print(ceil(6.2))
#     """sqrt will give the square root of a number"""
#     print(sqrt(36))


# class getting_input:
#     """This is for input"""
#     # input(f"Enter your name: ")
#     """add a variable if you want to store the input"""
#     user_name = input(f"Enter your name: ")
#     print(f"Hello {user_name}")


# class building_a_basic_calculator:
#     num1 = float(input("Enter a number: "))
#     num2 = float(input("Enter another number: "))
#     result = (num1) + (num2)
#     print(result)
#     """Alternatively you could do print(num1 + num2)"""
#     # print(num1 + num2)


# class mad_libs_game:
#     colour = input("Enter a colour: ")
#     plural_noun = input("Enter a Plural Noun: ")
#     celebrity = input("Enter a celebrity: ")

#     print(f"Roses are {colour}")
#     print(f"{plural_noun} are blue")
#     print(f"I love {celebrity}")


# class lists:
#     friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#     """           0        1        2      3        4
#     python starts counting at 0 not 1,
#     if you use a negative it will start from the end of the list."""
#     print(friends[-1])
#     """If you add a number:number it will grab everything from in between those 2,
#     however it will not include the first number but will include the second.
#     example is bellow"""
#     print(friends[1:3])
#     """you can use list_name[number] = "new variable" to edit a list"""
#     friends1 = friends
#     friends1[1] = "Mike"
#     print(friends1[1])


# class list_functions:
#     lucky_numbers = ["7", "77", "5", "1", "2", "3"]
#     friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
#     friends1 = friends
#     lucky_numbers1 = lucky_numbers
#     """Adds the list, basically joins the list"""
#     friends1.extend(lucky_numbers1)
#     print(friends1)
#     """Adds a new object to the end of the list"""
#     friends1.append("Creed")
#     """Adds a bew item to the specified location"""
#     friends1.insert(1, "Kelly")
#     """Removes the specified object"""
#     friends1.remove("Jim")
#     """Clears the list"""
#     friends1.pop()
#     """Shows the position of an object"""
#     print(friends.index("Kevin"))
#     """Shows the number of times and object is in the list"""
#     print(friends.count("Jim"))
#     """Sorts all the items by alpabetical order"""
#     friends1.sort()
#     print(friends1)
#     """Sorts all the items in ascending order order"""
#     lucky_numbers1.sort()
#     print(lucky_numbers1)
#     """Joins a list together, default is -"""
#     friends2 = ", ".join(friends1)
#     print(friends2)
#     friends1.clear()
#     """Removes an object"""


# class tuples:
#     """Tuples can't be changed or edited"""
#     coordinates = (4, 5)
#     coordinates1 = coordinates
#     print(coordinates)
#     """Some similar stuff too lists"""
#     print(coordinates[0])
#     print(coordinates1[1])
#     """You can have a list of tuples"""
#     coordinates2 = [(4, 5), (1, 2)]


# class functions:
#     def say_hi(name, age):
#         print(f"Hello {name}, you are {age}")

#     print("Top")
#     """How to run a function"""
#     say_hi(name="John", age="20")
#     print("Bottom")


# class return_statement:
#     def cube(number):
#         return number*number*number
#     print(cube(3))
#     """You could also do:"""
#     def cube2(number):
#         number = number*number*number
#         return number
#     number = cube2(4)
#     print(number)


# class if_statements:
#     is_male = True
#     is_tall = True

#     if is_male or is_tall:
#         """checks if you are tall or a male"""
#         print("You are either a male, tall or both!")
#     else:
#         """only runs if both is_male and is_tall is false"""
#         print("Your nither a male nor tall")

#     """You can also do:"""
#     if is_male and is_tall:
#         print(f"You are a tall male.")
#     elif is_male and not(is_tall):
#         print(f"You are a short male.")
#     elif not(is_male) and is_tall:
#         print(f"You are not a male but are tall.")
#     else:
#         print(f"You are not a male and not tall.")


# class if_statements_and_comparisons:
#     def max_num(num1, num2, num3):
#         # """Checks if num1 is greater than or equal to num 2 and 3"""
#         if num1 >= num2 and num1 >= num3:
#             return num1
#         # """Checks if num2 is greater than or equal to num 1 and 3
#         # but only if num1 is not greater than or equal to num 2 and 3"""
#         elif num2 >= num1 and num2 >= num3:
#             return num2
#         # """Returns num3"""
#         else:
#             return num3

#     print(max_num(3, 4, 5))

#     """My version, includes a error handler"""
#     def max_num_2(num1, num2, num3):
#         try:
#             # """Checks if num1 is greater than or equal to num 2 and 3"""
#             if num1 >= num2 and num1 >= num3:
#                 return num1
#             # """Checks if num2 is greater than or equal to num 1 and 3
#             # but only if num1 is not greater than or equal to num 2 and 3"""
#             elif num2 >= num1 and num2 >= num3:
#                 return num2
#             # """Returns num3"""
#             else:
#                 return num3
#         except Exception():
#             print("ERROR!")


# class building_a_better_calculator:
#     """Input stuff"""
#     num1 = float(input(f"Enter the first number: "))
#     opperator = input("Enter a operator: ")
#     num2 = float(input(f"Enter the second number: "))

#     if opperator == "+":
#         print(num1 + num2)
#     elif opperator == "-":
#         print(num1 - num2)
#     elif opperator == "/":
#         print(num1 / num2)
#     elif opperator == "*":
#         print(num1 * num2)
#     else:
#         print(f"Invalid operator.")


# class Dictionaries:
#     month_conversions = {
#         'Jan' or 'jan': 'January',
#         'Feb' or 'feb': 'February',
#         'Mar' or 'mar': 'March',
#         'Apr' or 'apr': 'April',
#         'May' or 'may': 'May',
#         'Jun' or 'jun': 'June',
#         'Jul' or 'jul': 'July',
#         'Aug' or 'aug': 'August',
#         'Sep' or 'Sept' or 'sep' or 'sept': 'September',
#         'Oct' or 'oct': 'October',
#         'Nov' or 'nov': 'November',
#         'Dec' or 'dec': 'December'
#     }
#     print(month_conversions["Nov"])
#     print(month_conversions.get("Dec"))
#     print(month_conversions.get("Luv", "Not a valid key"))


# class while_loop:
#     i = 1
#     """while 1 is less then 10"""
#     while i <= 10:
#         """ i + 1"""
#         i += 1
#     print("Done with loop")


# class building_a_guessing_game:
#     secret_word = "giraffe"
#     guess = ""
#     """While guess does not equal secret word"""
#     while guess != secret_word:
#         guess = input(f"Enter a guess: ")
#     print("You win!!")

#     """Second bit in the video"""
#     secret_word = "giraffe"
#     guess = ""
#     guess_count = 0
#     guess_limit = 3
#     out_of_guesses = False
#     """While guess does not equal secret word and you are not out of guesses"""
#     while guess != secret_word and not(out_of_guesses):
#         if guess_count < guess_limit:
#             guess = input(f"Enter a guess: ")
#             guess_count += 1
#         else:
#             out_of_guesses = True
#     if out_of_guesses:
#         print("Out of guesses, YOU LOSE!")
#     else:
#         print("You win!!")


# class for_loops:
#     friends = ["Jim", "Karen", "Kevin"]

#     """Letter is a variable"""
#     for letter in "Giraffe Academy":
#         """Will print the letters in giraffe academy from first to last"""
#         print(letter)

#     for index in range(10):
#         print(index)

#     for index in range(3, 10):
#         """Prints numbers between 3 and 10"""
#         print(index)

#     for index in range(len(friends)):
#         print(friends[index])

#     for index in range(5):
#         if index == 0:
#             print(f"First Iteration")
#         else:
#             print(f"Not first")


# class Exponent_Function:
#     def raise_to_power(base_num, pow_num):
#         result = 1
#         for index in range(pow_num):
#             result = result * base_num
#         return result
#     print(raise_to_power(3, 2))


# class two_d_lists_and_nested_loops:
#     """A list in a list"""
#     number_grid = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#         [0]
#     ]
#     """Prints the first number from the first list"""
#     print(number_grid[0][0])

#     for row in number_grid:
#         print(row)

#     for row in number_grid:
#         for col in row:
#             print(col)


# class Build_a_Translator:
#     def translate(phrase):
#         translation = ""
#         for letter in phrase:
#             if letter.lower() in "aeiou":
#                 if letter.isupper():
#                     translation = translation + "g"
#                 else:
#                     translation = translation + "g"
#             else:
#                 translation = translation + letter
#         return translation
#     print(translate(input("Enter a phrase: ")))


# class Comments:
#     # This program is cool
#     # THis prints out a string
#     """
#     This is a multi line comment
#     """
#     '''
#     THis also is a multi line comment
#     '''
#     print("Comments are fun")
#     # print("Comments are fun")


# class Try_and_Except:
#     """Basically trying to do:
#         number = int(input(f"Enter a number: "))
#         print(number)"""
#     try:
#         number = int(input(f"Enter a number: "))
#         print(number)
#     except:
#         """I an error happenes"""
#         print("Invalid input")

#     try:
#         answer = 10/0
#         number = int(input(f"Enter a number: "))
#         print(number)
#     except ZeroDivisionError as err:
#         print(err)
#     except ValueError:
#         print("Invalid input")
#     """
#     TIP:
#     Don't use
#     except:

#     instead use
#     use except Exception:

#     I don't want to write too much but if you want to know more you can
#     search it up.
#     """


# class Reading_Files:
#     """
#     This will open up the text document called employees.txt
#     if you can't see the .txt don't worry you just don't have the settings
#     enabled to view the file type.
#     """
#     """r means read, w means write, a means append,
#     r+ means read and write"""
#     employee_file = open("employees.txt", "r")

#     """Will print if it is readable"""
#     print(employee_file.readable())

#     """
#     Will print the items in the file by line
#     this will print the first line.
#     """
#     print(employee_file.readline())
#     """This will print the second"""
#     print(employee_file.readline())
#     """This the third"""
#     print(employee_file.readline())

#     """
#     This will put the items in a list by line,
#     so the first line will be the first item in the list
#     the second line the second, and so on
#     """
#     print(employee_file.readlines())

#     for employee in employee_file.readlines():
#         print(employee)

#     employee_file.close()


# class Writing_to_Files:
#     """the a is for appending"""
#     employee_file = open("employees.txt", "a")
#     employee_file.write("Toby - Human Resources")
#     """Adding a new line for when we append something"""
#     employee_file.write("\nKelly - Customer Service")
#     employee_file.close()


# class Modules_and_pip:
#     import useful_tools

#     print(useful_tools.roll_dice(10))

#     """Run pip install python-docx in the command prompt"""
#     import docx
#     """You can use functions just like the ones in
#     useful_tools"""
#     # docx.


# class Classes_and_Objects:
#     from Student import Student

#     student1 = Student("Jim", "Business", 3.1, False)
#     student2 = Student("Pam", "Art", 2.5, True)


# class Building_a_Multiple_Choice_Quiz:
#     from Question import Question
#     question_prompts = [
#         "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#         "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#         "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
#     ]
#     questions = [
#         Question(question_prompts[0], "a"),
#         Question(question_prompts[1], "c"),
#         Question(question_prompts[2], "b")
#     ]

#     def run_test(questions):
#         score = 0
#         for question in questions:
#             answer = input(question.prompt)
#             if answer == question.answer:
#                 score += 1
#         print(f"You got {score}/{len(questions)} Correct!")
#     run_test(questions)


# class Object_Functions:
#     from Student import Student

#     student1 = Student("Oscar", "Accounting", 3.1)
#     student2 = Student("Phyllis", "Business", 3.8)

#     print(student2.on_honor_roll())


class Inheritance:
    from Chef import Chef

    myChef = Chef()
    myChef.make_special_dish()

    from ChineseChef import ChineseChef

    myChineseChef = ChineseChef()
    myChineseChef.make_special_dish()
    myChineseChef.make_chicken()


class Python_Interpreter:
    """
    You will need to watch the video for this bit:
    https://youtu.be/rfscVS0vtbw?t=15643
    """

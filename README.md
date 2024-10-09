[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16444457)
1.  **Basic If Statement**
    Write a program that:
    -   Asks the user for their age
    -   Prints "You are an adult" if the age is 18 or over
    -   Prints "You are a child" if the age is under 18
    
2.  **If-Else Statement**
    Create a simple number guessing game that:
    -   Generates a random number between 1 and 10
	    - As a Hint, you will need to import the random library at the top of the file, and then generate a random number using the randint function and some parameters. 
	```python		
	import random 
	```
	and then call the generation of the random number with this command
	```python
	secret_number = random.randint(1,  10)
	```
	

    -   Asks the user to guess the number
    -   Prints "Too high" or "Too low" based on the user's guess 
    

3.  **If-Elif-Else Statement**
    Develop a grade calculator that:
    -   Asks for a numerical score (0-100)
    -   Prints the corresponding letter grade:
        
        -   A: 90-100
        -   B: 80-89
        -   C: 70-79
        -   D: 60-69
        -   F: Below 60
        
    -   Includes appropriate messages for each grade
    -   Handles invalid inputs (scores below 0 or above 100)
    -   For Example, if you were to run this and enter 88 you should get a B

4.  **Using 'and' Operator**  
    Create a login system that:
    -   Asks for a username and password
    -   Grants access only if both are correct
    -   Uses predefined correct values (e.g., username: "admin", password: "password123")
    -  This should return Error Access Denied if the username "robert", password "amazingDude" is used.
    
    
5.  **Using 'or' Operator** 
    Write a program that:
    -   Asks the user for a day of the week
    -   Prints "It's the weekend!" if the day is Saturday or Sunday
    -   Prints "It's a weekday." for any other day

6.  **Combining Operators**  
    Develop a movie ticket pricing system that:
    -   Asks for the user's age and whether they're a student (yes/no)
    -   Applies the following rules:
        
        -   Children (under 12) or seniors (65 and over): £5
        -   Students (12-64): £8
        -   Adults (12-64, non-students): £10
        
    -   Prints the ticket price based on the input

7. **Matching Calculator** 
Create a simple command-line calculator that:

	-   Asks the user for two numbers and an operation (+, -, *, /, ^, %)
	-   Uses a match statement to perform the correct operation
	-   Handles division by zero and invalid operations
	-   Continues asking for inputs until the user types "quit"
	- Some Hints :
	-- You will need to use the break command to end when a user quits 
	```python
	case "something":
		print("Quitting the application")
		break
	```
	-- You will also need to have your cases do more than one operation for example
	```python
	match something: 
		case  "+": 
			result = num1 + num2 
			print(f"{num1} + {num2} = {result}")
			
	```
	--Remember to include the default end case!
	
8. **CHALLENGE Project: Adventure Game**  
Develop a text-based adventure game that combines all the concepts learned:

	-   Create a story with at least 5 decision points
	-   Use if-elif-else statements for basic decisions
	-   Incorporate logical operators for complex conditions (e.g., having certain items)
	-   Include a simple inventory system
	-   Implement a win/lose condition
	- Some hints 
	-- You will have to use an array to store items captured. For example 
	```python
	inventory = [] #creates an empty inventory, define outside of a function for now
	inventory.append("Something shiny") # this adds something to inventory array
	inventory.clear() # empties the array 
	inventory.remove("Something shiny") # removes the shiny thing from the inventory
	if "Something shiny" in inventory #checks for the item in the inventory
	
	```

#
	MODEL SOLUTIONS WILL BE PROVIDED NEXT WEEK FOR ALL 8 PARTS.
	DO NOT WORRY IF YOU CANNOT FINISH EVERYTHING IN THE LAB, YOU CAN WORK ON THIS AT HOME.

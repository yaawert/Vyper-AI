#Welcome to Vyper, a basic A.I program
#Open-Source and free to use and modify

import time
import random
from datetime import date

print("Loading...")
time.sleep(1)
print("Loaded\n")
time.sleep(1)
print(" ")			
print('Hello, My name is vyper.')
#start--------------------	
AI = True
while AI == True:
	print("_________________________")
	print(" ")
	start = input(" ")
#-----------------------
	if start == "about":
                print(" ")
                print("Vyper is an A.I Program developed by Ashton Lanning")
                print("Vyper is open source and is active development")
                print("Start date: 5/18/20")
                print("What's needed?: Read/Write to store info, Login/SignUp, Adaptable personality based on user")

#-----------------------	
	if start == "how are you":
		
		print(" ")
		print("Good, how are you?")
		feeling = input(" ")
		print(" ")
		
		if feeling == "good":
			print("That's good. I hope it stays that way.")	
				
		if feeling == "bad":
			print("That's not good. I hope it gets better.")
			
		time.sleep(1)		
#-----------------------
	if start == "how old are you":
		
		print(" ")
		print("I first started being developed on 5/18/20.")
		time.sleep(.5)
		print(" ")
		print("How old are you?")
		age = input(" ")
		age = int(age)
		time.sleep(1)
		print(" ")
		
		if age < 50:
			print("Well, you're pretty young.")
			
				
		if age > 50:
			print("You're not too old.")
		time.sleep(1)

	if start == "calculator":
                calculator = True
                while calculator:
                        time.sleep(1)
                        print(" ")
                        print("1.Addition")
                        print(" ")
                        print("2.Subtraction")
                        print(" ")
                        print("3.Multiplication")
                        print(" ")
                        print("4.Division")
                        print(" ")
                        print("5.Exit")
                        print(" ")
                        
                        choice = int(input("Enter your number: "))
                        
                        if (choice>=1 and choice<=4):
                                print(" ")
                                print("Enter two numbers: ")
                                num1 = int(input(" "))
                                num2 = int(input(" "))
                        
                        if choice == 1:
                                num3 = num1 + num2
                                num1 + num2
                                print(" ")
                                print("Answer is:",num3)
                                print("_________________")
                                time.sleep(3)
                                
                        if choice == 2:
                                num3 = num1 - num2
                                num1 - num2
                                print(" ")
                                print("Answer is:",num3)
                                print("_________________")
                                time.sleep(3)
                        
                        if choice == 3:
                                num3 = num1 * num2
                                num1 * num2
                                print(" ")
                                print("Answer is:",num3)
                                print("_________________")
                                time.sleep(3)
                                
                        if choice == 4:
                                try:
                                        num1 / num2
                                        num3 = num1 / num2
                                        print(" ")
                                        print("Answer is:",num3)
                                        print("_________________")
                                except ZeroDivisionError:
                                        print("ERROR:")
                                        print("You cannot divide by zero")
                                        print("-----------------")
                                        time.sleep(3)
                                        
                        else:
                                print("-----------------")
                                print(" ")
                                time.sleep(1)
                                        
                        if choice == 5:
                                print(" ")
                                print("Ending")
                                break
                                calculator = True
#_____________________________________
	if start == "i want to play a game":
		print(" ")
		print("The games are:")
		print("guess game and blackjack")
		game = input(" ")
		print(" ")
		
		if game == "guess game":
			print("Hello, this is a guessing game where you have to guess a number between 1 and 500")
			print("Take your guesses, you have 20 tries.")
			guessestaken = 0
			while guessestaken < 20:
				number = random.randint(1, 501)
				guess = input()
				guess = int(guess)
				guessestaken = guessestaken + 1
				if guess < number:
					print("Your guess is too low")
				if guess > number:
					print("Your guess is too high")
				if guess == number:
					break
				if guess == number:
					guessestaken = str(guessestaken)
					print('Good job,' + name + '! You guessed my number in ' + guessestaken + 'guesses!')
					guessgame = True
				else:
					guess = input()
#___________________________
		if game == "blackjack":
			comp1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			comp2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			comp3 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			comp4 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			#numA = random.choice([1, 1])
			num1 = random.randint(1, 11)
			num2 = random.randint(1, 11)
			num3 = num1 + num2
			numA = num3
			
			card1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			card2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			card4 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			card6 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			card8 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			cardA = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			
			play = 0
			while play < 1:
				
				time.sleep(2)
				print("--------------------------------------")
				
				#computer plays
				if num3 >= 21:
					print("Dealer busts")
					numA = num3
					break
				#____________
				if num3 <= 10:
					num4 = num3 + comp1
					
					if num4 > 21:
						print("Dealer busts")
						break
						numA = num4
						
					if num4 == 21:
						print("Dealer has blackjack")
						break
						numA = num4
					
					if num3 <= 15:
						num5 = num4 + comp2
					
						if num5 > 21:
							print("Dealer busts")
							break
					
						if num5 == 21:
							print("Dealer has blackjack")
							break
					
						if num5 < 21:
							numA = num5
							
						if num5 <= 15:
							num6 = num5 + comp3
					
							if num6 > 21:
								print("Dealer busts")
								numA = num6
								break
					
							if num6 == 21:
								print("Dealer has blackjack")
								break
								numA = num6
					
							if num6 < 21:
								numA = num6
					
								
				if num3 <= 15:
					num4 = num3 + comp1
					#
					if num4 > 21:
						print("Dealer busts")
						numA = num4
						break
					#
					if num4 == 21:
						print("Dealer has blackjack")
						break
						numA = num4
					#
					if num3 <= 15:
						num5 = num4 + comp2
					#
						if num5 > 21:
							print("Dealer busts")
							numA = num5
							break
					#
						if num5 == 21:
							print("Dealer has blackjack")
							break
							numA = num5
					#
						if num5 < 21:
							numA = num5	
							
						if num5 <= 15:
							num6 = num5 + comp3
					#
							if num6 > 21:
								print("Dealer busts")
								numA = num6
								break
					#
							if num6 == 21:
								print("Dealer has blackjack")
								break
								numA = num6
					#
							if num6 < 21:
								numA = num6
				#----------------
				if num3 < 20:
					chance = random.choice("yes" or "no")
					#
					if chance == "yes":
						num4 = num3 + comp1
						#
						if num4 > 21:
							print("Dealer busts")
							numA = num4
							break
						#
						if num4 == 21:
							print("Dealer has blackjack")
							break
						#
						if num4 < 21:
							numA = num4
						#
					if chance == "no":
						numA = num3
				
				print("Dealer has stopped drawing")
##computer stops------------------------------
				print(" ")
				time.sleep(1)
				print("You drew:")
				print(card1)
				print(" ")
				time.sleep(1)
				print(" ")
				print("You drew:")
				print(card2)
				card3 = card1 + card2
				card1 + card2
				time.sleep(1)
				print(" ")
				print("Your value is:")
				print(card3)
				print(" ")
				print(" ")
					
				if card3 > 21:
					print("Player busts!")
					break
					
				if card3 == 21:
					print("You won!")
					
				if card3 < 21:
					print("Do you want to draw again?")
					print(" ")
					print("(Enter yes or no)")
					answer = input(" ")
					print(" ")

					if answer == "no":
						if numA == card3:
							print(" ")
							print("draw!")
							print(" ")
							print("Deaer had:")
							print(numA)
						if numA > card3:
							print(" ")
							print("Player busts!")
							print(" ")
							print("Dealer had:")
							print(numA)
						if numA < card3:
							print(" ")
							print("You won!")
							print(" ")
							print("Dealer had:")
							print(numA)
					
					
					if answer == "yes":				
						time.sleep(1)
						print("You drew:")
						print(card4)
						print(" ")
						card5 = card4 + card3
						card4 + card3
						time.sleep(1)
						print("Your value is:")
						print(card5)
						
						if card5 > 21:
							print("Player busts!")
							print("Dealer had:")
							print(numA)
							break
							
						if card5 == 21:
							print("You won!")
							print("Dealer had:")
							print(numA)
							blackjack == "won"
							break
						
						if card5 < 21:
							print(" ")			
							print("Draw again?")
							answer = input(" ")
							if answer == "no":
								if numA == card5:
									print(" ")
									print("draw!")
									print(" ")
									print("Dealer had:")
									print(numA)
								if numA > card5:
									print(" ")
									print("Player busts!")
									print(" ")
									print("Dealer had:")
									print(numA)
								if numA < card5:
									print(" ")
									print("You won!")
									print(" ")
									print("Dealer had:")
									print(numA)
							
							if answer == "yes":
								card7 = card5 + card6
								card5 + card6
								time.sleep(1)
								print(" ")
								print("You drew:")
								print(card6)
								time.sleep(1)
								print(" ")
								print("Your value is:")
								print(card7)
								print(" ")

								if card7 == 21:
									print("You won!")
									break
									
								if card7 > 21:
									print("Player busts!")
									break
								
								print("Draw again?")
								
								answer = input(" ")
								
								if answer == "no":
									if numA == card7:
										print(" ")
										print("draw!")
										print(" ")
										print("Dealer had:")
										print(numA)
									if numA > card7:
										print(" ")
										print("Player busts!")
										print(" ")
										print("Dealer had:")
										print(numA)
									if numA < card7:
										print(" ")
										print("You won!")
										print(" ")
										print("Dealer had:")
										print(numA)
								
								if answer == "yes":	
									card9 = card8 + card7
									card8 + card7
									print("You drew:")
									print(card8)
									time.sleep(1)
									print(" ")
									print("Your value is:")
									print(card9)
									
									if card9 > 21:
										print("Player busts!")
										break
									if card9 == 21:
										print("You won!")
										break
										
									print("Draw again?")
									answer = input(" ")
									
									if answer == "yes":
										cardB = cardA + card9
										cardA + card9							
										print("You drew:")
										print(cardA)							
										time.sleep(1)							
										print(" ")							
										print("Your value is:")
										print(cardB)							
										print(" ")
										
										if cardB > 21:
											print("Player busts!")
											break
											
										if cardB == 21:
											print("Player won!")
											break
											
									if answer == "no":
										if numA == cardB:
											print(" ")
											print("draw!")
											print(" ")
											print("Dealer had:")
											print(numA)
										if numA > cardB:
											print(" ")
											print("Player busts!")
											print(" ")
											print("Dealer had:")
											print(numA)
										if numA < cardB:
											print(" ")
											print("You won!")
											print(" ")
											print("Dealer had:")
											print(numA)
				break
##Ends and exceptions-------------------------

	if start == "stop":
		AI = False
		break
else:
	print("I don't know what you mean.")
	start = input(" ")

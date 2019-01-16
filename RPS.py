import time 
import random

print('-'*65)
print()
print('I am Game-Bot! ')
print('You will be playing Rock, Paper, Scissors against me today! I hope you are ready.')
print()
print()

playing = True
while playing:
	
	print()
	print('I am Game-Bot! ')
	print('You will be playing Rock, Paper, Scissors against me today! I hope you are ready.')
	print()
	print()
	print('-'*15)
	print()

	print('Rock')
	print('Paper')
	print('Scissors')
	print()

	P1move = input('Please choose your move out of the 3 shown above: ')

	print()
	print('-'*15)
		

	if P1move in ['Rock', 'Paper', 'Scissors']:
		print()
		print('Your opponent is making their choice! ')
		time.sleep(1/2)
		time.sleep(1/2)
		
		CPUmove = random.randint(1,3)

	#Loop
	while P1move not in ['Rock', 'Paper', 'Scissors']:
		print('That is not a valid move! Choose a move!')
		print()
		P1move = input('Please choose your move out of the 3 shown above: ')

		if P1move in ['Rock', 'Paper', 'Scissors']:
			print()
			print('Your opponent is making their choice! ')
			print()
			time.sleep(1/2)
			time.sleep(1/2)
		
			CPUmove = random.randint(1,3)
	#Loop

	if CPUmove == 1:
		CPUmove = 'Rock'

		print()
		print('Your choices have been locked in! Get ready to shoot! ')
		print()

		print('-'*20)
		time.sleep(1)
		print('Rock!')
		time.sleep(1)
		print('Paper!')
		time.sleep(1)
		print('Scissors...')
		time.sleep(1)
		print('Shoot!')




	elif CPUmove == 2:
		CPUmove = 'Paper'

		print()
		print('Your choices have been locked in! Get ready to shoot! ')
		print()

		print('-'*20)
		time.sleep(1)
		print('Rock!')
		time.sleep(1)
		print('Paper!')
		time.sleep(1)
		print('Scissors...')
		time.sleep(1)
		print('Shoot!')
		



	elif CPUmove == 3:
		CPUmove = 'Scissors'

		print()
		print('Your choices have been locked in! Get ready to shoot! ')
		print()

		print('-'*20)
		time.sleep(1)
		print('Rock!')
		time.sleep(1)
		print('Paper!')
		time.sleep(1)
		print('Scissors...')
		time.sleep(1)
		print('Shoot!')
		

	#Winning/losing moves and ties
	if (P1move == 'Rock' and CPUmove == 'Scissors') or (P1move == 'Scissors' and CPUmove == 'Rock'):
		print()
		print('Player 1 chose: ' + P1move + ' and Game-Bot chose: ' + CPUmove)
		if P1move == 'Rock':
			print()
			print('You have outsmarted and beat Game-Bot! Why not prove yourself the victor once more? ')
		elif P1move == 'Scissors':
			print()
			print('You have been outsmarted and been beat by Game-Bot! Try again and try outsmart him this time! ')
		print()
		print('-'*65)

	elif (P1move == 'Scissors' and CPUmove == 'Paper') or (P1move == 'Paper' and CPUmove == 'Scissors'):
		print()
		print('Player 1 chose: ' + P1move + ' and Game-Bot chose: ' + CPUmove)
		if P1move == 'Scissors':
			print()
			print('You have outsmarted and beat Game-Bot! Why not prove yourself the victor once more? ')
		elif P1move == 'Paper':
			print()
			print('You have been outsmarted and been beat by Game-Bot! Try again and try outsmart him this time! ')
		print('-'*65)

	elif (P1move == 'Paper' and CPUmove == 'Rock') or (P1move == 'Rock' and CPUmove == 'Paper'):
		print()
		print('Player 1 chose: ' + P1move + ' and Game-Bot chose: ' + CPUmove)
		if P1move == 'Paper':
			print()
			print('You have outsmarted and beat Game-Bot! Why not prove yourself the victor once more? ')
		elif P1move == 'Rock':
			print()
			print('You have been outsmarted and been beat by Game-Bot! Try again and try outsmart him this time! ')
		print('-'*65)

	elif (P1move == 'Rock' and CPUmove == 'Rock'):
		print()
		print('You and your opponent both chose Rock which means it is a tie! Why not try again?')
		print('-'*65)

	elif (P1move == 'Paper' and CPUmove == 'Paper'):
		print()
		print('You and your opponent both chose Paper which means it is a tie! Why not try again?')
		print('-'*65)

	elif (P1move == 'Scissors' and CPUmove == 'Scissors'):
		print()
		print('You and your opponent both chose Scissors which means it is a tie! Why not try again?')
		print('-'*65)

	time.sleep(2)
	

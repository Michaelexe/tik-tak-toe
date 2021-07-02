import random

bot = 0
friend = 0
win = 0

board = """
      |      |      
      |      |      
______|______|______
      |      |      
      |      |      
______|______|______
      |      |      
      |      |      
      |      |      """

player1_markedlist = []
player2_markedlist = []

winning_possibilities = [
[1,2,3], [4,5,6], [7,8,9],
[1,4,7], [2,5,8], [3,6,9],
[1,5,9], [3,5,7]]

possible_win = []














def bot_input():
	global board
	global player1_markedlist
	global player2_markedlist
	global possible_win

	choice_true = True
	print("bot plays:")
	while choice_true:

		bot_choice = random.randint(1,9)
		if bot_choice not in player1_markedlist and bot_choice not in player2_markedlist:
			player2_markedlist.append(bot_choice)

			if bot_choice == 1:
				board = board[:24] + 'O' + board[25:]

			elif bot_choice == 2:
				board = board[:31] + 'O' + board[32:]

			elif bot_choice == 3:
				board = board[:38] + 'O' + board[39:]

			elif bot_choice == 4:
				board = board[:87] + 'O' + board[88:]
				
			elif bot_choice == 5:
				board = board[:94] + 'O' + board[95:]

			elif bot_choice == 6:
				board = board[:101] + 'O' + board[102:]

			elif bot_choice == 7:
				board = board[:150] + 'O' + board[151:]

			elif bot_choice == 8:
				board = board[:157] + 'O' + board[158:]

			elif bot_choice == 9:
				board = board[:164] + 'O' + board[165:]

			choice_true = False

		else:
			pass




def take_input1():
	global board
	global player1_markedlist
	global player2_markedlist
	global possible_win

	choice_true = True

	while choice_true:

		player1_choice = int(input('player 1, choose number corresponding to the block you want to mark:'))

		if player1_choice not in player1_markedlist and player1_choice not in player2_markedlist:
			player1_markedlist.append(player1_choice)

			if player1_choice == 1:
				board = board[:24] + 'X' + board[25:]

			elif player1_choice == 2:
				board = board[:31] + 'X' + board[32:]

			elif player1_choice == 3:
				board = board[:38] + 'X' + board[39:]

			elif player1_choice == 4:
				board = board[:87] + 'X' + board[88:]
				
			elif player1_choice == 5:
				board = board[:94] + 'X' + board[95:]

			elif player1_choice == 6:
				board = board[:101] + 'X' + board[102:]

			elif player1_choice == 7:
				board = board[:150] + 'X' + board[151:]

			elif player1_choice == 8:
				board = board[:157] + 'X' + board[158:]

			elif player1_choice == 9:
				board = board[:164] + 'X' + board[165:]

			choice_true = False

		else:
			print()
			print("the block you've chosen is already marked, try again")
			print()

	print(board)




def take_input2():
	global board
	global player1_markedlist
	global player2_markedlist
	global possible_win

	choice_true = True
	while choice_true:
		player2_choice = int(input('player 2, choose number corresponding to the block you want to mark:'))

		if player2_choice not in player1_markedlist and player2_choice not in player2_markedlist:
			player2_markedlist.append(player2_choice)

			if player2_choice == 1:
				board = board[:24] + 'O' + board[25:]

			elif player2_choice == 2:
				board = board[:31] + 'O' + board[32:]

			elif player2_choice == 3:
				board = board[:38] + 'O' + board[39:]

			elif player2_choice == 4:
				board = board[:87] + 'O' + board[88:]
				
			elif player2_choice == 5:
				board = board[:94] + 'O' + board[95:]

			elif player2_choice == 6:
				board = board[:101] + 'O' + board[102:]

			elif player2_choice == 7:
				board = board[:150] + 'O' + board[151:]

			elif player2_choice == 8:
				board = board[:157] + 'O' + board[158:]

			elif player2_choice == 9:
				board = board[:164] + 'O' + board[165:]

			choice_true = False

		else:
			print()
			print("the block you've chosen is already marked, try again")
			print()







	






















print('HOW TO PLAY:')
print()
print('=======================================================')
print('Typing the number selects the respective block on the board')
print("""
      |      |      
   1  |   2  |   3  
______|______|______
      |      |      
   4  |   5  |   6  
______|______|______
      |      |      
   7  |   8  |   9  
      |      |      """)
print()
print('=======================================================')
print()

option = True
while option:
	friend_or_bot = input("if you want to play with a friend, press 'f' \nif you want to play with a bot, press 'b':")

	if friend_or_bot == 'f':
		friend = 1
		option = False

	elif friend_or_bot == 'b':
		bot = 1
		option = False

	else:
		print("the option you have given didn't match, try again")





























while friend:
	print(board)

	take_input1() 

	for i in winning_possibilities:
		for x in i:
			if x in player1_markedlist:
				possible_win.append(x)
				if len(possible_win) == 3:
					print('PLAYER 1 WINS!')
					print(i)
					win = 1
					friend = 0


				else:
					pass
		possible_win = []

	if len(player1_markedlist) + len(player2_markedlist) == 9 and win != 1:
		print("It's a draw!")
		friend = 0

	while friend:

		take_input2()

		for i in winning_possibilities:
			for x in i:
				if x in player2_markedlist:
					possible_win.append(x)
					if len(possible_win) == 3:
						print(board)
						print('PLAYER 2 WINS!')
						print(i)
						win = 2
						friend = 0

					else:
						pass

			possible_win = []

		break

	if friend == 0:
		again = input("Play again? (y/n):")

		if again == "y":
			friend = 1

			board = """
      |      |      
      |      |      
______|______|______
      |      |      
      |      |      
______|______|______
      |      |      
      |      |      
      |      |      """

			player1_markedlist = []
			player2_markedlist = []
			win = 0

		else:
			pass






while bot:
	print(board)

	take_input1()

	for i in winning_possibilities:
		for x in i:
			if x in player1_markedlist:
				possible_win.append(x)
				if len(possible_win) == 3:
					print('PLAYER 1 WINS!')
					print(i)
					win = 1
					bot = 0


				else:
					pass
		possible_win = []

	if len(player1_markedlist) + len(player2_markedlist) == 9 and win != 1:
			print("It's a draw!")
			bot = 0

	while bot:

		bot_input()

		for i in winning_possibilities:
			for x in i:
				if x in player2_markedlist:
					possible_win.append(x)
					if len(possible_win) == 3:
						print(board)
						print('BOT WINS!')
						print(i)
						win = 2
						bot = 0

					else:
						pass

			possible_win = []

		break

	if bot == 0:
		again = input("Play again? (y/n):")

		if again == "y":
			bot = 1

			board = """
      |      |      
      |      |      
______|______|______
      |      |      
      |      |      
______|______|______
      |      |      
      |      |      
      |      |      """

			player1_markedlist = []
			player2_markedlist = []
			win = 0

		else:
			pass





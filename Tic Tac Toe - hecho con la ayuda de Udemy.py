#!/usr/bin/env python
# coding: utf-8

# # Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output

def display_board(board):
    #Limpiar tablero anterior
    print('\n'*3)
    #Mostrar tablero
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("   |   |   ")


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[85]:


test_board = ["_"," "," "," "," "," "," "," "," "," "]
display_board(test_board)
display_board(test_board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[2]:


def player_input():
    marker = ""
    players = ("","")
    
    #Solicita a jugador 1 seleccionar su ficha
    while marker != 'X' and marker != 'O':
        marker = input("Jugador 1 selecciona X ó O ")
        marker = marker.upper()
    
    #Asigna ficha
    player1 = marker
    if player1=='X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    players = (player1,player2)
    return players


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[68]:


player_input()


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[12]:


def place_marker(board, marker, position):
    board[position] = marker


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[64]:


place_marker(test_board,'X',8)
display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[5]:


def win_check(board, mark):
    
        if (board[1]==board[2]==board[3]==mark):
            return True
        elif (board[4]==board[5]==board[6]==mark):
            return True
        elif (board[7]==board[8]==board[9]==mark):
            return True
        elif (board[1]==board[4]==board[7]==mark):
            return True
        elif (board[2]==board[5]==board[8]==mark):
            return True
        elif (board[3]==board[6]==board[9]==mark):
            return True
        elif (board[1]==board[5]==board[9]==mark):
            return True
        elif (board[3]==board[5]==board[7]==mark):
            return True
        else:
            return False


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[88]:


win_check(test_board,'X')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[6]:


import random

def choose_first():
    
    randomizer = random.randint(0,1)
    #Si el resultado del numero random es 1 el jugador 1 inicia, si es 2 el jugador 2 parte.
    
    if(randomizer == 1):
        return 'Player 1'
    else:
        return 'Player 2'
    


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[7]:


def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False
    


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[8]:


def full_board_check(board):
    check = False
    for x in range(1,10):
        if board[x]== " ":
            check = True
    return not check


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[9]:


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Seleccione una posición (1-9): "))
        
    return position


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[18]:


def replay():
    
    choice = input("Quieres jugar otra vez? (S/N) ")
    choice = choice.upper()
    return choice == 'S'
    


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[ ]:


print('Welcome to Tic Tac Toe!')

#while True:
while True:
    
    # Set the game up here
    the_board = [" "]*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn+" irá primero")
    
    play_game = input("Listo para jugar? s/n").lower()
    if play_game == 's':
        game_on = True
    
    else:
        game_on = False
   

    while game_on:
        if turn == 'Player 1':
            #Player 1 Turn
            #Mostrar tablero
            display_board(the_board)
            #Elige posicion
            position = player_choice(the_board)
            #Fija la posicion
            place_marker(the_board, player1_marker, position)
            #Revisa si ganó
            if(win_check(the_board, player1_marker)):
                display_board(the_board)
                print("Gana el jugador 1")
                game_on = False
                
            else:
                #Revisa si empataron
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Empate")
                    game_on = False
                else:
                    turn = 'Player 2'
                    
        else:
            #Player 2 Turn
            #Mostrar tablero
            display_board(the_board)
            #Elige posicion
            position = player_choice(the_board)
            #Fija la posicion
            place_marker(the_board, player2_marker, position)
            #Revisa si ganó
            if(win_check(the_board, player2_marker)):
                display_board(the_board)
                print("Gana el jugador 2")
                game_on = False
                
            else:
                #Revisa si empataron
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Empate")
                    game_on = False
                else:
                    turn = 'Player 1'
        
            
            #pass

    if not replay():
        break


# ## Good Job!

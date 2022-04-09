
#imports
import os
from random import randint

#functions
def draw():
	screen.fill("gold")
	fox.draw()
	coin.draw()
	screen.draw.text("Score:" + str(score), color="black", topleft=(10, 10))

	if game_over:
		screen.fill("pink")
		screen.draw.text("final score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
	coin.x = randint(20, (WIDTH - 50))
	coin.y = randint(20, (HEIGHT - 50))

def update():
	global i
	global fox
	global score
	global coin
	if keyboard.left:
		fox.x = fox.x - SPEED
	elif keyboard.right:
		fox.x = fox.x + SPEED
	elif keyboard.up:
		fox.y = fox.y - SPEED
	elif keyboard.down:
		fox.y = fox.y + SPEED
	coin_collected = fox.colliderect(coin)

	if coin_collected:
		score = score + 10
		sounds.eat.play()
		if i <5:
			i = i + 1 
		fox = Actor("anant_faces/"+anant_list[i], fox.pos)
		coin = Actor("food/"+food_list[randint(0,6)])
		place_coin()	

def time_up():
	global game_over
	game_over = True

# variables
WIDTH = 400
HEIGHT = 400
PLAY_TIME = 40.0
score = 0
game_over = False
SPEED = 4
i = 0
anant_list = sorted(os.listdir('images/anant_faces'))

fox = Actor("anant_faces/"+anant_list[i])
fox.pos = 50, 50 

food_list = os.listdir('images/food')
coin = Actor("food/"+food_list[randint(0,6)])
coin.pos = 200, 200

# run
clock.schedule(time_up, PLAY_TIME)
place_coin()
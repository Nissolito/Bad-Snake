from time import sleep
from random import randint

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

def controlls():
	"""Returns the last character in a text file to be used as input"""
	with open("controlls.txt", "r", encoding="utf-8") as file:
		TextInput = file.read()
		print(TextInput[len(TextInput)-1])
	return TextInput[len(TextInput)-1]

def playbox(screenrows: list):
	"""Print the play area in the terminal"""
	print("[]"*(width+2))
	for i in screenrows:
		print("[]" + "".join(i) + "[]")
	print("[]"*(width+2))

def make_gamebox():
	"""Creates the play area for the game in the form of a two dimensional list"""
	return [
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
		["::","::","::","::","::","::","::","::","::","::","::","::"],
	]

gamebox = make_gamebox()
height = len(gamebox)
width = len(gamebox[0])
print(f"{height} x {width}")


fruit_pos_y, fruit_pos_x = 5, 9
pos_y, pos_x = 0, 0

fruit_head = f"{RED}\U0001FBE9\U0001FBEB{RESET}"
character_body = f"{GREEN}\U0001FBE9\U0001FBEB{RESET}"
character_head = f"{GREEN}\U0001FBE1\U0001FBE3{RESET}"

dir = 0
body_pos = []
body_len = 5
while True:
	gamebox = make_gamebox()
	print("\n"*10)
	if (pos_x,pos_y) in body_pos:
		break
	if (pos_y,pos_x) == (fruit_pos_y,fruit_pos_x):
			body_len += 1
			while True:
				try:
					fruit_pos_y = randint(0,11)
					fruit_pos_x = randint(0,11)
					for i in body_pos:
						if (fruit_pos_y,fruit_pos_x) == i:
							print(i)
							raise KeyError
							
					break
				except KeyError:
					pass
	gamebox[fruit_pos_y][fruit_pos_x] = fruit_head
	body_pos.append((pos_x,pos_y))
	if len(body_pos) >= body_len:
		body_pos.pop(0)
	
	for i in body_pos:
		if i == body_pos[len(body_pos)-1]:
			gamebox[i[1]][i[0]] = character_head
		else:
			gamebox[i[1]][i[0]] = character_body
	playbox(gamebox)
	print(f"Score: {body_len-5}")
	sleep(1.4)
	match controlls():
		case "d":
			if pos_x < width-1:
				pos_x += 1
				dir = 0
		case "a":
			if pos_x > 0:
				pos_x -= 1
				dir = 1
		case "w":
			if pos_y > 0:
				pos_y -= 1
				dir = 2
		case "s":
			if pos_y < height-1:
				pos_y += 1
				dir = 3
		case "1":
			print("QUITING...")
			sleep(0.3)
			break
		case _:
			pass

a_figure = {True: 'A', False: 'a'}
b_figure = {True: 'B', False: 'b'}
punch_figure = {
(True, True): '=',
(True, False): '_',
(False, True): ' ',
(False, False): ' '
}
gap_figure = {True: '    ', False: ''}
turn_a = True
gap = True
a_stand = True
b_stand = True
bot = False
a_pu = False
b_pu = False
life_a = 3
life_b = 3
a_act = None
b_act = None
a_act1 = None
a_act2 = None
b_act1 = None
b_act2 = None
a_foward_offensive = False
b_foward_offensive = False
a_hit = False
b_hit = False
a_jump = False
b_jump = False

#game loop
while life_a > 0 and life_b > 0:
	
	drawscreen()
	
	#if bot:
	if turn_a:
		a_act1, a_act2 = action_definer()
	else:
		b_act1, b_act2 = action_definer()
	if turn_a:
		a_act = a_act1
		b_act = b_act2
	else:
		a_act = a_act2
		b_act = b_act1
	
	a_foward_offensive, b_foward_offensive = forward_offensive_check()
	gap = gap_no_gap()
	up_down()
	colision()
	score()
	if hit:
		replace()
	
	turn_a = not turn_a
	a_jump = False
	b_jump = False

# ------------------------------
# functions

def drawscreen():
	print(a_figure[a_stand] + punch_figure[(a_pu, a_stand)] + gap_figure[gap] + punch_figure[(b_pu, b_stand)] + b_figure[b_stand])
	
	def inputs():
		return input()
	
	def action_definer(): #just takes player's choices
		if turn_a:
			if a_act2 = 1:
				a = 5
				b = inputs()
			else:
				a = inputs()
				if a == 1:
					b = 5
				else:
				b = inputs()
		else:
			if b_act2 = 1:
				a = 5
				b = inputs()
			else:
				a = inputs()
				if a == 1:
					b = 5
				else:
					b = inputs()
		return a, b
	
	def foward_offensive_check():
		if not gap:
			if a_act == 3 and b_act != 4:
				a = True
			else:
				a = False
			if a_act != 4 and b_act == 3:
				b= True
			else:
				b = False
			return a, b
		else:
			if a_act == 3 and b_act == 3:
				return (True, True)
			else:
				return (False, False)
	
	def gap_no_gap():
		if gap:
			if a_act == 3 and b_act != 4:
				return False
			elif a_act != 4 and b_act == 3:
				return False
			else:
				return True
		else:
			if a_act == 4 and b_act != 3:
				return True
			elif a_act != 3 and b_act == 4:
				return True
			return False

	def up_down():
		if a_act == 2:
			if a_stand:
				global a_stand = False
			else:
				global a_stand = True
				global a_jump = True
		if b_act == 2:
			if b_stand:
				global b_stand = False
			else:
				global b_stand = True
				global b_jump = True

	def colision():
		# foward offensive colision
		
			

#actions: 1: punch, 2:up or down, 3: foward, 4: back, 5: punch return
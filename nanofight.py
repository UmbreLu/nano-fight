

# ------------------------------
# functions
def draw_screen():
    """
Graphical part of the game.
    """
    if a_jump or b_jump:
        jump = True
    else:
        jump = False
    if gap:
        print(f'''Valid actions: 1-punch, 2-stand-up or stand-down, 3-step forward and 4-step back.
    
     Turn:{turn_count}    _____D_O_J_O______     A move: {actions.get(a_act, '')}
     A:{life_a}      |                  |    B move: {actions.get(b_act, '')}
     B:{life_b}      |     ''' + a_figure[a_stand] + punch_figure[(a_pu, a_stand)] + gap_figure[gap] + punch_figure[(b_pu, b_stand)] + b_figure[
            b_stand] + f'''     |    {jump_message[jump]}
              ^^^^^^^^^^^^^^^^^^^^''')
    else:
        print(f'''Valid actions: 1-punch, 2-stand-up or stand-down, 3-step forward and 4-step back.

             Turn:{turn_count}    _____D_O_J_O______     A move: {actions.get(a_act, '')}
             A:{life_a}      |                  |    B move: {actions.get(b_act, '')}
             B:{life_b}      |       ''' + a_figure[a_stand] + punch_figure[(a_pu, a_stand)] +
              punch_figure[(b_pu, b_stand)] + b_figure[
                  b_stand] + f'''       |    {jump_message[jump]}
                      ^^^^^^^^^^^^^^^^^^^^''')


def inputs():
    """
Handles inputs.
    :return: return handled input
    """
    while True:
        raw = int(input('> '))
        if raw in valid_inputs:
            return raw
        else:
            print('Invalid input.')


def action_definer():  # just takes player's choices
    """
This function asserts player inputs "properly" to the action queue (a_acts and b_acts) tanking in count that punch
actions takes 2 turns.
    :return:
    """
    if turn_a:
        print('A turn. Choose your actions.')
        if a_act2 == 1:
            a = 5
            b = inputs()
        else:
            a = inputs()
            if a == 1:
                b = 5
            else:
                b = inputs()
    else:
        print('B turn. Choose your actions.')
        if b_act2 == 1:
            a = 5
            b = inputs()
        else:
            a = inputs()
            if a == 1:
                b = 5
            else:
                b = inputs()
    return a, b


def forward_offensive_check():
    """
This function checks if there is a forward offensive as an additional consequence of a forward action of the combatants.
    :return: True or False for if forward offensive exists for a and/or b.
    """
    if not gap:
        if a_act == 3 and b_act != 4:
            a = True
        else:
            a = False
        if a_act != 4 and b_act == 3:
            b = True
        else:
            b = False
        return a, b
    else:
        if a_act == 3 and b_act == 3:
            return True, True
        else:
            return False, False


def gap_no_gap():
    """
This function determines if the combatants are close or far from each other.
    :return: True or False.
    """
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
    """
This function handles the up/down states of the combatants in accord to their commands.
    :return: True or False for stand states of each combatant.
    """
    global a_stand
    global a_jump
    global b_stand
    global b_jump
    if a_act == 2:
        if a_stand:
            a_stand = False
        else:
            a_stand = True
            a_jump = True
    if b_act == 2:
        if b_stand:
            b_stand = False
        else:
            b_stand = True
            b_jump = True


def collision():
    """
This function handles all collisions.
    :return: True of False for collisions.
    """
    global a_punches_b
    global b_punches_a
    global a_stomps_b
    global b_stomps_a

    # punch collision
    if not gap:
        if a_stand and b_stand:
            if a_act == 1:
                a_punches_b = True
                print('a punches b')
            if b_act == 1:
                b_punches_a = True
                print('b punches a')
        elif not a_stand and b_stand and not b_jump:
            if a_act == 1:
                a_punches_b = True
                print('a punches b')
        elif a_stand and not b_stand and not a_jump:
            if b_act == 1:
                b_punches_a = True
                print('b punches a')
        elif not a_stand and not b_stand:
            if a_act == 1:
                a_punches_b = True
            if b_act == 1:
                b_punches_a = True

    # forward collision
    if not a_punches_b and not b_punches_a:
        if not gap:
            if a_stand and not b_stand and a_forward_offensive:
                a_stomps_b = True
            if not a_stand and b_stand and b_forward_offensive:
                b_stomps_a = True


def score():
    """
This function updates game score after collisions.
    """
    global life_a
    global life_b

    if a_punches_b:
        life_b -= 1
    if b_punches_a:
        life_a -= 1
    if a_stomps_b:
        life_b -= 1
    if b_stomps_a:
        life_a -= 1


def replace():
    """
This function replace combatants if there is any collision, even after gap_no_gap function have already taken place
inside the round loop.
    """
    global gap
    global message
    if a_punches_b or b_punches_a:
        punch_collision = True
    else:
        punch_collision = False
    if a_stomps_b or b_stomps_a:
        forward_collision = True
    else:
        forward_collision = False
    if punch_collision or forward_collision:
        gap = True

# actions: 1: punch, 2:up or down, 3: forward, 4: back, 5: punch return

# -----------------------------------------------
# global variables and constant values


jump_message = {True: 'Jump!', False: ''}
actions = {1: 'Punch', 2: 'Stand up or down', 3: 'Step forward', 4: 'Step back', 5: 'Punch recovery'}
valid_inputs = {1, 2, 3, 4, 5}
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
b_stand = False
# bot = False
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
a_forward_offensive = False
b_forward_offensive = False
a_hit = False
b_hit = False
a_jump = False
b_jump = False
a_punches_b = False
b_punches_a = False
a_stomps_b = False
b_stomps_a = False
turn_count = 0
message = ''

# -----------------------------------------------------
# game loop
while life_a > 0 and life_b > 0:

    draw_screen()

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
    if a_act == 1:
        a_pu = True
    else:
        a_pu = False
    if b_act == 1:
        b_pu = True
    else:
        b_pu = False

    a_forward_offensive, b_forward_offensive = forward_offensive_check()
    gap = gap_no_gap()
    up_down()
    collision()
    score()
    replace()

    turn_a = not turn_a
    a_jump = False
    b_jump = False
    a_punches_b = False
    b_punches_a = False
    a_stomps_b = False
    b_stomps_a = False
    turn_count += 1

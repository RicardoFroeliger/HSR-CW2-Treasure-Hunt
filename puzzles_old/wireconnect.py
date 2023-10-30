import os
import random

wires = []
colors = {
    'RED': '\033[0;31;40m',
    'GREEN': '\033[0;32;40m',
    'YELLOW': '\033[0;33;40m',
    'BLUE': '\033[0;34;40m',
    'MAGENTA': '\033[0;35;40m',
    'CYAN': '\033[0;36;40m',
    # 'BOLD_RED': '\033[1;31;40m',
    # 'BOLD_GREEN': '\033[1;32;40m',
    # 'BOLD_YELLOW': '\033[1;33;40m',
    # 'BOLD_BLUE': '\033[1;34;40m',
    # 'BOLD_MAGENTA': '\033[1;35;40m',
    # 'BOLD_CYAN': '\033[1;36;40m',
}
color_end = '\033[0m'

def wireconnect(wires_quantity: int = None, message: str = None, selected_left_wire: dict = None, game_active: bool = True):
    global wires

    # clear console
    os.system('cls' if os.name == 'nt' else 'clear')

    # generate wires or print message
    if wires_quantity:
        generate_wires(wires_quantity)
        game_active = True
    elif message:
        print(message + ('\n' if game_active else ''))

    # handle exit
    if not game_active:
        return

    # get the wires that are not connected, sort by right id for possible swapped wires
    not_connected_wires = [x for x in wires if x['left_connected'] is False and x['right_connected'] is False]
    not_connected_wires = sorted(not_connected_wires, key=lambda k: k['right_id'])

    # print wires
    for wire in enumerate(not_connected_wires):
        left_wire = sorted(not_connected_wires, key=lambda k: k['position_left'])[wire[0]]
        right_wire = wire[1]

        print(
            f'{left_wire["left_id"]}{" " if len(str(left_wire["left_id"])) > 1 else "  "}' +
            f'|{colors[left_wire["color"]]}=========={color_end}x   ' +
            f'x{colors[right_wire["color"]]}=========={color_end}| {right_wire["right_id"]}'
        )

    # get left wire input if not selected
    if selected_left_wire:
        print(f'\nSelected left wire: {selected_left_wire}')
        left_wire_input = selected_left_wire
    else:
        # validate left wire input
        left_wire_input = input('\nEnter the position of LEFT wire you want to select or type "exit" to exit the game: ')
        if left_wire_input.isdigit() and int(left_wire_input) in [x['left_id'] for x in not_connected_wires]:
            left_wire_input = int(left_wire_input.strip())
            message = None
            selected_left_wire = left_wire_input

        # validate exit
        elif left_wire_input.lower() == 'exit':
            message = 'Successfully exited the game'
            game_active = False

        # retry if left wire input is invalid
        else:
            message = 'The position of the LEFT wire you entered is invalid (must be a number in the list of LEFT wires)'

        # return so right wire input is not triggered more than once after left wire had an invalid input
        return wireconnect(message = message, selected_left_wire = selected_left_wire, game_active = game_active)

    # get & validate right wire input
    right_wire_input = input('Enter the position of RIGHT wire you want to select or type "exit" to exit the game: ')
    if right_wire_input.isdigit() and int(right_wire_input) in [x['right_id'] for x in not_connected_wires]:
        right_wire_input = int(right_wire_input.strip())
    else:
        # validate exit
        if right_wire_input.lower() == 'exit':
            message = 'Successfully exited the game'
            game_active = False

        # retry if right wire input is invalid
        else:
            message = 'The position of the RIGHT wire you entered is invalid (must be a number in the list of RIGHT wires)'
            selected_left_wire = left_wire_input

        # return so left_wire & right_wire are not set until right wire input is valid
        return wireconnect(message = message, selected_left_wire = selected_left_wire, game_active = game_active)

    # get left wire
    left_wire = [x for x in wires if x['left_id'] == left_wire_input][0]
    right_wire = [x for x in wires if x['right_id'] == right_wire_input][0]

    # check if left wire and right wire are the same color
    if left_wire['color'] == right_wire['color']:
        left_wire['left_connected'] = True
        right_wire['right_connected'] = True

        # check if left wire and right wire dont belong to the same wire dictionary
        if not left_wire['left_connected'] or not left_wire['right_connected']:

            # set left wire left/right connected to true, set right wire left/right connected to false
            left_wire['left_connected'] = True
            left_wire['right_connected'] = True
            right_wire['left_connected'] = False
            right_wire['right_connected'] = False

            # swap left wire right id with right wire right id
            right_wire_right_id = right_wire['right_id']
            right_wire['right_id'] = left_wire['right_id']
            left_wire['right_id'] = right_wire_right_id

        # check if all wires are connected
        if all([x['left_connected'] and x['right_connected'] for x in wires]):
            message = 'All wires have successfully been connected!'
            game_active = False
        else:
            message = f'Successfully connected wire {left_wire_input} to {right_wire_input}'
    else:
        message = 'Failed to connect the wires, the colors of the selected wires don\'t match'

    wireconnect(message = message, game_active = game_active)


def generate_wires(wires_quantity: int):
    global wires
    existing_colors = []

    # generate wires by left position
    for i in range(wires_quantity):

        # generate random color with as less repeating colors as possible
        wirecolors = [x for x in list(dict.keys(colors)) if x not in existing_colors]
        wirecolor = random.choice(wirecolors)

        if len(existing_colors) < len(colors) - 1:
            existing_colors.append(wirecolor)
        else:
            existing_colors = []

        # append wire
        wires.append({
            'color': wirecolor,
            'left_id': i + 1,
            'position_left': i + 1,
            'left_connected': False,
            'right_connected': False
        })

    # shuffle wires & set right position
    random.shuffle(wires)
    for i in range(len(wires)):
        wires[i]['position_right'] = i + 1
        wires[i]['right_id'] = wires_quantity + i + 1
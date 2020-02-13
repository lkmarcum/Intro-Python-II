from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'coin': Item("coin")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['foyer'].items.append(items['coin'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# p = Player("Player 1", room["outside"])
p = Player(input("Enter your name:  "), room['outside'])

# Write a loop that:
print(p.current_room)
choices = ["n", "s", "e", "w"]

while True:
    #
    # * Prints the current room name
    # print(f"\n{p.current_room.name}")

    # * Prints the current description (the textwrap module might be useful here).
    # print(p.current_room.description, "\n")

    # * Waits for user input and decides what to do.
    cmd = input("Enter a command.\n").split()

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if len(cmd) == 1:
        if cmd[0] in choices:
            p.travel(cmd[0])
        elif cmd[0] == 'i' or cmd[0] == "inventory":
            print("Inventory:")
            for i in p.items:
                print(i.name)
        elif cmd[0] == 'q':
            print("\nGoodbye.")
            break
        else:
            print("Command not recognized.")
    elif len(cmd) == 2:
        if cmd[0] == "get" or cmd[0] == "take":
            if cmd[1] in items.keys() and items[cmd[1]] in p.current_room.items:
                items[cmd[1]].on_take()
                p.current_room.items.remove(items[cmd[1]])
                p.items.append(items[cmd[1]])
            else:
                print(f"There is no {cmd[1]} in this room.")
        elif cmd[0] == "drop":
            if items[cmd[1]] in p.items:
                items[cmd[1]].on_drop()
                p.current_room.items.append(items[cmd[1]])
                p.items.remove(items[cmd[1]])
        else:
            print("Command not recognized.")
    else:
        print("Command not recognized.")

    # if cmd == 'n':
    #     if p.current_room.n_to == None:
    #         print(
    #             "\nThere is no path here. Please choose another direction: n, s, e, or w (q to quit)")
    #     else:
    #         p.current_room = p.current_room.n_to

    # elif cmd == 's':
    #     if p.current_room.s_to == None:
    #         print(
    #             "\nThere is no path here. Please choose another direction: n, s, e, or w (q to quit)")
    #     else:
    #         p.current_room = p.current_room.s_to

    # elif cmd == 'e':
    #     if p.current_room.e_to == None:
    #         print(
    #             "\nThere is no path here. Please choose another direction: n, s, e, or w (q to quit)")
    #     else:
    #         p.current_room = p.current_room.e_to

    # elif cmd == 'w':
    #     if p.current_room.w_to == None:
    #         print(
    #             "\nThere is no path here. Please choose another direction: n, s, e, or w (q to quit)")
    #     else:
    #         p.current_room = p.current_room.w_to

    # If the user enters "q", quit the game.
    # elif cmd == 'q':
    #     print("\nGoodbye.")
    #     break

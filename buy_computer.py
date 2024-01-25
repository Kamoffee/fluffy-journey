# available_parts = ["computer",
#                    "monitor",
#                    "keyboard",
#                    "mouse",
#                    "mouse mat",
#                    "hdmi cable",
#                    "dvd drive"
#                    ]
# #valid_choices = [str(i) for i in range(1, len(available_parts) +1)] one way to do it
# valid_choices = []
# for i in range(1, len(available_parts) + 1):
#     valid_choices.append(str(i))
# print(valid_choices)
# current_choice = "-"
# computer_parts = [] #create an empty list
#
# while current_choice != '0':
#     if current_choice in valid_choices:
#         print("Adding {}".format(current_choice))
#         index = int(current_choice) - 1
#         chosen_part = available_parts[index]
#         computer_parts.append(chosen_part)
    # if current_choice in "1234567":
    #     print("Adding {}".format(current_choice))
    #     if current_choice == '1':
    #         computer_parts.append("computer")
    #     elif current_choice == '2':
    #         computer_parts.append("monitor")
    #     elif current_choice == '3':
    #         computer_parts.append("keyboard")
    #     elif current_choice == '4':
    #         computer_parts.append("mouse")
    #     elif current_choice == '5':
    #         computer_parts.append("mouse mat")
    #     elif current_choice == '6':
    #         computer_parts.append("hdmi")
    #     elif current_choice == '7':
    #         computer_parts.append("dvd drive")
    # else:
    #     print("Please add options from the list bellow:")
    #     for number, part in enumerate(available_parts):
    #         print("{0}: {1}".format(number + 1, part))
        # for part in available_parts:
        #     print("{0}: {1}".format(available_parts.index(part) +1, part))

        # print("1: computer") these are being replaced with the line above
        # print("2: monitor")
        # print("3: keyboard")
        # print("4: mouse")
        # print("5: mouse mat")
        # print("6: hdmi cable")
        # print("0: to finish")

#     current_choice = input()
#
# print(computer_parts)

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"
                   ]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] #create an empty list
available_parts.sort()

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            #it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list bellow:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)

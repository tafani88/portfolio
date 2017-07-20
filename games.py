start = '''
You wake up one morning with a a startle from your mother running into your room. she tells you that your grandmother is ill and needs medicine in order to get better. \
Your mission is now to retrieve your grandma's medicine and deliver it to her by the end of the night.
You're now in the middle of the woods.
A sign is hanging from the ivy: "There are two paths in front of you. which way do you want to go? Left or Right?"
'''

left = '''
You go left and as you go farther down the path you become hungry. you see these little berries
along your journey. you debate how hungry you are because you are not sure if they are safe to eat.
But you eat them anyways. An hour passes by and you start hallucinating. As time goes on and
on you become more weary and weaker. you then realize that eating those berries was not safe and
that they may have been poisonous. another conflict arises. you have the choice to either keep going
or sleep it off overnight in the woods.'''

keep_going = '''you make it to your grandmas house in time to hand her the medicine.
however, you die by
the end of the night.'''
sleep_it_off = '''after eating the poisonous berries, you decide its best to sleep
it off in the woods for just one night. if you chose to sleep it off, then you would
have wasted a whole night to make it to your grandma's house. by the time you get there in
the morning, you find out she already died and you were too late.'''


right = '''you go right and as you farther down the path you come by a lake. you are a
little tired, so you sit next to the lake for ten minutes.as your resting you feel an
aggressive pressure on your left upper arm. you find a next next to you and your arm
covered in blood. the snake has bitten you. another conflict arises. you have the choice to
either use your grandmothers medicine or not to use it and leave it for her.'''

Use_it = '''you drink it and your are healthier again. But then your grandma dies by the end
of the night because she had no other medicine to save her.'''
dont_use_it = '''by the time you get home you have lost an arm and a
leg because the posion has spread throughout your body. on the bright side, your grandmother
is saved and is healthy again'''

print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()


if user_input == "left":
    print(left)
    print("Type 'keep going'to keep going or type 'Sleep it off' to sleep it off")
    user = input()

if user_input == "keep_going":
    print(keep_going)
    user_input = input()
elif user_input == "sleep it off":
    print(sleep_it_off)


elif user_input == "right":
    print(right)
    print("Type 'use it' to use the medicine or type 'done use it' to not use the medicine")
    user_input = input()

    if user_input =="Use_it":
        print(use_it)
    elif user_input == "dont use it":
        print(dont_use_it)

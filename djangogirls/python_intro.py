
volume = 90
if volume < 20 or volume > 80:
    print("That's better!")

def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi_with_name(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi_with_name("anonymous")

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)
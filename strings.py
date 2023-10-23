message = 'Hello World! :)'

message2 = """bobby es un
chico malo"""

print(message)
print(len(message2))

# prints the letter on said index
print(message[0])


# prints the letters between said indexs without the last index
print(message[0:5])

# prints the letters between said indexs without the last index
# without start index know its from the index0
print(message[:5])

# prints the letters between said indexs without the last index
# without end index know its to the last index
print(message[5:])

print(message.lower())
print(message.upper())

print(message.count('hello'))
print(message.count('l'))

print(message.find('World'))

# returns -1 if not exists
print(message.find('babrie'))

new_message = message.replace('World', 'Universe')
message = message.replace('World', 'Universe')
print(new_message)
print(message)


greeting = 'Hello'
name = 'Gaalpos'

#Different ways to format text
message = greeting +', '+ name + '. Welcome'

print(message)

message = '{}, {}. Welcome'.format(greeting, name)
print(message)

message = f'{greeting}, {name}. Welcome'
print(message)

message = f'{greeting}, {name.upper()}. Welcome'
print(message)

print(dir(name))
print(help(str))
print(help(str.lower))
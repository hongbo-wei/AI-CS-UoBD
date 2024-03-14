# A class of Caesar cypher objects, each of which is
# a machine that can be used for encoding and decoding
# text strings using the Caesar cypher system
# Each character in the plain text string must be drawn
# from the alphabet given below, and will be encoded as a
# different character from the same alphabet

class Caesar():
    alphabet = "abcdefghijklmnopqrstuvwxyz .,"

    def __init__(self, shift):
        # initialises a Caesar object by setting the number of
        # positions it will shift each character to the right
        # when the character is encoded
        self.shift = shift

    def encode(self, char):
        # Method to encode a single character

        position = Caesar.alphabet.index(char)
        newpos = position + self.shift

        if newpos >= len(Caesar.alphabet):
            # this means the new position is 'off the right hand end'
            # of the alphabet, so it needs to be 'wrapped around'
            # to the left hand end
            newpos = newpos - len(Caesar.alphabet)

        newchar = Caesar.alphabet[newpos]
        return newchar

    def decode(self, char):
        # Method to decode a single character

        position = Caesar.alphabet.index(char)
        newpos = position - self.shift

        if newpos < 0:
            # this means the new position is 'off the left hand end'
            # of the alphabet, so it needs to be 'wrapped around' to
            # the right hand end
            newpos = newpos + len(Caesar.alphabet)

        newchar = Caesar.alphabet[newpos]
        return newchar

machine = Caesar (4)

cyphertext = "lipps"

plaintext = ""

for c in cyphertext :
    d = machine.decode (c)
    plaintext = plaintext + d

a = machine.encode (machine.encode ("f"))

b = machine.encode (machine.encode ("p"))

# After executing all of the code above

# What is the value of machine.encode("i")?

# What is the value of machine.encode("z")?

# What is the value of machine.encode ("A")?

# What is the value of machine.encode (machine.encode ("g")) ?

# What is the value of machine.decode (machine.encode ("f")) ?

# What is the value of machine.encode (machine.decode ("p")) ?


# What is the value of machine.shift ?

# How many times will the body of the for loop be executed?

# What is the value of c on the first iteration of the for loop?

# What is the value of d on the last iteration of the for loop?

# What is the value of the variable plaintext after the program has finished executing?
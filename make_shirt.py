# 3- (Try it yourself) Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#    The function should print a sentence summarizing the size of the shirt and the message printed on it.
#    Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# 4- (Try it yourself) Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
#   Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(message_text, size='large'):
    """that prints a size and the text of a given message"""
    print(f'The size of the shirt is {size} and the text message is "{message_text}"')

text = input("What is the text on the shirt? ")
make_shirt(text)
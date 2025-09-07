# given a string containing just the characters

# (    )     {       }        [       ]

# determine  if the input string is valid

# A string is valid if :


# Open brackets are closed by the same type of brackets 

# Open brackets are closed by the correct order


# like: (  {  [  ]  }  )    output: true 

# like: (  {  )  ]    output: false 


# intuition: checking open close           
# we scan one by one
# if its a open bracket stack.append(ch)
# if its not a openning bracket then the stack must have something , we will check if it has someting
# what it means if id doesnt have anything ? it means we have a closing bracket(in about to enter thing) 
# without an opening bracket return false
# now the under case within the else is that the stack has something
# we will pop it and check if it matches the closing bracket(in about to enter thing)
# important we used dictionary to map the closing and opening brackets

def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        else:
            if not stack:
                return False
            top_element = stack.pop()
            if mapping[ch] != top_element:
                return False

    return not stack

# so main line is mapping[ch] != top_element:
# map was used to map the closing and opening brackets
# map[ch] gives corresponding opening bracket for the closing bracket ch
# if it is not equal to the top element of the stack return false
# so thing to remember is make dictionary to map closing and opening brackets
# and use stack to keep track of opening brackets
# and when you encounter closing bracket check if stack is not empty
# if it is empty return false
# if it is not empty pop the top element and check if it matches the closing bracket(through map)
# if it does not match return false
# one more thing order of mapping is important i.e first round then curly then square
# also in loop we check if ch in mapping.values() i.e if it is opening bracket
# if it is opening bracket we append it to stack
# again we checked if its opening bracket through mapping.values()
# if it is not opening bracket then it must be closing bracket
# closing + stack empty = false 
# why? because closing bracket without opening bracket is invalid
# a case like this )(
# anoter case like this (])
# if we dry run this code on (])
# first ( is opening bracket so stack = ['(']
# then ] is closing bracket so stack is not empty we pop the top element which is (
# now we check if mapping[']'] != '('
# mapping[']'] is '[' so it is not equal to '(' so return false

# another dry run on ( { [ ] } )
# first ( is opening bracket so stack = ['(']
# then { is opening bracket so stack = ['(', '{']
# then [ is opening bracket so stack = ['(', '{', '[']
# then ] is closing bracket so stack is not empty we pop the top element which is [
# now we check if mapping[']'] != '['
# mapping[']'] is '[' so it is equal to '[' so continue
# now stack = ['(', '{']
# then } is closing bracket so stack is not empty we pop the top element which is {
# now we check if mapping['}'] != '{'
# mapping['}'] is '{' so it is equal to '{' so continue
# now stack = ['(']
# then ) is closing bracket so stack is not empty we pop the top element which is ( 
# now we check if mapping[')'] != '('
# mapping[')'] is '(' so it is equal to '(' so continue
# now stack = []
# at the end we return not stack which is True because stack is empty

        
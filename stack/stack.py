#!/usr/bin/python2

###############################################################################
## Stack class
###############################################################################
class Stack:
   def __init__(self):
      self.items = []

   ############################################################################
   ## Check if stack is empty
   ## 
   ############################################################################
   def is_empty(self):
      return not self.items

   ############################################################################
   ## Push an item to Stack
   ##
   ## @param item item to push to stack
   ############################################################################
   def push (self, item):
      self.items.append(item)

   ############################################################################
   ## Pop the top item op Stack
   ##
   ## @return the top item from Stack
   ##
   ## @remarks Stack is modified
   ############################################################################
   def pop (self):
      if (not self.is_empty()):
	  return self.items.pop()

   ############################################################################
   ## Retrieve the top item op Stack
   ##
   ## @return the top item from Stack
   ##
   ## @remarks Stack is not
   ############################################################################
   def top (self):
      if (not self.is_empty()):
	  return self.items[len(self.items) - 1]

   ############################################################################
   ## Get size of Stack
   ## 
   ############################################################################
   def size(self):
      return len(self.items)

###############################################################################
## Program to test Stack
###############################################################################
if __name__ == "__main__":
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')
    s.push('d')
    while not s.is_empty():
        print(s.pop())


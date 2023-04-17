# making sure the package works via imports 

from myLib.datastructures.Linear.SLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
from myLib.datastructures.Trees import *

from myLib.tests import *


# Create a linked list
my_list = SinglyLinkedList()
my_list.InsertHead(SNode(3))
my_list.InsertHead(SNode(2))
my_list.InsertHead(SNode(1))

# Print the linked list
#print(my_list.head.data)

new = AVL()

new.Insert(5)
new.Insert(6)
new.Insert(8)

new.printBF()


# Output:
# 1 -> 2 -> 3 -> None

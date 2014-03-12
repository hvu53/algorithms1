prolem = '''children game - hot potatoes: children line up in a circle and pass an item from neighbor
to neighbor as fast as they can. At a certain point in the game, the action is stopped and the child
who has the item (the potato) is removed from the circle. Play continues until only one child is left'''

from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
   simqueue = Queue()
   for name in namelist:
      simqueue.enqueue(name)

   while simqueue.size() > 1:
      for i in range(num):
         simqueue.enqueue(simqueue.dequeue())

      simqueue.dequeue()

   return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

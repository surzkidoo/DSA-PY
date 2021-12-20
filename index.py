from pylearn import Queue
qs=Queue()
qs.enqueue(8)
qs.enqueue(4)
qs.dequeue()
print(qs)
import queue

q = queue.PriorityQueue()

q.put((1, 1, 'first_in'))
q.put((1, 2, 'last_in'))
q.put((2, 1, 'not_to_be_returned'))

for i in range(q.qsize()):
    print(q.get(i))

q.put((1, 0, 'first_in'))
q.put((1, -1, 'last_in'))
q.put((1, -4, 'not_to_be_returned'))
q.put((1, -5, 'not_to_be_returned'))
q.put((2, -2, 'not_to_be_returned'))
q.put((2, -3, 'not_to_be_returned'))

for i in range(q.qsize()):
    print(q.get(i))


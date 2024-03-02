import heapq

input = [
    [9, 12],
    [8, 14],
    [12, 13],
    [10, 11]
]

# sort the input
heapq.heapify(input)

# flip and add first element to priorityQueue
priority_queue = []
priority_queue.append([input[0][1], input[0][0]])
# loop the input
for meet in input[1:]:
    # if end time of input is >= top elemenet of priority queue
    if meet[0] >= priority_queue[0][0]:
        # remove top element from priorityQueue
        # add input to priorityQueue
        heapq.heapreplace(priority_queue, meet)
    else:
        heapq.heappush(priority_queue, meet)

# return size of priorityQueue
room = len(priority_queue)
print(f"{room} room(s) are needed.")
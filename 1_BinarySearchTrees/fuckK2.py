from queue import PriorityQueue

my_pq = PriorityQueue()

my_pq.put((1,"Vivek"))
my_pq.put((1,"Ankit"))
my_pq.put((2,"Shivraj"))

while my_pq.empty() != True:
    prio,val = my_pq.get()
    print(val)
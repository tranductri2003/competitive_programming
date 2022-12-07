from queue import PriorityQueue
from collections import deque
from collections import OrderedDict
from collections import defaultdict
a=deque()
a=PriorityQueue()
a.put((1,"Thuong"))
a.put((2,"Tri"))
a.put((3,"Tinh yeu"))
a.put((-12123,"fuck"))
while not a.empty():
    so=a.get()
    print(so[0],     so[1])
    
a={}
a[5]=12123
a[6]=1212123
a[7]=121212
for num in a:
    print(num,a[num])
    
b=defaultdict(lambda:0)
print(b[5])
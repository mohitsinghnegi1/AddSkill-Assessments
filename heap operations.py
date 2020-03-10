print "enter array "
a=map(int,raw_input().split())
heap=[0]
def build_heap(heap,x):
    pos=len(heap)
    heap.append(x)
    while(pos>0):
        if(pos/2>0 and heap[pos/2]>heap[pos]):
            heap[pos/2],heap[pos]=heap[pos],heap[pos/2]
        else:
            break
        pos=pos/2
def heapify(heap):
    i=1
    while(i<len(heap)):
        flag=False
        if(i*2 < len(heap) and heap[i*2]<heap[i]):
            heap[i*2],heap[i]=heap[i],heap[i*2]
            i=i*2
            flag=True
        if(i*2+1<len(heap) and heap[i*2+1]<heap[i]):
            heap[i*2+1],heap[i]=heap[i],heap[i*2+1]
            i=i*2+1
            flag=True
        if(not flag):
            break
        #print heap
        

def remove_min(heap):
    min1=heap[1]
    heap[1]=heap[-1]
    
    heap.pop()
    #print heap
    heapify(heap)

for x in a:
    build_heap(heap,x)
print heap
remove_min(heap)          
print heap


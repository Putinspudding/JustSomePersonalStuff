wait=[]
def fifo(mem,wait,num):
	count=0
	for i in wait:
		if i in mem:
			continue
		mem.append(i)
		if(len(mem)>num):
			mem.pop(0)
			count=count+1
		print(mem)
	print((float(count)+num)/len(wait))

request = [2,3,2,1,5,2,4,5,3,2,5,2]
mem=[]
fifo(mem,request,3)

#taking 5 integers as input from user
val=[0,0,0,0,0]
for y in range(5):
	val[y]=int(input())
#the required index of integers
index = [0,0,0,0,0]
#to make sure that used_val does not contain any integer from val
max=min(val)
used_val = [max-1,max-1,max-1,max-1,max-1]
#finding the unrepeated max integer
for x in range(5):
	max=min(val)
	for i in range(5):
		if(max<val[i] and val[i] not in used_val):
			max=val[i]
#rearranging val integers into used_val from max to min with their index stored
	for j in range(5):
		if(max==val[j]):
			index[x]=j
			used_val[x]=max
#output
print("\n",used_val,"\n",index)

import time

count = 0
sum = 0
start = time.time()
while (count < 1000000):
	count = count +1
	sum = sum + count
	# print(sum)
end = time.time()
print(end-start)

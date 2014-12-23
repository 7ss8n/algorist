# Code for the exercises in Goodrich, Tamassia, Goldwasser's 
# book on data structures and algorithms in Python


# REINFORCEMENT

# R-1.1
def is_multiple(n, m):
	return n % m == 0

# R-1.2
def even(k):
	return is_multiple(k, 2)

# R-1.3
def minmax(data):
	ans_min, ans_max = data[0], data[0]
	for itm in data:
		if itm > ans_max:
			ans_max = iym
		if itm < ans_min:
			ans_min = itm
	return ans_min, ans_max

# R-1.4
def funny_sum(n):
	ans = 0
	i = 0
	while i < n:
		ans += i * i
		i += 1
	return ans

# R-1.5
def short_funny_sum(n):
	return sum([i * i for i in xrange(n)])

# R-1.6
def sum_odds(n):
	ans = 0
	i = 0
	while i < n:
		if i % 2 == 1:
			ans += i * i
		i += 1
	return ans

# R-1.7
def short_sum_odds(n):
	return sum([i * i for i in xrange(n) if i % 2 == 1])

# R-1.8
def negative_index():
	data = list(xrange(100))
	for i in xrange(1, 100):
		assert data[100 - i], data[-i]

# R-1.9
def sequence_1():
	print range(50, 90, 10)

# R-1.10
def sequence_2():
	print range(8, -9, -2)

# R-1.11
def sequence_3():
	print [2 ** i for i in range(9)]

sequence_3()

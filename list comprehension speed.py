import random
import time

def speed_checker(n):

	while n > 0:

		# 리스트 컴프리헨션
		start_time = time.time()
		ten_scores = [(random.randint(1,100), random.random()) for num in range(1000000)]
		end_time = time.time()

		print("리스트 컴프리헨션 타임: ", end_time - start_time, " 초" )

		# 루프

		ten_scores = []

		start_time = time.time()
		for ind in range(1000000):
			val_1 = random.randint(1,100)
			val_2 = random.random()
			ten_scores.append((val_1, val_2))
		end_time = time.time()
	
		print("루프 타임: ", end_time - start_time, " 초" )

		n -= 1

speed_checker(5)
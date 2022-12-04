def solution_pt1() -> int:
	with open('input.txt') as f:
		lines = f.readlines()

	calories_arr = []
	curr_cals = 0

	for line in lines:
		if line == '\n':
			calories_arr.append(curr_cals)
			curr_cals = 0
		else:
			curr_cals += int(line)

	return max(calories_arr)

def solution_pt2() -> int:
	with open('input.txt') as f:
		lines = f.readlines()

	calories_arr = []
	curr_cals = 0

	for line in lines:
		if line == '\n':
			calories_arr.append(curr_cals)
			curr_cals = 0
		else:
			curr_cals += int(line)

	calories_arr.sort()
	return sum(calories_arr[-3:])

if __name__ == "__main__":
	print(solution_pt1())

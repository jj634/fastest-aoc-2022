from helpers import get_data

def solution_pt1_impl(data):
	elf_list = data.split("\n\n")
	max_elf = 0
	for elf in elf_list:
		curr_total = sum([int(calorie) for calorie in elf.split("\n")])
		max_elf = max(max_elf,curr_total)
	return max_elf

def solution_pt2_impl(data):
	elf_list = data.split("\n\n")
	top_three = [0,0,0]
	for elf in elf_list:
		curr_total = sum([int(calorie) for calorie in elf.split("\n")])
		if curr_total > top_three[2]:
			top_three.pop(0)
			top_three.insert(2,curr_total)
		elif curr_total > top_three[1]:
			top_three.pop(0)
			top_three.insert(1,curr_total)
		elif curr_total > top_three[0]:
			top_three.pop(0)
			top_three.insert(0,curr_total)
	return top_three

def solution_pt1() -> int:
	return solution_pt1_impl(get_data())

def solution_pt2() -> int:
	return solution_pt2_impl(get_data())

if __name__ == "__main__":
	print(solution_pt1())
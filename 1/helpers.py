import timeit
import os, psutil
from memory_profiler import memory_usage

def get_data() -> str:
	""" Returns the problem input as a string. """
	filepath: str = "./input.txt"
	with open(filepath) as file:
		return file.read()

def benchmark(solution_fn):
	""" Prints the runtime and memory usage of solution_fn(). """
	num_repetitions=5000
	elapsed_time_ms = round(timeit.timeit(stmt=solution_fn,number=num_repetitions)/num_repetitions * 1000,4)
	
	# memory_used_mib=max(memory_usage((solution_fn, (), {}),interval=1e-6, timeout=0.01))

	print("%s ms" % (elapsed_time_ms))
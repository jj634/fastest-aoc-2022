import time
import os, psutil

def get_data() -> str:
	""" Returns the problem input as a string. """
	filepath: str = "./input.txt"
	with open(filepath) as file:
		return file.read()

def benchmark(solution_fn):
	""" Prints the runtime and memory usage of solution_fn(). """
	start_time = time.time()

	solution_fn()

	elapsed_time_ms = round((time.time() - start_time)*1000,4)

	process = psutil.Process(os.getpid())
	memory_used_mb=process.memory_info().rss / 2**20

	print("%s ms, %s MB" % (elapsed_time_ms, memory_used_mb))
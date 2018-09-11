import multiprocessing as mp
import os

mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
mem_gib = mem_bytes/(1024.**3)  # e.g. 3.74

print "No. of cores : ", mp.cpu_count()
print "Memory (GiB) : ", mem_gib
print "Page size : ", os.sysconf('SC_PAGE_SIZE')


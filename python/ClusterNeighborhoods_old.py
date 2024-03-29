usage = """
usage: python ClusterNeighborhoods.py inputFifo outputFifo nthreads
metisFile = path to one indexed metis graph
targetFile = filename to write new graph with added central node connected to every other node to
"""

import sys

from networkit import *

if len(sys.argv) != 4:
    print(usage)
    sys.exit(1)

i = 0
while(True):
    with open(sys.argv[2]) as f:
        f.readlines()
        print(i)
        i += 1
    with open(sys.argv[3], "w") as f:
        f.write("k")

#from multiprocessing import Pool
#
#if len(sys.argv) != 4:
#    print(usage)
#    sys.exit(1)
#
#inputGraph = sys.argv[1]
#outputPath = sys.argv[2]
#nthreads = int(sys.argv[3])
#
#
#def task(params):
#    file = params[0]
#    id = params[1]
#    nthreads = params[2]
#
#
#
#    # PLM is parallel by default, but the neighborhoods are tiny enough for 1 thread
#    # also scaling completely breaks if we use too many threads
#    setNumberOfThreads(1)
#
#    for i in range(id, main_graph.numberOfNodes(), nthreads):
#
#        #subg = normalizedNeighborhood(main_graph, i)
#        # PLM runs slower if node ids are spread apart
#
#        if len(subg.edges()) > 0:
#            community.detectCommunities(subg, algo=community.PLM(subg, True, par="none"))
#
#
#if __name__ == '__main__':
#    job = [(inputGraph, x, nthreads) for x in range(nthreads)]
#
#    with Pool(nthreads) as p:
#        p.map(task, job)
#
#    sys.exit(0)

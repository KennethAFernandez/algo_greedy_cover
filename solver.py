import sys
from subset import subset

'''
# Reformatted so read just returns the parsed contents of the file
Open the file, read in the number of elments and the number of sets. Create
the universal set from the given input and append rest of file to the items
list as (set(), weight, count)
'''
def read(file):      

    subsets = []

    try:
        with open(file, 'r') as f:
            n = int(f.readline().strip())   # Line 1
            m = int(f.readline().strip())   # Line 2
            univ = set(range(1, n + 1))

            count = 1
            for line in f:
                subsets.append(subset(set(int(i) for i in line.split()), int(f.readline()), count))
                count += 1
            f.close()
            
    except FileNotFoundError:
        print(f"Input file '{file}' does not exist")
        exit(-1)

    print(f" Input file  :  {file}")
    print(f"Count elems  :  {n}")
    print(f" Count sets  :  {m}")

    return n, univ, subsets

'''
# Renamed function from 'greedy' to 'simple'
Sort items list (contains (set(), weight, count )) by weight over length of items in the set
then while the cover does not equal the inputted universal set add values from tuple to
the cover, then remove tuple.
#items.sort(key = lambda x: (float(x[1]/len(x[0])), len(x[0])), reverse = False)
# I reformatted this quite a bit to fit the object format, but it should work exactly the same
# It now also checks if a cover isn't possible and will return a weight of -1 if this is the case
'''

def simple(univ, subsets):     

    cover = set()
    weight = 0
    used = []
    
    subsets.sort()
    
    isCover = False
    for ss in subsets:
        if len(ss.data) > 0:
            for val in ss.data:
                cover.add(val)

            weight += ss.weight
            used.append(ss.index)

            if cover == univ:
                isCover = True
                break

            i = 0
            for s in subsets:
                subsets[i].data = s.data.difference(cover)
                temp = subsets[i]
                i += 1

    if not isCover:
        return -1, None

    used.sort()
    print(f"   Solution  :  {weight}")
    print(f"  Sets Used  :  {used}")
    return weight, used

# OPTIMIZES SETS by removing sets that are *definitely* worse than others
def optimize(sets):
    return sets

if __name__ == "__main__":
    params = ["s"]
    pCount = 0
    infile = "input.txt"

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "?" or sys.argv[i] == "help":
            print("Usage: solver.py ['s' - simple heuristic]['nv' - numbver value heuristic] [infile: str]")
            exit()

        elif sys.argv[i] == "s":
            if not pCount: params = []
            params.append("s")
            pCount += 1

        elif sys.argv[i] == "nv":
            if not pCount: params = []
            params.append("nv")
            pCount += 1

        # Assume this is the name of the input file
        else:
            infile = sys.argv[i]

    n, univ, subsets = read(infile)

    # Execute specified algorithms
    bestWeight = 500000   # We have at most 500 lines with weight of at most 1000
    bestSubsets = []
    for p in params:
        if p == "s":
            print("  Algorithm  :  SIMPLE")
            weight, solsets = simple(univ, subsets)
        elif p == "nv":
            opsets = optimize(subsets)
            #weight, solsets = numberValue(n, univ, subsets)

        if weight < bestWeight:
            bestWeight = weight
            bestSubsets = solsets

    # TODO write output to output.txt (or some name variation of the input filename)

    sol = " ".join(map(str, solsets))
    with open('output.txt', 'w') as out:
        out.write(str(weight)+'\n')
        out.write(str(sol))  
        out.close()
    
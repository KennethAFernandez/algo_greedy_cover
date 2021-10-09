
def greedy(univ, items):

    cover = set()
    weight = 0
    used = []

    items.sort(key = lambda x: (float(x[1]/len(x[0])), len(x[0])), reverse = False)
    
    while cover != univ:
        tup = items[0]

        if len(tup[0]) > 0:
            for val in tup[0]:
                cover.add(val)
            weight += tup[1]
            used.append(tup[2])
            items.remove(tup)
        
            if(cover == univ): 
                break

            for i, temp in enumerate(items):
                items[i] = (temp[0].difference(cover), temp[1], temp[2])
                if len(items[i][0]) == 0:
                    items.remove(items[i])        

    return cover, weight, used

def read(file):

    items = []
    with open(file, 'r') as f:
        nelems = int(f.readline().strip())
        nsets = int(f.readline().strip())
        univ = set(range(1, nelems + 1))

        count = 1
        for line in f:
            items.append((set([int(i) for i in line.split()]), int(f.readline()), count))
            count += 1 

    f.close()

    cover, sol, sets = greedy(univ, items)

    print(f"Number of elems.:   {nelems}")
    print(f"Number of sets:     {nsets}")
    print(f"Solution:           {sol}")
    print(f"Sets Used:          {sets}")
    print(f"Cover:              {cover}")
    print()
read('long.txt')
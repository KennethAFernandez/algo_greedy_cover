
def greedy(univ, items):

    '''
    Sort items list (contains (set(), weight, count )) by weight over length of items in the set
    then while the cover does not equal the inputted universal set add values from tuple to
    the cover, then remove tuple. 
    MAYBE: Find the difference between the given sets and the current cover and update all the tuples
    and remove any tups that no longer have values in their set. 
    '''

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

    return weight, used

def read(file):

    '''
    Open the file, read in the number of elments and the number of sets. Create
    the universal set from the given input and append rest of file to the items
    list as (set(), weight, count)
    '''

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

    sol, sets = greedy(univ, items)

    print(f"Number of elems.:   {nelems}")
    print(f"Number of sets:     {nsets}")
    print(f"Solution:           {sol}")
    print(f"Sets Used:          {sets}")
    print()

print('Generated Input:')
read('input.txt')
print('Given Input:')
read('givenInput.txt')
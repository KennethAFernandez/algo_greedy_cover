# GENERATOR.py
# Generates subsets from the set of integers {1 to n} such that their union covers the parent set
# Format corresponds with AlgoBOWL formatting
#
# COMMAND:
# [python generator.py] n s r outFile
# n -> count of elements in parent set (values will range from 1 to n)
# m -> number of subsets to generate
# r -> range of subset weights will be (1 to r)
# outFile -> where to save the results (if none provided, output will be to stdout)
#
# AUTHOR: Liam Dempsey

from random import random
import sys

from subset import subset

def equilikely(a, b):
    return a + int((b - a + 1) * random())

def interval(n):
    return n - int(((n * (n + 1) * random() + 0.25) ** 0.5) - 0.5)

def writeline(line, output, file):
    if output:
        print(line)
        return

    file.write(f"{line}\n")

if __name__ == "__main__":
    params = [5, 5, 25]
    path = ""
    outfile = None
    stdout = True

    # Get program arguments
    for i in range(1, len(sys.argv)):
        try:
            arg = int(sys.argv[i])
            params[i - 1] = arg
        except ValueError:
            path = str(sys.argv[i])
            stdout = False
        except IndexError:
            print("Usage: generator.py [n: int] [m: int] [r: int] [outFile: str]")
        finally:
            pass

    # Attempt to open/create the specified file
    try:
        outfile = open(path, 'w')
    except IOError:
        stdout = True
    finally:
        pass

    print(f"Generator parameters: n = {params[0]}, m = {params[1]}, r = {params[2]}")
    if stdout: print("Outputting to standard out\n")
    else: print(f"Outputing to file: {path}")

    # Write n and s
    writeline(params[0], stdout, outfile)
    writeline(params[1], stdout, outfile)

    # Build the sets
    sets = []  # Final set of subsets

    # for m in range(params[1]):
    #     currSet = []
    #     val = interval(params[0])
    #
    #     while val <= params[0]:
    #         currSet.append(val)
    #         val += interval(params[0])
    #
    #     sets.append(currSet)

    # Create M sets
    for i in range(params[1]):
        #data = equilikely(1, params[0])
        weight = equilikely(1, params[2])
        sets.append(subset(None, weight))

    # Place every value (1, n) in a set
    for i in range(params[0]):
        index = i
        if index >= params[1]:
            index = equilikely(0, params[1] - 1)

        currSet = sets[index]
        currSet.data.add(i + 1)

    # Place at least one value in every set (n, m) [if applicable]
    for i in range(params[0], params[1]):
        currSet = sets[i]
        currSet.data.add(equilikely(1, params[0]))

    # Place n * m / 2 values randomly in the sets
    # Considering duplicates, this should yield sets with *roughly* an average length of n / 2
    for i in range(int(params[0] * params[1] / 2)):
        index = equilikely(0, params[1] - 1)
        currSet = sets[index]
        currSet.data.add(equilikely(1, params[0]))

    # Debug stuff
    # sum = 0
    # for item in sets:
    #     sum += len(item.data)
    #     print(item)
    #
    # print("Average: ", sum / params[1])

    # Output the set contents
    for item in sets:
        writeline(item, stdout, outfile)

class subset:
    def __init__(self, x : set, w, i = 0):
        if x is None: self.data = set()
        else: self.data = x
        self.weight = w
        self.index = i

    def __str__(self):
        output = ""

        for item in self.data:
            output += f"{item} "

        output = output.strip()
        output += "\n"
        output += str(self.weight)

        return output

    def __lt__(self, other):
        comp_self = float(self.weight) / len(self.data)
        comp_other = float(other.weight) / len(other.data)

        if comp_self == comp_other:
            return self.weight < other.weight

        return comp_self < comp_other

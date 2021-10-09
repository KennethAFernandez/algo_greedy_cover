class subset:
    def __init__(self, x, r):
        if x is None: self.data = set()
        else: self.data = {x}
        self.weight = r

    def __str__(self):
        output = ""

        for item in self.data:
            output += f"{item} "

        output = output.strip()
        output += "\n"
        output += str(self.weight)

        return output

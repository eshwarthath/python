class hiphen:
    def __init__(self):
        self.string = ""

class change(hiphen):
    def replace(self, string):
        string = string.replace(' ', '-')
        string = string.replace('e', 'N')
        print("New string:")
        print(string)

# ---- Main Code ----
h = change()
h.string = input()
string = h.string
h.replace(string)

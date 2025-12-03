class case:
    def __init__(self, s):
        self.s = s

    def check(self):
        upper = 0
        lower = 0
        for ch in self.s:
            if ch.isupper():
                upper += 1
            elif ch.islower():
                lower += 1
        print("The number of lowercase characters is:")
        print(lower)
        print("The number of uppercase characters is:")
        print(upper)

# Input reading
string = input().strip()

# Object creation
obj = case(string)

# Function call
obj.check()

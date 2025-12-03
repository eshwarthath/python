class anagram:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def checked(self):
        if sorted(self.s1) == sorted(self.s2):
            print("The strings are anagrams")
        else:
            print("The strings aren't anagrams")

# Input reading
string1 = input().strip()
string2 = input().strip()

# Object creation
strobj = anagram(string1, string2)

# Function call
strobj.checked()

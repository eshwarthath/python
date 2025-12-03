class vowel:
    def __init__(self, s):
        self.s = s

    def count_vowel(self):
        count = 0
        for ch in self.s:
            if ch.lower() in 'aeiou':
                count += 1
        print("Enter string:Count of the vowel is:")
        print(count)

# Input
string = input()

# Object creation
v = vowel(string)

# Function call
v.count_vowel()

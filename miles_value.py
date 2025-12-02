class miles:
    def __init__(self, k):
        self.k = k

    def convert(self):
        miles_value = self.k * 0.621371
        print(f"{self.k} kilometers is equal to {miles_value} miles")

k = float(input())
m = miles(k)
m.convert()

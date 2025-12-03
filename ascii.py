class ascii:
    def Show(self,c):
        print("The ASCII of'" + c + "' is", ord(c))

c = input()
obj = ascii()
obj.Show(c)

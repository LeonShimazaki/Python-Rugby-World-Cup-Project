print("hello world")

for number in range(1, 101):
    def SiteHost():
        if number % 15 == 0:
            return "SiteHost"
        elif number % 3 == 0:
            return "Site"
        elif number % 5 == 0:
            return "Host"
        else:
            return number
    print(SiteHost())

def ringNumber():
    global rings
    while(1):
        try:
            rings = int(input("Number of rings: "))
            if rings < 0:
                print("Please input a postive number of rings.")
            if rings > 0:
                return rings
        except ValueError:
            print("Please input a valid number of rings.")
        
print(ringNumber())
for i in range(1,6):
    for j in range(1,6):
        if (j>=6-i)and(j<=5):
            print(" * ",end="")
        else:
            print("  ",end=" ")
    print("\n")
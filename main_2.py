def shortest_path(a, b, c):
    paths = [("Edinburgh-Glasgow-Stirling-Perth-Dundee", a),
             ("Edinburgh-Stirling-Perth-Dundee", b),
             ("Edinburgh-Perth-Dundee", c)]
    shortest = min(paths, key=lambda x: x[1])
    print("The shortest path is {}: {}".format(shortest[0], shortest[1]))

print("Enter costs")
PD = int(input("Perth-Dundee(60): "))
EP = int(input("Edinburgh-Perth(100): "))
SP = int(input("Stirling-Perth(40): "))
ES = int(input("Edinburgh-Stirling(50): "))
GS = int(input("Glasgow-Stirling(50): "))
EG = int(input("Edinburgh-Glasgow(70): "))

print()
shortest_path(EG + GS + SP + PD, ES + SP + PD, EP + PD)

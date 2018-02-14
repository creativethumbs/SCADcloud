import math, random

output = open("cloud.scad","w")
count = 0

(prevX, prevY, prevZ) = (0,0,0)

# stores (x,y,z,radius)
pointslist = []

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

def distlist(point):
    for elem in pointslist:
        distance = dist(elem, point)

        if not(max(point[3], elem[3]) < distance):
            return False
    return True

output.write("module cloud() {\n")

while count < 7:
    if (count == 0):
        rad = random.uniform(4,6)
        output.write("translate([0,0," + str(rad) + "])")
        output.write("sphere("+str(rad)+", $fn=20, center = true);\n")
        pointslist.append((0,0,0,rad))
        count = count+1

    else:
        # (x, y, z) = (prevX+random.uniform(-7, 7), prevY+random.uniform(-7, 7),prevZ+random.uniform(-5, 5))
        (x, y, z, rad) = (random.uniform(-7, 7), random.uniform(-3, 3),random.uniform(0, 3), random.uniform(3,6))

        if(distlist((x,y,rad, rad))):

            output.write("translate([" + str(x) + "," + str(y) + "," + str(rad) + "])")
            output.write("sphere("+str(rad)+", $fn=20, center = true);\n")
            count = count+1

            pointslist.append((x,y,z, rad))

            # (prevX, prevY, prevZ) = (x,y,z)

output.write("}\n")
# output.write("rotate([0,90,90]) cloud();")
output.write("cloud();")

output.close()
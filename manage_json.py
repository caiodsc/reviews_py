from by_product_u import mv
import json

f = open("myfile", "w")
c = []
for i in range (79916):
    if not mv[i][0] in c:
        c.append(mv[i][0])

f.write(str(c))


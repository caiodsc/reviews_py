import json
from testdata_cat import mv
cats = []
jsonformated = {}
for i in range (79959):
    if not mv[i][1] in cats:#1
        cats.append(mv[i][1])#1
        jsonformated[str(mv[i][1])] =  {#1
            str(mv[i][0]) : int(mv[i][2])#0
        }
    else:
        jsonformated[str(mv[i][1])][str(mv[i][0])] = int(mv[i][2])#1#0
print(jsonformated)

f = open("base_de_dados.py", "w")
f.write(str(jsonformated))
f.close()
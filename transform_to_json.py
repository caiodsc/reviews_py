import json
from testdata_cat import mv
cats = []
jsonformated = {}
for i in range (79959):
    if not mv[i][0] in cats:
        cats.append(mv[i][0])
        jsonformated[str(mv[i][0])] =  {
            str(mv[i][1]) : int(mv[i][2])
        }
    else:
        jsonformated[str(mv[i][0])][str(mv[i][1])] = int(mv[i][2])
print(jsonformated)

f = open("base_de_dados_invertida.py", "w")
f.write(str(jsonformated))
f.close()
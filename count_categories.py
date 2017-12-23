from testdata import mv

categorias ={'Celulares e Telefonia Fixa': 0,
            'Móveis e Decoração': 0,
            'Eletrodomésticos': 0,
            'Eletrônicos': 0,
            'Informática e Tablets': 0,
            'Brinquedos e Games': 0,
            'Utilidades Domésticas': 0,
            'Eletroportáteis': 0,
            'Ferramentas e Máquinas': 0,
            'Relógios': 0,
            'Livros e CDs': 0,
            'Artigos Infantis': 0,
            'Beleza e Saúde': 0,
            'Escritório': 0,
            'Esporte e Lazer': 0,
            'Malas, Mochilas e Bazar': 0,
            'Vídeo e Foto': 0,
            'Cama, Mesa e Banho': 0,
            'Automotivos': 0}

for i in range (79959):
    c = int (mv[i])
    if 12001 <= c and c <= 12029:
        categorias['Eletrônicos'] += 1
    elif 12030 <= c and c <= 12068:
        categorias['Eletrodomésticos'] += 1
    elif 12069 <= c and c <= 12079:
        categorias['Vídeo e Foto'] += 1
    elif 12080 <= c and c <= 12109:
        categorias['Eletroportáteis'] += 1
    elif 12110 <= c and c <= 12137:
        categorias['Informática e Tablets'] += 1
    elif 12138 <= c and c <= 12255:
        categorias['Livros e CDs'] += 1
    elif 12256 <= c and c <= 12272:
        categorias['Artigos Infantis'] += 1
    elif 12273 <= c and c <= 12288:
        categorias['Beleza e Saúde'] += 1
    elif 12289 <= c and c <= 12311:
        categorias['Brinquedos e Games'] += 1
    elif 12312 <= c and c <= 12324:
        categorias['Escritório'] += 1
    elif 12325 <= c and c <= 12350:
        categorias['Esporte e Lazer'] += 1
    elif 12351 <= c and c <= 12371:
        categorias['Ferramentas e Máquinas'] += 1
    elif 12372 <= c and c <= 12392:
        categorias['Malas, Mochilas e Bazar'] += 1
    elif 12393 <= c and c <= 12491:
        categorias['Móveis e Decoração'] += 1
    elif 12492 <= c and c <= 12496:
        categorias['Relógios'] += 1
    elif 12497 <= c and c <= 12508:
        categorias['Celulares e Telefonia Fixa'] += 1
    elif 12509 <= c and c <= 12547:
        categorias['Utilidades Domésticas'] += 1
    elif 18001 <= c and c <= 18507:
        categorias['Automotivos'] += 1
    elif 19001 <= c and c <= 20002:
        categorias['Cama, Mesa e Banho'] += 1

print (categorias)
aqr= open("C:/temp/", 'w')
texto = []
texto.append("Lista Aluno\n")
texto.append("----\n")
texto.append("Jose Lima\n")
aqr.writelines(texto)
aqr.close()

aqr= open("C:/temp/", 'r')
texto= aqr.read()
print(texto)
aqr.close()

aqr= open("C:/temp/", 'r')
texto= aqr.readline()
for linha in texto:
    print(linha)
aqr.close()
aqr.close()
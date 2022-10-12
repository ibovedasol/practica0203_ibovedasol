frase = input('Escriba una frase; ')
vocal = input('Ponga una vocal; ')
print('La frase con ' + str(vocal) + ' en mayusculas es, '+ str(frase.replace(vocal, vocal.upper())))
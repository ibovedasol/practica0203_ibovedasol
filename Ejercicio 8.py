precio = input('Introduce el precio con 2 decimales; ')
print('Tienes que pagar' + str(precio[:precio.find('.')]) + '€ y '
+ str(precio[precio.find('.')+1:]) + ' cent. ')

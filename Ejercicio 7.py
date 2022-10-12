correo = input('Escribe un correo electronico: ')
print('El nuevo correo es; ' + str(correo[:correo.find('@')] + '@ceu.es'))
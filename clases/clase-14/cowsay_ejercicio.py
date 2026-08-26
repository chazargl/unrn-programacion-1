import cowsay
personaje = input('Ingrese un nombre de personaje elegible o exit para terminar: ')
while personaje != 'exit':
    print(cowsay.get_output_string(personaje, 'Hello World'))
    personaje = input('Ingrese un nombre de otro personaje elegible o exit para terminar: ')

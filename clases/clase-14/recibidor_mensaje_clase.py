import cliente
import cowsay

while True:
    msg = cliente.obtener_mensaje()
    print(cowsay.get_output_string('cow', msg))
    print(type(msg))

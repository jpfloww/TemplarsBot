from pynput.mouse import Listener
from pynput import keyboard as kb
lista=[]
def on_click(x, y, button, pressed):
    archivo = open("posiciones.txt", "a")
    if pressed:
        print('Se añade la posicion: '+str(x)+', '+str(y)+' ).')
        lista.append( (x,y))
        print(lista)

def suelta(tecla):
    print('se suelta la tecla'+str(tecla))
    if tecla== kb.KeyCode.from_char('q'):
        return False

print('Bienvenido, 1: Agregar nueva posicion en un mapa. 2: Usar posicion existente')
opcion=input('Ingrese opción: ')
if int(opcion)==1:
    with Listener(
            on_click=on_click , suelta=suelta) as listener:
        listener.join()

elif int(opcion)==2:
    print("desarrollandose")
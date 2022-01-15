import pyautogui
import keyboard
import time
import mouse
lista=[]
zona=input('Ingrese Zona: ')
recursos=input('Ingrese cantidad de recursos:' )
posicion=input('Ingrese posicion: ')
listadetalles=[zona,recursos,posicion]
listacolores=[]
while True:

    if keyboard.is_pressed('ctrl'):
        break
    if mouse.is_pressed(button='left'):
        print(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y))
        lista.append(pyautogui.position())
        listacolores.append(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y))
        time.sleep(0.1)
    time.sleep(0.1)
print(lista)
archivo=open('posiciones.txt','a')
cadena1=str(lista)
cadena2=cadena1.replace('),',');').replace('Point(','(').replace('x=','').replace('y=','').replace('[(','(').replace(')]',')').replace(' ','')
print(cadena2)
archivo.write(str(lista))
archivo.write('\n')
archivo.close()

detalle=open('detalles.txt','a')
detalle.write(str(listadetalles))
detalle.write('\n')
detalle.close()

archivocolores=open('colores.txt','a')
archivocolores.write(str(listacolores))
archivocolores.write('\n')
archivocolores.close()
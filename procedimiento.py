import pyautogui, time
import keyboard
archivo=open('constantes.txt','r')
lineas=archivo.readlines()
archivo.close()
#Leo primera linea que tiene que ver con estaencombate si no esta la varita
spelliconpos=(lineas[0].split(";")[1].split(',')[0], lineas[0].split(";")[1].split(',')[1]) # spelliconpos[0] es x. analogo y
spelliconcolor=tuple(map(int,lineas[0].split(";")[2].replace('(','').replace(')','').split(',')))

#Leo segunda linea que tiene que ver si esta la ventana de cierre de combate
endfightwindowpos=(lineas[1].split(";")[1].split(',')[0], lineas[1].split(";")[1].split(',')[1])
endfightwindowcolor=tuple(map(int,lineas[1].split(";")[2].replace('(','').replace(')','').split(',')))
print(endfightwindowpos)
print(pyautogui.pixel(int(endfightwindowpos[0]),int(endfightwindowpos[1])))
print(pyautogui.pixelMatchesColor(int(endfightwindowpos[0]), int(endfightwindowpos[1]), endfightwindowcolor, tolerance=30))
def estaencombate():
    if pyautogui.pixelMatchesColor(int(spelliconpos[0]),int(spelliconpos[1]),  spelliconcolor, tolerance=40):
        print('sale verdadero, no esta en combate')
        return False
    else:
        print('sale falso, si esta en combate')
        return True
def cerrarventanacombate():
    if pyautogui.pixelMatchesColor(int(endfightwindowpos[0]), int(endfightwindowpos[1]), endfightwindowcolor, tolerance=3):
        print('Se encuentra ventana, se cierra')
        keyboard.press('esc')
        keyboard.release('esc')

while True:
    if estaencombate():
        print('en combate')
    cerrarventanacombate()
    time.sleep(4)

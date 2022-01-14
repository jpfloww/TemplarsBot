import pyautogui
import keyboard
import time
import mouse
# Para funcion estaencombate
#lista=[]
archivo=open('constantes.txt','w')
contador=0
contador2=0
print('Mueva el puntero del ratón al icono de mis hechizos en la parte amarilla de la varita. Luego presione Ctrl')
while True:
    contador2=0
    if keyboard.is_pressed('ctrl'):
        if contador==0 and contador2==0:
            #lista.append(['spellicon', pyautogui.position(),pyautogui.pixel(pyautogui.position().x, pyautogui.position().y) ]) # nombre, (x,y) , RGB(255,200,200)
            archivo.write('spellicon; '+str(pyautogui.position().x)+', '+str(pyautogui.position().y)+'; '+str(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)))
            archivo.write('\n')
            print('Añadido correctamente: '+'color: '+str(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y) ))
            contador=1
            contador2=1
            print('Mueva el puntero hacia el marco lateral negro de la ventana de termino de combate. Luego presione Ctrl')
            time.sleep(0.5)

        if contador==1 and contador2==0:

            archivo.write('endfightwindow; '+str(pyautogui.position().x)+', '+str(pyautogui.position().y)+'; '+str(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)))
            archivo.write('\n')
            print(' Añadido correctamente')
            contador=2
            contador2=1
            time.sleep(0.5)



    if keyboard.is_pressed('shift'):
        print('se apreto shift')
        break
    time.sleep(0.1)
archivo.close()

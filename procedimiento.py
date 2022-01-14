import pyautogui
archivo=open('constantes.txt','r')
lineas=archivo.readlines()
archivo.close()
#Leo primera linea que tiene que ver con estaencombate si no esta la varita
spelliconpos=(lineas[0].split(";")[1].split(',')[0], lineas[0].split(";")[1].split(',')[1]) # spelliconpos[0] es x. analogo y
spelliconcolor=lineas[0].split(";")[2]
print(spelliconcolor)
print(pyautogui.pixel(int(spelliconpos[0]),int(spelliconpos[1])))
print(   pyautogui.pixelMatchesColor(int(spelliconpos[0]),int(spelliconpos[1]), spelliconcolor ) )
def estaencombate():
    print('estoyencombate')

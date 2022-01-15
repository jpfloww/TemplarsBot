import pyautogui, time, keyboard, mouse

k=0
#pyautogui.screenshot('num7.png', region=(946,732, 23, 20)) SIRVE PARA SACAR FOTO
time.sleep(2)
while True:
    archivoposiciones = open('posiciones.txt', 'r')
    archivocolores = open('colores.txt', 'r')
    for linea in archivoposiciones:
        listadeelementos=linea.split(';')
        for pos in listadeelementos:
            coordenadas=pos.split(',')
            x=int(coordenadas[0]) ; y=int(coordenadas[1])
            pyautogui.moveTo(x,y)
            time.sleep(0.3)
            mensajedeencuentro=pyautogui.locateOnScreen('num7.PNG', region=(x,y,430,200),grayscale=False,confidence=0.1)
            guardarmensaje=str(type(mensajedeencuentro))
            print(guardarmensaje+'')
            if guardarmensaje=="<class 'NoneType'>": # Si ocurre esto significa que se puede recolectar
                print('no se encontro nada')
                mouse.press('left')
                mouse.release('left')
                time.sleep(5.5)
            else:
                time.sleep(0.3)
            time.sleep(0.1)
    archivoposiciones.close()
    archivocolores.close()

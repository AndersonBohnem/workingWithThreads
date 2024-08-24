import threading
import os
import time
import subprocess

contador = 0
contador_lock = threading.Lock()  
pids = []  


def abrir_notepad():
    global contador
    with contador_lock:
        contador += 1
        data_hora = time.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Notepad {contador} foi aberto em {data_hora}.")
    
    process = subprocess.Popen('notepad.exe', shell=True)
    pids.append(process.pid)

def fechar_notepads():
    time.sleep(15)  
    os.system('taskkill /f /im notepad.exe')  
    print(f"Todos os Notepads foram fechados em {time.strftime('%d/%m/%Y %H:%M:%S')}")

def gerenciar_notepads():
    
    abrir_threads = []

    
    for i in range(2):
        thread = threading.Thread(target=abrir_notepad)
        abrir_threads.append(thread)
        thread.start()
        time.sleep(10)  

    
    for thread in abrir_threads:
        thread.join()

    
    fechar_thread = threading.Thread(target=fechar_notepads)
    fechar_thread.start()
    fechar_thread.join()


if __name__ == "__main__":
    gerenciar_notepads()
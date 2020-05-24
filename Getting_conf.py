#========================================================
# Dando uma olhadinha na máquina
# adaptado por Julio Cesar Souza-Silva, MD, MSc, PhD
# 
# O Objetivo deste aplicativo é levantar dados de configuração (reconhceimento da plataforma) da maquina em operação 
# e mostrá-los em uma Janela (GUI)
# Resultado: Objetivo básico alcaçado
# 
# V 1.0
# 23/05/2020
# ======================================================================================================================

import socket
import os 
import sys
import platform
#import psutil
import uuid


# Obtenção de dados do meio ambiente de sistema operacional e máquina
Author_name ='Julio Cesar Souza-Silva, PhD'
OS_System_name = "Name: " +socket.gethostname()
OS_System_fqdn = "FQDN: " +socket.getfqdn()
OS_System_platform = "System Platform: "+sys.platform
OS_Machine = "Machine: " +platform.machine()
OS_Node = "Node " +platform.node()
OS_Platform = "Platform: "+platform.platform() 
OS_Processor = "Processor: " +platform.processor()
OS_System_OS = "System OS: "+platform.system()
OS_System_Release = "Release: " +platform.release()
OS_System_Version = "Version: " +platform.version()
OS_Full_Text_Exibition = Author_name+'\n\n'+ OS_System_name + '\n' + OS_System_fqdn+ '\n' + OS_System_platform + '\n' + OS_Machine + '\n'+ OS_Node + '\n'+ OS_Platform + '\n'+ OS_Processor + '\n'+ OS_System_OS +'\n'+ OS_System_Release +'\n'+ OS_System_Version +'\n'

# Exibição de dados na janela
from tkinter import *
window = Tk()
window.title("Obtenção de dados de configuração do sistema")
window.geometry('350x400')
lbl = Label(window, text=OS_Full_Text_Exibition)
lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Muito obrigado!")
    

btn = Button(window, text="Pressione Aqui", command=clicked)
btn.grid(column=0, row=12)
window.mainloop()


#Need  Model of Computer i.e.  HP Compaq 8100 Elite SFF, HP X600 workstation
#need Ram
#need Disk space
#Need Manufacturer i.e. HP, Dell, Lenova
# EOF ------------------------------------------------------------------------------------------------------ DrJCSS
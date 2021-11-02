#OPTIMIZACION DEL CODIGO USANDO FUNCIONES
#correr comandos
import subprocess
#para importar y usar comandos
import optparse
#para usar expresiones regulares
import re

def mac_changer(interface, new_mac):
    subprocess.call(["ifconfig" , interface , "down"])
    subprocess.call(["ifconfig" , interface , "hw","ether" , new_mac])
    subprocess.call(["ifconfig" , interface , "up"])
    #print('Se ha cambiado la direccion MAC a : ', new_mac)

def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface",dest="interface",help="Interface para cambiar idreccion MAC")
    parser.add_option("-m", "--mac",dest="new_mac",help="Define la nueva direccion MAC")
    #return parser.parse_args()
    (options,arguments)=parser.parse_args()
    #print(options)
    if not options.interface:
        parser.error("Ingrese una interface correcta, usa --help para mas informacion")
    elif not options.new_mac:
        parser.error("Ingrese una MAC valida, use --help para mas informacion")
    return options

def get_current_mac(interface):
    ifconfig_output= subprocess.check_output(["ifconfig",interface])
    #print(ifconfig_output)
    mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_output)
    #en regex se guardan los resultados en grupos, por eso se instancia el grupo 0
    if mac_search:
        return mac_search.group(0)
    else:   
        print("No se pudo obtener la direccion mac")

options = get_arguments()
current_mac= get_current_mac(options.interface)
print("Current MAC =  " + str(current_mac))

mac_changer(options.interface,options.new_mac)
current_mac_n = get_current_mac(options.interface)
if current_mac_n == options.new_mac:
    print("[+] DIreccion MAC cambiada a " + current_mac_n)
else:
    print ("[-] Direccion MAC no fue cambiada.")




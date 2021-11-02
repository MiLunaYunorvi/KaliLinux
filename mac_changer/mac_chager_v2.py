#correr comandos
import subprocess
#para importar y usar comandos
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface",dest="interface",help="Interface para cambiar idreccion MAC")
parser.add_option("-m", "--mac",dest="new_mac",help="Define la nueva direccion MAC")
(options,arguments)=parser.parse_args()

#options recibe un diccionario con los valores de las variables segun se llamaron en destino.
#print(options,'  ',arguments)

#refinar el programa con variables
interface = options.interface
new_mac = options.new_mac


subprocess.call(["ifconfig" , interface , "down"])
subprocess.call(["ifconfig" , interface , "hw","ether" , new_mac])
subprocess.call(["ifconfig" , interface , "up"])

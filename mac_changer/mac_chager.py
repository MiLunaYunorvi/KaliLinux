#correr comandos
import subprocess

#subprocess.call("ifconfig eth0 down",shell=True)
#subprocess.call("ifconfig eth0 hw ether aa:bb:cc:dd:ff:00",shell=True)
#subprocess.call("ifconfig eth0 up",shell=True)

#refinar el programa con variables
interface = raw_input("interface > ")
new_mac = raw_input ("nuevo MAC > ")

#subprocess.call("ifconfig " + interface + " down",shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac,shell=True)
#subprocess.call("ifconfig " + interface + " up",shell=True)

##al usar shell=True se permite la ejecucion de varios comandos concatenados con ';'
#por eso se hace uso de la siguiente sintaxis: 
subprocess.call(["ifconfig" , interface , "down"])
subprocess.call(["ifconfig" , interface , "hw","ether" , new_mac])
subprocess.call(["ifconfig" , interface , "up"])

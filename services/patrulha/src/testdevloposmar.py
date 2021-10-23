#Biblioteca para Acesso
from netmiko import ConnectHandler

#Informações do Usuario
cisco = { 
    'device_type': 'cisco_ios', 
    'host': '10.10.20.161', 
    'username': 'developer', 
    'password': 'C1sco12345'
}  

our_lab = 'b3264b'
xr_node = 'n0'

cmd =  "show ip int brief"

#Conexão com o elemento
# Will automatically 'disconnect()'
with ConnectHandler(**cisco) as net_connect:
    #print(net_connect.find_prompt())
    output1 = net_connect.send_command(f'open /{our_lab}/{xr_node}/0\r')
    net_connect.send_command("\n")
    net_connect.send_command("ena")
    
print()
print(output1)
print()
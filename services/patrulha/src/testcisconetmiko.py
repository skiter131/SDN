#Biblioteca para Acesso
from netmiko import ConnectHandler

cisco = { 
'device_type': 'cisco_ios', 
'host': '192.168.123.2', 
'username': 'patrulha', 
'password': '1234',
'secret' :  'patrulha123'
}  

# net_connect = ConnectHandler(**cisco)

# print(net_connect.find_prompt())

# config_commands = ['do show ip int brief']

# output =  net_connect.send_config_set(config_commands)

command = "show ip int brief"

# with open('cisco.csv','w+', encoding = 'utf-8') as net_connect:
#     output = net_connect.send_command(command)

# #print(output)

with ConnectHandler(**cisco) as net_connect:
    net_connect.enable()
    output = net_connect.send_command(command)

print()
print(output)
print()
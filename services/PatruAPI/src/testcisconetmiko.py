#Biblioteca para Acesso
from netmiko import ConnectHandler

cisco = { 
'device_type': 'cisco_ios', 
'host': 'sandbox-iosxe-latest-1.cisco.com', 
'username': 'developer', 
'password': 'C1sco12345', 
}  

net_connect = ConnectHandler(**cisco)
net_connect.find_prompt()

config_commands = ['do show int g1', 'do show ip int brief']

output =  net_connect.send_config_set(config_commands)

# with open('cisco.csv','w+', encoding = 'utf-8') as arquivo:
#     arquivo.write(output)

print(output)

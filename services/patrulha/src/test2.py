from netmiko import ConnectHandler
from pprint import pprint

#Informações do Usuario
cisco1 = { 
    'device_type': 'cisco_ios', 
    'host': '10.10.20.50', 
    'username': 'developer', 
    'password': 'C1sco12345',
    "global_delay_factor": 2,

}  

# our_lab = "b3264b"
# xr_node = "n0"

#command = "show ip arp"
net_connect = ConnectHandler(**cisco1)
output = print(net_connect.find_prompt())
# net_connect.enable()
# net_connect.disconnect()

print("output")
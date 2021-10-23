import getpass
import netmiko
from virl2_client import ClientLibrary
from pprint import pprint

LAB_USERNAME = 'developer'
LAB_PASSWORD = 'C1sco12345'
VIRL_CONTROLLER = '10.10.20.161'
VIRL_USERNAME = 'developer'
VIRL_PASSWORD = 'C1sco12345'

client = ClientLibrary(VIRL_CONTROLLER, VIRL_USERNAME, VIRL_PASSWORD, ssl_verify=False)

our_lab = 'b3264b'
xr_node = 'n0'

c = netmiko.ConnectHandler(device_type='cisco_ios', host=VIRL_CONTROLLER, username=VIRL_USERNAME, password=VIRL_PASSWORD)
c.write_channel('\r')
c.write_channel(f'open /{our_lab}/{xr_node}/0\r')

c.write_channel('\r')
c.write_channel(LAB_USERNAME + '\r')
c.write_channel(LAB_PASSWORD + '\r')

# our_lab = "b3264b"
# xr_node = "n0"

command = "show ip int brief"

output1 = print(c.find_prompt())
c.enable()

c.write_channel('\r')

output = c.send_command(command, use_textfsm=True)

#print(output)

c.disconnect()

print()
pprint(output)
print()

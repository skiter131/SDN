import getpass
import netmiko

from virl2_client import ClientLibrary

LAB_USERNAME = 'developer'
LAB_PASSWORD = 'C1sco12345'
VIRL_CONTROLLER = '10.10.20.161'
VIRL_USERNAME = 'developer'
VIRL_PASSWORD = 'C1sco12345'

client = ClientLibrary(VIRL_CONTROLLER,
                       VIRL_USERNAME,
                       VIRL_PASSWORD,
                       ssl_verify=False)

# this assumes that there's exactly one lab with this title
our_lab = client.find_labs_by_title('Projeto_EB')[0]
xr_node = 'n0'

# open the Netmiko connection via the terminal server
# (SSH to the controller connects to the terminal server)
c = netmiko.ConnectHandler(device_type='terminal_server',
                           host=VIRL_CONTROLLER,
                           username=VIRL_USERNAME,
                           password=VIRL_PASSWORD)

# send CR, get a prompt on terminal server
c.write_channel('\r')

# open the connection to the console
c.write_channel(f'open /{our_lab.id}/{xr_node}/0\r')

# router login
# this makes an assumption that it's required to login
c.write_channel('\r')
# c.write_channel(LAB_USERNAME + '\r')
# c.write_channel(LAB_PASSWORD + '\r')

# switch to Cisco XR mode
netmiko.redispatch(c, device_type='cisco_ios')
c.find_prompt()

# get the list of interfaces
result = c.send_command('show ip int brief')
print(result)

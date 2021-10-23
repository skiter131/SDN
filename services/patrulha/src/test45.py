from netmiko import ConnectHandler
import re
#from device_info import ios_xe1 as device # noqa

# Create a CLI command template
show_interface_config_temp = "show running-config interface {}"

with ConnectHandler(host='10.10.20.161', username='developer', password='C1sco12345', device_type = 'cisco_ios') as ch:
    ch.write_channel('\r')
    ch.write_channel(f'open /{our_lab}/{xr_node}/0\r')

    ch.write_channel('\r')
    ch.write_channel(LAB_USERNAME + '\r')
    ch.write_channel(LAB_PASSWORD + '\r')


    # Create desired CLI command and send to device
    command = show_interface_config_temp.format("Loopback103")
    interface = ch.send_command(command)

    # Print the raw command output to the screen
    print(interface)

    try:
        # Use regular expressions to parse the output for desired data
        name = re.search(r'interface (.*)', interface).group(1)
        description = re.search(r'description (.*)', interface).group(1)
        ip_info = re.search(r'ip address (.*) (.*)', interface)
        ip = ip_info.group(1)
        netmask = ip_info.group(2)

        # Print the info to the screen
        print("The interface {name} has ip address {ip}/{mask}".format(
                name = name,
                ip = ip,
                mask = netmask,
                )
            )
    except Exception:
        print("There was an error, Loopback103 might not exist.")
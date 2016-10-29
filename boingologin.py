import sys

from spoofmac import interface

def connect()
    spoofer = interface.get_os_spoofer()
    with open('address', 'w') as fw:
        for port, device, address, current_address in spoofer.find_interfaces():
            if address in current_address:
                fw.write('{0}/{1}\n'.format(device, current_address.split(' ')))
            else:
                print(port, device, address, current_address)
                print("Manual current address record required")
                manual_address = input()
                fw.write('{0}/{1}\n'.format(device, current_address.split(' ')))
            spoofer.set_interface_mac(device, '00:00:00:00:00:01')
            print("Mac address set to 1 for all devices")

def disconnect()
    spoofer = interface.get_os_spoofer()
    with open('address') as fp:
        for line in fp:
            device, address = line.split('/')
            spoofer.set_interface_mac(device, address)
            print("Mac address set to oringinal for all devices")

if __name__ == '__main__':
    if sys.argv[1] in ['c', 'connect']:
        connect()
    elif sys.argv[1] in ['dc', 'disconnect']:
        disconnect()

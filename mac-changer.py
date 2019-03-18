import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", dest="new_mac", help="New MAC adress")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("Please specify a new mac address, use --help for more info.")
        return  options

def change_mac (interface, new_maac)
    print("Channing MAC address for " + interface + "to " new_maac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_maac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface,options.new_mac)

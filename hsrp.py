#This will generate a pair of HSRPv2 enabled SVIs with a random password
#for HSRP authentication using MD5

import uuid

def gen_password(string_length=10):
    #Returns a random string of length string_length
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    #random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

def generate_config(vlan, subnet, mask):
	hsrpAuth = 	gen_password()

	print("!!!!! SWITCH A !!!!!")
	print("interface vlan " + vlan)
	print("  ip address " + subnet + "2 " + mask)
	print(" no ip proxy-arp")
	print(" no ip unreachables")
	print(" hsrp version 2")
	print(" hsrp " + vlan)
	print("  authentication md5 key-string " + hsrpAuth)
	print("  priority 110")
	print("  preempt")
	print("  ip " + subnet + "1")
	#
	print("\n!!!!! SWITCH B !!!!!")
	print("interface vlan " + vlan)
	print("  ip address " + subnet + "3 " + mask)
	print(" no ip proxy-arp")
	print(" no ip unreachables")
	print(" hsrp version 2")
	print(" hsrp " + vlan)
	print("  authentication md5 key-string " + hsrpAuth)
	print("  priority 90")
	print("  ip " + subnet + "1")
	return;

print("::::::::::::::::::::::::::::::::::::")
print("::::: HSRP Interface Generator :::::")
print("::::::::::::::::::::::::::::::::::::\n")
print("This will generate two SVI configs with the following settings:\n")
print("Virtual IP:   x.x.x.1 | Auth enabled (10 characters) | HSRP v2")
print("Switch A: IP: x.x.x.2 | HSRP Priority 110 | Premption")
print("Switch B: IP: x.x.x.3 | HSRP Priority 90  | No preemption\n")


vlan = input("What VLAN number is this for? ")
subnet = input("What IP subnet? (Use x.x.x.) ")
mask = input("What subnet mask? (Full mask, no CIDR notation) ")
generate_config(vlan, subnet, mask)




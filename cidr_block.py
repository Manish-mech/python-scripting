import ipaddress

# Function to calculate subnet CIDRs from a given VPC CIDR and required number of subnets
def generate_ip(cidr_block, subnet_count):
    vpc = ipaddress.ip_network(cidr_block)  # Convert input CIDR to ip_network object
    bits = (subnet_count - 1).bit_length()  # Calculate how many extra bits are needed
    prefix = vpc.prefixlen
    new_prefix = bits + prefix  # New prefix length for subnets

    # If new prefix is larger than 32, it's invalid for IPv4
    if new_prefix > 32:
        raise ValueError("Please enter the correct values:")

    subnets = list(vpc.subnets(new_prefix=new_prefix))  # Generate subnets with new prefix

    # Check if we have enough subnets
    if len(subnets) < subnet_count:
        raise ValueError("The subnets are not sufficient:")

    return subnets[:subnet_count]  # Return only the required number of subnets

def main():
    # Take input from user for CIDR and number of subnets
    cidr_block = input("Please enter the CIDR block such as 10.0.0.0/16:\t")
    subnet_count = int(input("Please enter the number of subnets:\t"))
    try:
        subnets = generate_ip(cidr_block, subnet_count)
        # Print each subnet
        for i, subnet in enumerate(subnets):
            print(f" subnet {i+1}: {subnet}")
    except ValueError:
        print("Please provide the valid response!")

if __name__ == "__main__":
    main()

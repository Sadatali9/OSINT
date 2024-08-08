import socket

def network_scanner(ip_address, port_range):
    """
    Scan a network for open ports and services.
    """
    for port in range(port_range[0], port_range[1]):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

def main():
    ip_address = input("Enter the IP address: ")
    port_range = input("Enter the port range (e.g., 1-100): ")
    port_range = [int(x) for x in port_range.split('-')]
    network_scanner(ip_address, port_range)

if __name__ == "__main__":
    main()
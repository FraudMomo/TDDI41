import subprocess, ipaddress

# Settings
IP_NETWORK = "10.0.0.0/24"
NETMASK = "24"
ROUTER_IP = "10.0.0.1"
NAMES = ["gw", "server", "client-1", "client-2"]

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def test_ip():
    result = run_command("ip addr | grep inet | grep ens3")
    ip = result.split()[1].split('/')[0]
    netmask = result.split()[1].split('/')[1]
    assert ipaddress.ip_address(ip) in ipaddress.ip_network(IP_NETWORK) and netmask == NETMASK

def test_gateway():
    gateway = run_command("ip r | grep default").split()[2]
    assert gateway == ROUTER_IP

def test_name():
    name = run_command("cat /etc/hostname").strip()
    assert name in NAMES

def test_reach_router():
    result = run_command(f"ping {ROUTER_IP} -c 1 | grep transmitted")
    transmitted = int(result.split(',')[0].strip()[0])
    recieved = int(result.split(',')[1].strip()[0])
    assert transmitted == recieved == 1

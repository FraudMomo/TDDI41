import subprocess

commands = [
    # ping 10.0.2.2
    ['ping -c 3 10.0.2.2'],
    # Is ipforwarding enabled?
    ['cat /etc/sysctl.conf | grep net.ipv4.ip_forward'],
    # Is IP-masquerading enabled?
    ['iptables -t nat -L'],
]

for command in commands:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))
    input()

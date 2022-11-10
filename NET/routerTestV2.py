import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def test_reach_ip():
    result = run_command(f"ping 10.0.2.2 -c 1 | grep transmitted")
    transmitted = int(result.split(',')[0].strip()[0])
    recieved = int(result.split(',')[1].strip()[0])
    assert transmitted == recieved == 1

def test_ip_forwarding_on():
    assert run_command("cat /proc/sys/net/ipv4/ip_forward")

def test_masquerading():
    result = run_command("iptables -L -t nat | grep MASQUERADE")
    assert result.split()[0] == "MASQUERADE"

import subprocess

# Settings
NAMESERVER = "10.0.0.4"

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def test_nameserver():
    result = run_command("cat /etc/resolv.conf | grep nameserver")
    assert NAMESERVER in result

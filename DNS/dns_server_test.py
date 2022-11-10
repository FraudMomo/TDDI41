import subprocess

# Variables


def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def test_bind9_conf():
    result = run_command("named-checkconf")
    assert result == ""

def test_bind9_zone():
    result = run_command("named-checkzone grupp2.example.com /etc/bind/zones/grupp2.example.com")
    assert "OK" in result

def test_bind9_zone():
    result = run_command("systemctl list-units --type=service --state=running | grep named.service")
    assert "named.service" in result

def test_dig():
    result = run_command("dig ")
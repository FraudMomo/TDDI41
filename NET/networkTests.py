import subprocess

commands = [
    # network config
    ['ip addr'],
    # configured routes
    ['tail -4 /etc/network/interfaces'],
    # hostname
    ['cat /etc/hostname'],
    # ping router
    ['ping -c 3 10.0.0.1']
]

for command in commands:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))
    input()

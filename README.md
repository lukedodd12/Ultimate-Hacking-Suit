# Ultimate Hacking Suite

A self-contained, portable suite with **200+ pentesting and hacking tools** across 16 categories, inspired by HackingToolkit. Tools are auto-installed via `requirements.txt` (Python dependencies) and `install_tools.sh` (system tools and repos).  

Run `Ultimate_hacking_tool.py` to access a clean, menu-driven interface for launching tools like **Nmap, sqlmap, Metasploit**, and more.  

> **Designed for educational purposes only.** Ideal for pentesting labs like HackTheBox or TryHackMe.

---

## Features

- **200+ Tools:** Includes Nmap, sqlmap, Metasploit, Aircrack-ng, Hydra, Sherlock, XSStrike, and 120+ custom scripts from HackingToolkit.
- **16 Categories:** Anonymity, Information Gathering, Wireless Attacks, SQL Injection, Phishing, Web Attacks, DDoS, RATs, and more.
- **Auto-Installation:** Python dependencies via `pip`, system tools via `apt` or `pkg`, and git-cloned repos for full coverage.
- **User-Friendly Menu:** Nested text-based UI in `Ultimate_hacking_tool.py` simplifies tool usage—no manual command typing.
- **Portable:** Distributed as a `.zip` file for easy sharing and setup.
- **Platform Support:** Optimized for **Kali/Parrot Linux**. Partial support for **Termux (Android)** with root for some tools.

---

## Installation

### 1. Unzip the Archive
```bash
unzip ultimate-hacking-suite.zip
cd ultimate-hacking-suite

2. Install Python Dependencies

pip3 install -r requirements.txt

3. Install System Tools and Clone Repos

chmod +x install_tools.sh
sudo ./install_tools.sh

4. Run the Suite

sudo python3 Ultimate_hacking_tool.py

> Requires root for most tools. In Termux, run without sudo if not rooted (some tools may fail).




---

Termux Notes

Use pkg install instead of apt in install_tools.sh.

Tools like Wireshark, Autopsy, or Ghidra may not work without root or a Linux VM.

Install prerequisites:


pkg install git python wget curl clang

Non-Linux Users

Use a Kali/Parrot VM or WSL2 on Windows.

Some GUI tools (Burp Suite, Maltego) require a desktop environment.



---

Usage

sudo python3 Ultimate_hacking_tool.py

or in Termux:

python3 Ultimate_hacking_tool.py

Navigate the menu, select a category, choose a tool, and launch with default/example commands.

Customize commands by editing Ultimate_hacking_tool.py.

Replace placeholders like target.com, your.ip, <BSSID> with real values.

Check tools/other_scripts for additional HackingToolkit scripts.



---

Tool Categories

Anonymously Hiding Tools (6): Tor, Proxychains, Anonsurf, VPNBook, I2P, OnionScan
Information Gathering (16): Nmap, theHarvester, Maltego, Shodan CLI, Recon-ng, plus 11+ scripts in tools/other_scripts
Wordlist Generator (5): Crunch, Cewl, Cupp, Mentalist, Custom Script
Wireless Attacks (9): Aircrack-ng, Wifite, WiFi Jammer (Deauth), Kismet, plus 5+ scripts
SQL Injection (7): SQLMap, NoSQLMap, sqlninja, plus 4+ scripts
Phishing Attacks (16): SET, Evilginx2, HiddenEye, plus 13+ scripts
Web Attacks (7): Burp Suite, Nikto, Wapiti, plus 4+ scripts
Post Exploitation (2): Meterpreter, PowerSploit
Forensic Tools (5): Autopsy, Volatility, Sleuth Kit, plus 2+ scripts
Payload Creation (8): MSFVenom, Veil, Shellter, plus 5+ scripts
Exploit Framework (4): Metasploit, Exploit-DB, RouterSploit, BeEF
Reverse Engineering (3): Ghidra, Radare2, IDA Free
DDoS Attacks (4): hping3, LOIC, Slowloris, Custom Script
Remote Administrator Tools (2): Pupy, QuasarRAT
XSS Attacks (9): XSStrike, XSSer, XSS Hunter, plus 6+ scripts
Steganography (4): Steghide, Stegseek, OpenStego, Custom Script
Other Tools (120+): Hydra, ADB, IDN Homograph, Email Verify, Hashcat, WiFi Deauth, Sherlock, Payload Injector, Wget, plus 110+ scripts in tools/other_scripts.


---

Notes

Customization: Edit Ultimate_hacking_tool.py to set targets or parameters.

Termux Limitations: Root or GUI may be required for full functionality.

Install Time: ~10-30 minutes depending on system and network.

Errors: If a tool fails, rerun sudo ./install_tools.sh or check tools/other_scripts.



---

Contributing

1. Edit Ultimate_hacking_tool.py to add new menu options.


2. Update install_tools.sh for system dependencies.


3. Add scripts to tools/other_scripts.
Share improvements via pull requests.




---

License

GNU General Public License v3.0. See the LICENSE file.


---

Disclaimer

EDUCATIONAL USE ONLY.
Authorized pentesting and cybersecurity learning only. Unauthorized hacking violates local and international laws. Use responsibly and only with explicit permission.




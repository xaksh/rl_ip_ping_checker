
██████╗░░█████╗░░█████╗░██╗░░██╗███████╗████████╗  ██╗░░░░░███████╗░█████╗░░██████╗░██╗░░░██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝  ██║░░░░░██╔════╝██╔══██╗██╔════╝░██║░░░██║██╔════╝
██████╔╝██║░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░  ██║░░░░░█████╗░░███████║██║░░██╗░██║░░░██║█████╗░░
██╔══██╗██║░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░  ██║░░░░░██╔══╝░░██╔══██║██║░░╚██╗██║░░░██║██╔══╝░░
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗███████╗░░░██║░░░  ███████╗███████╗██║░░██║╚██████╔╝╚██████╔╝███████╗
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚══════╝╚══════╝╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚══════╝

██╗██████╗░  ██████╗░██╗███╗░░██╗░██████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██║██╔══██╗  ██╔══██╗██║████╗░██║██╔════╝░  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║██████╔╝  ██████╔╝██║██╔██╗██║██║░░██╗░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║██╔═══╝░  ██╔═══╝░██║██║╚████║██║░░╚██╗  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║██║░░░░░  ██║░░░░░██║██║░╚███║╚██████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝╚═╝░░░░░  ╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

## Quick using One-Liners
For Unix-like Systems (Linux, macOS):

```bash
curl -sL https://raw.githubusercontent.com/xaksh/rl_ip_ping_checker/main/server_info.py | python -
```

For Windows (Using PowerShell):

```powershell
Invoke-WebRequest https://raw.githubusercontent.com/xaksh/rl_ip_ping_checker/main/server_info.py -OutFile rl_log_parser.py; python rl_log_parser.py; Remove-Item rl_log_parser.py
```

# Description
The Rocket League IP Ping Checker is a Python script for checking the ping to servers you've played on in Rocket League. I created this script to easily assess server performance by pinging IP addresses extracted from the game's log files.

### Features
- Parses Rocket League log files to find server IPs.
- Checks ping for each unique server IP.
- Groups server data by log file and IP.

### Prerequisites
- Python 3.6 or higher.
- Access to Rocket League log files.

## Manual Execution
Alternatively, download the script and run it locally:

#### Windows

`python path\to\server_info.py`

#### Linux

`python3 /path/to/server_info.py`

#### Usage
Run the script, and it will automatically locate the Rocket League log files in the default directory and output server IPs along with their ping.

## License
Feel free to use this script. If you find it helpful, consider sharing it!

█▀▄▀█ █▀▀█ █▀▀▄ █▀▀ 　 █▀▀▄ █░░█ 　 █░█ █▀▀█ █░█ █▀▀ █░░█ 
█░▀░█ █▄▄█ █░░█ █▀▀ 　 █▀▀▄ █▄▄█ 　 ▄▀▄ █▄▄█ █▀▄ ▀▀█ █▀▀█ 
▀░░░▀ ▀░░▀ ▀▀▀░ ▀▀▀ 　 ▀▀▀░ ▄▄▄█ 　 ▀░▀ ▀░░▀ ▀░▀ ▀▀▀ ▀░░▀
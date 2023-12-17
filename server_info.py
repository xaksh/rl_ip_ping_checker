#!/usr/bin/env python3

import os
import glob
import platform
import re
import subprocess
import sys

def extract_between(text, start, end):
    try:
        start_idx = text.index(start) + len(start)
        end_idx = text.index(end, start_idx)
        return text[start_idx:end_idx]
    except ValueError:
        return None

def ping_ip(ip):
    os_name = platform.system()
    if os_name == "Windows":
        command = ['ping', '-n', '3', ip]
    else:
        command = ['ping', '-c', '3', ip]

    # Check Python version and use appropriate subprocess arguments
    if sys.version_info >= (3, 7):
        # For Python 3.7 and newer
        response = subprocess.run(command, capture_output=True, text=True)
    else:
        # For Python 3.6 and older
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        response.stdout = response.stdout.decode('utf-8')

    return parse_ping_response(response.stdout)

def parse_ping_response(response):
    os_name = platform.system()
    if os_name == "Windows":
        match = re.search(r'Average = (\d+)ms', response)
    else:
        match = re.search(r'(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)', response)

    if match:
        avg_ping = match.group(1) if os_name == "Windows" else match.group(2)
        return avg_ping
    else:
        return "N/A"

def process_log_file(file_path, pinged_ips):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if "GameURL" in line:
                server_name = extract_between(line, "ServerName=\"", "\"")
                server_ip = extract_between(line, "GameURL=\"", ":")
                if server_name and server_ip and server_name not in pinged_ips.get(server_ip, []):
                    if server_ip not in pinged_ips:
                        pinged_ips[server_ip] = [ping_ip(server_ip), {server_name}]
                        print_entry(file_path, server_name, server_ip, pinged_ips[server_ip][0])
                    elif server_name not in pinged_ips[server_ip][1]:
                        pinged_ips[server_ip][1].add(server_name)
                        print_entry(file_path, server_name, server_ip, pinged_ips[server_ip][0])

def print_entry(file_path, server_name, server_ip, ping):
    print(f"{os.path.basename(file_path):<40} {server_name:<30} {server_ip:<15} {ping} ms")

def main():
    print("ROCKET LEAGUE IP PING CHECKER")
    print("Made by XAKSH")
    print('-' * 90)

    os_name = platform.system()
    if os_name == "Windows":
        log_directory = os.path.join(os.getenv('USERPROFILE'), r'Documents\My Games\Rocket League\TAGame\Logs')
    else:  # Assuming Linux/Unix
        log_directory = os.path.expanduser('~/My Games/Rocket League/TAGame/Logs')

    if os.path.exists(log_directory):
        log_files = glob.glob(os.path.join(log_directory, '*.log'))
        print(f"{'Log File':<40} {'Server Name':<30} {'IP':<15} {'Ping':<5}")
        print('-' * 90)

        pinged_ips = {}
        for file_path in log_files:
            process_log_file(file_path, pinged_ips)
            print('-' * 90)
    else:
        print(f"Log directory not found: {log_directory}")
        print("Please ensure Rocket League is installed and logs are in the default location.")

if __name__ == "__main__":
    main()
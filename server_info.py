import os
import glob

def parse_log_file(file_path):
    server_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if "GameURL" in line:
                server_name = extract_between(line, "ServerName=\"", "\"")
                server_ip = extract_between(line, "GameURL=\"", ":")
                if server_name and server_ip:
                    server_data.append((server_name, server_ip))

    return server_data

def extract_between(text, start, end):
    try:
        start_idx = text.index(start) + len(start)
        end_idx = text.index(end, start_idx)
        return text[start_idx:end_idx]
    except ValueError:
        return None

def main():
    user_profile = os.getenv('USERPROFILE')
    if user_profile:
        log_directory = os.path.join(user_profile, r'Documents\My Games\Rocket League\TAGame\Logs')
        if os.path.exists(log_directory):
            log_files = glob.glob(os.path.join(log_directory, '*.log'))

            for file_path in log_files:
                server_data = parse_log_file(file_path)
                print(f"File: {os.path.basename(file_path)}")
                for name, ip in server_data:
                    print(f"Server Name: {name}, IP: {ip}")
                print('-' * 40)
        else:
            print(f"Log directory not found: {log_directory}")
            print("Please ensure Rocket League is installed and logs are in the default location.")
    else:
        print("Unable to determine the user profile directory.")

if __name__ == "__main__":
    main()

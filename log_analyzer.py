# log_analyzer.py
import re
from collections import Counter

def analyze_log(log_file):
    try:
        with open(log_file, 'r') as file:
            # Read all lines from the log file
            lines = file.readlines()

            # Count occurrences of each log level
            log_levels = re.findall(r'\b(?:INFO|WARNING|ERROR|DEBUG)\b', ' '.join(lines))
            log_level_counts = Counter(log_levels)

            # Print log level statistics
            print("Log Level Statistics:")
            for level, count in log_level_counts.items():
                print(f"{level}: {count} occurrences")

            # Example: Extract and print IP addresses
            ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', ' '.join(lines))
            unique_ip_addresses = set(ip_addresses)

            print("\nUnique IP Addresses:")
            for ip_address in unique_ip_addresses:
                print(ip_address)

    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")

if __name__ == "__main__":
    # Replace 'your_log_file.log' with the path to your log file
    log_file_path = 'your_log_file.log'
    analyze_log(log_file_path)

# log_analyzer.py
import re
from collections import Counter

def analyze_log(log_file):
    with open(log_file, 'r') as file:
        log_content = file.read()

        # Extract IP addresses from the log using a simple regex
        ip_addresses = re.findall(r'\d+\.\d+\.\d+\.\d+', log_content)

        # Count occurrences of each IP address
        ip_counts = Counter(ip_addresses)

        # Print the results
        print("IP Address\tOccurrences")
        print("-------------------------")
        for ip, count in ip_counts.items():
            print(f"{ip}\t\t{count}")

if __name__ == "__main__":
    # Replace 'example.log' with the actual log file name
    log_file = 'example.log'
    analyze_log(log_file)

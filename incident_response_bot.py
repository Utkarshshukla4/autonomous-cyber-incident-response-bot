import re
import time
import platform
import sys

# Linux log monitoring imports
try:
    from watchgod import watch
except ImportError:
    print("Please install watchgod: pip install watchgod")
    sys.exit(1)

# Windows Event Log imports
if platform.system() == "Windows":
    import subprocess
    import xml.etree.ElementTree as ET

# Regex to detect failed login attempts in Linux logs
FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for invalid user (?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

def incident_response(ip):
    print(f"[ALERT] Multiple failed login attempts detected from IP {ip}. Taking action...")
    block_ip(ip)

def block_ip(ip):
    print(f"Blocking IP address: {ip} (simulation)")

def monitor_linux_log(file_path, threshold=3, window_seconds=300):
    failed_attempts = {}
    print(f"Monitoring Linux log: {file_path}")
    for changes in watch(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        current_time = time.time()
        for line in lines:
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                ip = match.group('ip')
                timestamps = failed_attempts.get(ip, [])
                timestamps = [ts for ts in timestamps if current_time - ts < window_seconds]
                timestamps.append(current_time)
                failed_attempts[ip] = timestamps
                if len(timestamps) >= threshold:
                    incident_response(ip)
                    failed_attempts[ip] = []
        time.sleep(1)

def get_failed_windows_logins():
    """
    Fetch failed login attempts from Windows Security Event Log.
    Return list of tuples (ip, time).
    """
    query = '*[System[(EventID=4625)]]'
    cmd = ['wevtutil', 'qe', 'Security', f'/q:{query}', '/f:xml', '/c:20']
    result = subprocess.run(cmd, capture_output=True, text=True)
    events = result.stdout.split('<Event ')
    
    failed_ips = []
    for event_xml in events:
        if '</Event>' not in event_xml:
            continue
        event_xml = "<Event " + event_xml.split('</Event>')[0] + '</Event>'
        root = ET.fromstring(event_xml)
        ip = None
        time_created = None
        for data in root.iter('Data'):
            name = data.attrib.get('Name', '')
            if name == 'IpAddress':
                ip = data.text
            if name == 'SubjectUserName':
                # optionally get user
                pass
        for time_elem in root.iter('TimeCreated'):
            time_created = time_elem.attrib.get('SystemTime')

        if ip and ip != '::1' and ip != '127.0.0.1' and ip != '-':
            failed_ips.append((ip, time_created))
    return failed_ips

def monitor_windows_logs(threshold=3, window_seconds=300):
    print("Monitoring Windows Security Event Logs for failed logins...")
    failed_attempts = {}

    while True:
        current_time = time.time()
        failed_logins = get_failed_windows_logins()
        for ip, time_str in failed_logins:
            timestamps = failed_attempts.get(ip, [])
            timestamps = [ts for ts in timestamps if current_time - ts < window_seconds]
            timestamps.append(current_time)
            failed_attempts[ip] = timestamps
            if len(timestamps) >= threshold:
                incident_response(ip)
                failed_attempts[ip] = []
        time.sleep(10)  # query Windows logs every 10 seconds

if __name__ == "__main__":
    os_type = platform.system()
    print(f"Detected OS: {os_type}")
    if os_type == "Linux":
        log_path = "/var/log/auth.log"
        monitor_linux_log(log_path)
    elif os_type == "Windows":
        monitor_windows_logs()
    else:
        print(f"Unsupported OS: {os_type}")
        sys.exit(1)

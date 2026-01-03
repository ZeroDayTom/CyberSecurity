import re
from datetime import datetime
from dateutil import parser as date_parser

SSH_FAILED_REGEX = re.compile(
    r'(?P<date>\w+\s+\d+\s[\d:]+).*Failed password for (?P<user>\S+) from (?P<ip>\d+.\d+.\d+.\d+)'
)

def parse_auth_log(file_path):
    events = []

    with open(file_path, "r") as f:
        for line in f:
            match = SSH_FAILED_REGEX.search(line)
            if match:
                event = {
                    "timestamp": date_parser.parse(match.group("date")),
                    "user": match.group("user"),
                    "source_ip": match.group("ip"),
                    "event_type": "ssh_failed"
                }
                events.append(event)

    return events
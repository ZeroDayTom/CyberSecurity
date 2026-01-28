from collections import defaultdict
from datetime import timedelta

FAILED_THRESHOLD = 5
TIME_WINDOW_MINUTES = 5

def detect_bruteforce(events):

    alerts = []
    events_by_ip = defaultdict(list)
    alerted_ips = set()  # Avoid duplicate alerts

    for event in events:
        events_by_ip[event["source_ip"]].append(event)

    for ip, ip_events in events_by_ip.items():
        if ip in alerted_ips:  # Skip if already alerted
            continue
            
        ip_events.sort(key=lambda x: x["timestamp"])

        for i in range(len(ip_events)):
            window = [e for e in ip_events
                      if ip_events[i]["timestamp"] <= e["timestamp"] <= ip_events[i]["timestamp"] + timedelta(minutes=TIME_WINDOW_MINUTES)]

            if len(window) >= FAILED_THRESHOLD:
                alerts.append({
                    "alert_type": "brute_force_ssh",
                    "severity": "high",
                    "source_ip": ip,
                    "user": window[0]["user"],
                    "count": len(window),
                    "first_seen": window[0]["timestamp"].isoformat(),
                    "last_seen": window[-1]["timestamp"].isoformat()
                })
                alerted_ips.add(ip)  # Indicate as alerted
                break

    return alerts
import re
import subprocess

import pandas as pd


def ping_servers(hosts, n: int = 10) -> pd.DataFrame:
    rows = []

    for host in hosts:
        print(f"Pinging: {host}")
        result = subprocess.run()#TODO uzupełnić

        values = []

        for line in []: #TODO tu pobrać stdout z ping
            match = re.search(r"time[=<]([\d.]+)\s*ms", line)
            if match:
                values.append(float(match.group(1)))

        s = pd.Series(values, dtype="float64")

        rows.append({
            "server": host,
            "mean": s.mean(),
            "std": s.std(),
            "median": s.median(),
            "n": len(s),
        })

    return pd.DataFrame(rows)



def main():
    server_list = ["8.8.8.8", "o2.pl", "google.pl", "wp.pl"]
    stats = ping_servers(server_list)
    print(stats)

if __name__ == "__main__":
    main()
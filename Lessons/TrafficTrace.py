import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("network_traffic_logs.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

ip_counts = df["SourceIP"].value_counts()

plt.figure(figsize=(10, 5))
ip_counts.head(10).plot(kind="bar", color="skyblue")
plt.xlabel("Source IP Address")
plt.ylabel("Request Count")
plt.title("Top 10 Most Active IPs")
plt.xticks(rotation=45)
plt.show()

protocol_counts = df["Protocol"].value_counts()

plt.figure(figsize=(8, 5))
protocol_counts.plot(kind="bar", color=["blue", "red", "green", "orange"])
plt.xlabel("Protocol")
plt.ylabel("Count")
plt.title("Distribution of Protocols in Network Traffic")
plt.xticks(rotation=45)
plt.show()

port_scan_ips = df.groupby("SourceIP")["DestinationIP"].nunique()
suspicious_port_scanners = port_scan_ips[port_scan_ips > 50]
print("\n Possible Port Scanners (IPs targeting multiple destinations):")
print(suspicious_port_scanners)

large_packets = df[df["PacketSize"] > 1000]
("\n Large Packets Detected (Potential Data Exfiltration):")
print(large_packets[["Timestamp", "SourceIP", "DestinationIP", "PacketSize"]])
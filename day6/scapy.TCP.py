from scapy.all import TCP, sniff, IP

IFACE = None
bpt = "tcp"

def on_puket(pkt):
    if IP in pkt and TCP in pkt:
        src = pkt[IP].src 
        dst = pkt[IP].dst

        print(f"TCP {src}:{pkt[TCP].sport} -> {dst}:{pkt[TCP].dport}")

print(f"Sniffing iface={IFACE or 'default'} filter={bpt}")
sniff(filter=bpt, prn=on_puket, store=False, iface=IFACE)
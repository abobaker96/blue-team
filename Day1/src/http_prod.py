log_tokens= "Aug 12 10:06:01 sshd[1234]: Failed password for guest from 192.0.2.15 port 22 ssh2".split()
month, day, time, host,  *message_ports= log_tokens 
ip=log_tokens[9]
print (f"Date: {month} {day} {time}, Host: {host}, Ip: {ip}")
print (f"[MESSAGE]: {' '.join(message_ports)}")

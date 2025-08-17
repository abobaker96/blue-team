ip_string= "192.168.1.1"
port = "443"
port =int (port)
is_secure= bool(port == 443)
#print (is_secure)
log_tokens = "Aug 12 10:06:01 sshd[1234]: Failed password for " \
    "guest from 192.0.2.15 port 22 ssh2".split()
#print(log_tokens)
ipadd = log_tokens[9]
month, day, time, host , *message_ports = log_tokens
#print(log_tokens)
print(month,' ',day,' ',time,' ', host,' ',ipadd) 
print(f"[message]: {' '.join(message_ports)}")
#print(f"ip address :  {' '.join(ipadd)}")

print(ipadd)





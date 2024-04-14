import paramiko

# PC (destination) details
pc_hostname = 'your_pc_hostname_or_ip'
pc_username = 'your_pc_username'
pc_private_key = '/home/your_username/.ssh/id_rsa'  # Path to your private key file

# Raspberry Pi (source) details
pi_hostname = 'your_pi_hostname_or_ip'
pi_username = 'your_pi_username'
pi_file_path = '/path/to/your/file/on/pi'

# Establish SSH connection using private key for authentication
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Load private key
private_key = paramiko.RSAKey.from_private_key_file(pc_private_key)

# Connect using private key
ssh.connect(pc_hostname, username=pc_username, pkey=private_key)

# SCP (Secure Copy) the file from Raspberry Pi to PC
scp = paramiko.SFTPClient.from_transport(ssh.get_transport())
scp.put(pi_file_path, pi_file_path)

# Close the SSH connection
ssh.close()

print("File transfer successful!")

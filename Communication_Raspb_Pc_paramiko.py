import paramiko

# PC (destination) details
pc_hostname = 'fedora'
pc_username = 'khalil'
pc_password = 'Nounou2012'
pc_path = '/home/khalil'

# Raspberry Pi (source) details
pi_hostname = 'raspberry'
pi_username = 'khalil'
pi_password = 'khalil'
pi_file_path = '/home/khalil/test'

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(pc_hostname, username=pc_username, password=pc_password)

# SCP (Secure Copy) the file from Raspberry Pi to PC
scp = paramiko.SFTPClient.from_transport(ssh.get_transport())
scp.put(pi_file_path, pc_path)

# Close the SSH connection
ssh.close()

print("File transfer successful!")

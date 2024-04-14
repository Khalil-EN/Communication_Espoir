import paramiko

# PC (destination) details
pc_hostname = 'your_pc_hostname_or_ip'
pc_username = 'your_pc_username'
pc_password = 'your_pc_password'
pc_path = '/path/to/save/file/on/pc/'

# Raspberry Pi (source) details
pi_hostname = 'your_pi_hostname_or_ip'
pi_username = 'your_pi_username'
pi_password = 'your_pi_password'
pi_file_path = '/path/to/your/file/on/pi'

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

# Usage: In an admin powershell,
# Set-ExecutionPolicy RemoteSigned
# .\WLS2.ps1 <PORT>

$port=$args[0]
echo $port

$host = wsl bash -c " ip addr show dev eth0 | grep 'inet ' | grep -Eo '([0-9]{1,3}[\.]){3}[0-9]{1,3}' | head -1"
echo $host

netsh interface portproxy add v4tov4 listenport=$port listenaddress=0.0.0.0 connectport=$port connectaddress=$host

echo Success
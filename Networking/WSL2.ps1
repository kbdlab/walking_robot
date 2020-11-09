# Usage: powershell .\WLS2.ps1 <PORT>

$port=$args[0]
echo $port

$remoteport = wsl bash -c " ip addr show dev eth0 | grep 'inet '"
$wsl = $remoteport -match '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}';
echo $wsl

netsh interface portproxy add v4tov4 listenport=$port listenaddress=0.0.0.0 connectport=$port connectaddress=$wsl

echo Success
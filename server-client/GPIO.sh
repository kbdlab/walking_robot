echo 11 > /sys/class/gpio/export

echo out > /sys/class/gpio/gpio11/direction

while :; do
    echo 1 | tee /sys/class/gpio/gpio11/value
    sleep 1s
    echo 0 | tee /sys/class/gpio/gpio11/value
    sleep 1s
done
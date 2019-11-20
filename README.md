# [연세대 WiFi 공식 매뉴얼](https://yis.yonsei.ac.kr/_res/ics/etc/Yonsei_Manual_KO.pdf)

# wpa_supplicant.conf 설정 필수

몇몇 분들에게 동영상 튜토리얼에 있는 wpa_supplicant.conf가 필요 없다고 말씀드렸는데, 꼭필요한 것으로 드러났습니다.
잘못 말씀드려서 죄송합니다.
안 하면 설치 시 설정한 WiFi외에 다른 WiFi에는 연결이 안 된다고 합니다.

# apt upgrade 시 linux-firmware 문제

저희가 팀 뷰어를 깔려면
`sudo apt update
sudo apt upgrade`
를 해야 한다고 말씀을 드렸는데,
upgrade는 꼭 필요하지는 않습니다.
팀 뷰어를 깔고 추후에 하셔도 됩니다.

현재 upgrade 시 linux-firmware라는 패키지를 업그레이드 하다가 라즈베리 파이가 다운되거나
`Sub-process /usr/bin/dpkg returned an error code (1)`
메시지가 뜨는 오류가 수업에 사용되는 라즈베리 파이 보드와 Ubuntu Mate 버전에 대해서 커뮤니티에 보고되고 있습니다.
이런 현상의 해결책은 이 [링크](https://ubuntu-mate.community/t/error-updating-ubuntu-mate-18-04-on-pi-3b/20001/4
)에서 찾을 수 있습니다.
내용을 미리 말씀드리면,
`sudo dpkg -i --force-all /var/cache/apt/archives/linux-firmware-raspi2_1.20190215-0ubuntu0.18.04.1_armhf.deb`
명령어를 사용하시면 됩니다.

# 라즈베 파이에 opencv 설치하기
'sudo apt-get install python-opencv' 

# pip 설치

pip 는 파이썬 패키지 관리자로 필요한 패키지를 편리하게 설치/관리할 수 있게 해줍니다.
'sudo apt-get install python-pip' 으로 설치 가능하며, 중간에 오류 발생 시 'sudo apt update' 를 한 번 해주시고 다시 설치를 진행하면 됩니다. 우분투 18.04 이후로는 picamera가 기본 패키지가 아니어서 pip으로 설치하신 후에 'pip install picamera'로 해주시고, 만약 권한 문제가 생기면 해당 코드에 '--user'를 붙이면 됩니다.


# Repository 관련

## Branch 분리
`2019` branch로 가시면 2019년 수업 자료만 보실 수 있습니다.
`main` branch는 2020년 수업에서 사용한 자료들만으로 새로 구성할 예정입니다.

## Issues
Issue들이 해결되는 대로 Close 하고 있습니다. 과거의 Issue들을 보고 싶으시면 closed를 포함해서 보는 버튼을 눌러 읽어보세요.

# WSL
WSL에는 버전 1과 2가 존재하는데, 2는 성능이 뛰어나지만 본 수업에서 WSL 상에서 서버를 구동하려면 복잡한 설정이 필요합니다.
수업 중에는 [마이크로소프트의 지침](https://docs.microsoft.com/en-us/windows/wsl/install-win10) 중 WSL 2로 업그레이드 하는 부분은 건너뜀으로써 WSL 1을 설치하라고 말씀을 드렸는데, 기본값으로 WSL 2가 깔리는 컴퓨터들이 발견되었습니다.
이럴 경우, 또는 WSL 2 사용하고자 하는 분들은 올려드린 [PowerShell script](https://github.com/kbdlab/walking_robot/blob/master/Networking/WSL2.ps1)를 사용하시면 됩니다. 자세한 사용법은 [Networking 폴더](https://github.com/kbdlab/walking_robot/tree/master/Networking)를 참조하세요.

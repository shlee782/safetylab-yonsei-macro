# 연세대학교 연구실 환경안전관리시스템 일상점검 매크로 (safetylab-yonsei-macro)

본 repository는 연세대학교 연구실 환경안전관리시스템의 일상점검에 필요한 타이핑 및 클릭에 대한 매크로로 파이썬을 기반으로 작성되었습니다.

- - -
## 사용법

1. input.txt에 매크로 사용 시 필요한 내용들을 입력합니다. (각 사항의 colon(:) 다음에 한 칸 띄우고 내용을 적습니다.)
- year, month, id, nam에 각각 점검 연도, 점검 월, 학번, 이름을 적습니다.
- check_list에는 각 점검사항(일반사항, 전기안전, 소방안저, 가스안전, 화공안전, 생물안전)에 대해서 적합(1), 부적합(2), 미해당(3)를 표시한다. 이를테면, 각 사항에 대해서 적합, 적합, 적합, 미해당, 미해당, 미해당, 미해당으로 표기하고 싶은 경우 'check_list: 1 1 1 3 3 3 3'이라고 하면 됩니다.
- lab에는 점검해야할 연구실을 표기하면 됩니다. 'safetylab.yonsei.ac.kr'에서 연구실 선택 란에 점검이 필요한 연구실이 두번째 란에 있다면, 'lab: 2'라고 하면 됩니다.

2. main.py를 실행시킵니다. 이때, 순서대로 'day: '와 'check_type: '이 출력됩니다. 전자에서는 점검 일자를 입력하면 되고, 후자에서는 점검을 해야할 날짜인 경우 'a'를 공휴일 등의 이유로 점검이 필요하지 않은 날짜인 경우 'b'라고 입력하면 됩니다.

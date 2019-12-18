'''
# 절차적 프로그램 실습
# 간단한 게임을 구현하여
# 긴 단위의 프로그램을 작성하고, 절차적 프로그램을 이해한다.
# 머드 게임 스타일로 터미널에서 입력하면서 게임을 진행.
# 목적, 파이썬 타입, 연산, 조건, 반복, 흐름제어 등을 프로그램을 개발하면서 
# 심화 학습한다.
# ---------------------------------------------------------------------
# step1 게임이 시작하면 "Enjoy custom Game world"라는 문구를 출력한다
c
# step 3
    3-1 플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
    3-2 입력에 대한 처리는 step2와 동일하다
    3-3 플레이어의 이름은 player_name이라는 변수에 담는다.
# step4
    4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다."    
    4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
    4-3 게임 난이도는 game_level이라는 변수에 담는다.
'''
# step1 게임이 시작하면 "Enjoy custom Game world"라는 문구를 출력한다
print("Enjoy custom Game world")
# step2 
    # 2 - 1" 게임 제목을 입력하시오, 단 20 자 이내로 입력 가능합니다. "
    # 2 - 2 " 사용자가 입력할때까지 무제한으로 대기한다"
    # 2 - 3 " 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다"
    # 2 - 4 " 20자 이상 입력하면 "20자가 초과 되었습니다."출력하고, 다시 입력 대기 한다"
    # 2 
while True :
    tmp = input(' 게임 제목을 입력하시오,\n \
        단 20 자 이내로 입력 가능합니다. \n \
            ').strip()
    if not tmp:
        print('정확하게 입력하세요')
    elif len(tmp)>20:
        
        print("20자가 초과되었습니다.")
        
    else:
        gameTitle = tmp
        
        break
print('gameTitle',gameTitle)
# step 3
    #3-1 "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
    #3-2 입력에 대한 처리는 step2와 동일하다
    #3-3 플레이어의 이름은 player_name이라는 변수에 담는다.

while True :
    tmp = input("플레이어의 닉네임을 입력하시오,\n \
        단 15 자로 제한한다. \n \
            " ).strip()
    if not tmp:
        print('정확하게 입력하세요')
    elif len(tmp)>15:
        
        print("15자가 초과되었습니다.")
        
    else:
        player_name = tmp
        
        break
print('player_name',player_name)
# step4
    #4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다."    
    #4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
    #4-3 게임 난이도는 game_level이라는 변수에 담는다.
while True :
    tmp = input("게임 난이도를 입력하시오 ,\n \
        단 1~9까지 정수 형태로 제한한다. \n \
            " ).strip()
    if not tmp.isdecimal():
        print('정확하게 입력하세요')
    elif int(tmp)==0:
        print('정확하게 입력하세요')
    elif len(tmp)>1:
        
        print("1자가 초과되었습니다.")
        
    else:
        game_level = tmp
        
        break
print('game_level',game_level)




'''
# 절차적 프로그램 실습
# 간단한 게임을 구현하여
# 긴 단위의 프로그램을 작성하고, 절차적 프로그램을 이해한다.
# 머드 게임 스타일로 터미널에서 입력하면서 게임을 진행.
# 목적, 파이썬 타입, 연산, 조건, 반복, 흐름제어 등을 프로그램을 개발하면서 
# 심화 학습한다.
# ---------------------------------------------------------------------
# step1 게임이 시작하면 "Enjoy custom Game world"라는 문구를 출력한다
# step2 
    # 2 - 1" 게임 제목을 입력하시오, 단 20 자 이내로 입력 가능합니다. "
    # 2 - 2 " 사용자가 입력할때까지 무제한으로 대기한다"
    # 2 - 3 " 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다"
    # 2 - 4 " 20자 이상 입력하면 "20자가 초과 되었습니다."출력하고, 다시 입력 대기 한다"
    # 2 - 5 " 20자이내로 입력하면 game_Title라는 변수에 게임 제목을 담고 다음 3단계로 진입한다"
# step 3
    3-1 플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
    3-2 입력에 대한 처리는 step2와 동일하다
    3-3 플레이어의 이름은 player_name이라는 변수에 담는다.
# step4
    4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다."    
    4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
    4-3 게임 난이도는 game_level이라는 변수에 담는다.
'''
# -----------------------------------------------------------------------
# step1
print("Enjoy custom Game world")
# step2
    # 2 - 1" 게임 제목을 입력하시오, 단 20 자 이내로 입력 가능합니다. " << 2-2 이랑 순서 바꿔야됨
        # > 매번 입력을 대기 할 때 마다 해당 프럼프트를 출력하겠다.   
# 2 - 2 " 사용자가 입력할때까지 무제한으로 대기한다" ( 그냥 넘어가면됨)
while True : # 반드시 내부에 break가 있어야 한다.
    # 사용자가 엔터키를 칠때까지코드를 블럭하고 있다.
    tmp = input(' 게임 제목을 입력하시오, \n \
        단 20 자 이내로 입력 가능합니다. \n \
            ').format(GAME_TITLE_LEN_MAX).strip()
    if not tmp:# 2 - 3 " 아무것도 입력하지 않고 엔터를 치면 
        #스페이스바를 몇번 치고 엔터를 친것도 잡는다.<< 
        # "정확하게 입력하세요!" 출력하고 다시 입력 대기한다"
        print('정확하게 입력하세요')
        pass
    elif len(tmp)>20:# 2 - 4 " 20자 이상 입력하면 
        # "20자가 초과 되었습니다."출력하고, 다시 입력 대기 한다"
        print("20자가 초과되었습니다.")
        pass
    else:# 2 - 5 " 20자이내로 입력하면
         # game_Title라는 변수에 게임 제목을 담고 다음 3단계로 진입한다"
        gameTitle = tmp
         # 다음 3단계로 진입한다> 2단계
        break
        pass
    pass
# 3단계
# gmaeTilte이 정의된 곳 > while 안에 else안에서 정의
# while 밖에서도 사용이 가능하다?
# 함수나 클레스 내부에서 저으이된 변수가 아닌 변수들은 
# 모두 전역변수 이다 .(어느곳에서든 사용가능하다 )< - variable scope(범위)
print('gameTitle',gameTitle)


a.
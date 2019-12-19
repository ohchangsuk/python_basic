while True :
    tmp = input("게임 난이도를 입력하시오 ,\n \
        단 %d~%d까지 정수 형태로 제한한다. \n \
            "%(GAME_LEVEL_MIN, GAME_LEVEL_MAX,) ).strip()
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
'''
# step4
    4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다."    
    4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
    4-3 게임 난이도는 game_level이라는 변수에 담는다.
# step4
    #4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다."    
    #4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
        #사용자가 넣을수 있는 케이스를 고려하여 점점 범위가 줄어들게 배치
        #(공백입력, 1~9 이외의 값, 정수가 될수 없는 값, 정확하게 넣을 경우, 우선 순위는 포괄적인 순위에서 점점 걸러지게 , 점층적?
        # 순서 > 1공백입력, 2정수가 될수 없는 값, 3.1~9이외의 값, 4정확하게 넣을 경우)
    #4-3 게임 난이도는 game_level이라는 변수에 담는다.
    '''
if condition:# 공백은 잡는다 컷
    pass 
elif:# 뭔가는 들어있다. >정수가 안되면 컷
    continue
    pass
# 정수 변환 
if condition: # 1~~9 이외의값이면 컷
    pass
else:# 정상값
    pass
##########################
if condition: # 공백이면 컷
    pass
elif condition: #정수 아니면 컷
    pass
else condition: # 정수가 될수 있는 놈들
    # 정수 변환
    if condition: # 1~9가 아닌 값 컷
        pass
    else     # 정확한 입력
        pass
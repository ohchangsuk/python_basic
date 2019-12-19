GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE =True
if not IS_DEV_MODE: # release 버전의 코드가 작동
    # step1
    print( "Enjoy Custom Game world" )
    # step2 
    while True:
        tmp = input("게임 제목을 입력하시오, 단 {}자 \이내로 입력 가능합니다. => ".format(GAME_TITLE_LEN_MAX)).strip()       
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.") 
        else:
            gameTitle = tmp
            break
    print( 'gameTitle', gameTitle )
    # step 3
    while True:
        tmp = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n=>" % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>PLAYER_NAME_LEN_MAX:
            print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
        else:
            player_name = tmp
            break
    # step4
    while True:
        tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            print('정확하게 입력하세요')
            continue
        if not tmp.isnumeric():
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue
        tmp = int(tmp)
        if tmp>9 or tmp<1:
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue    
        game_level = tmp
        break
else:
# 매번 입력받아서 테스트하기 시간이 많이 소요 ㅗ디므로 , 값을 고정하여 개발
    gameTitle  = '테스트 게임'
    player_name  ='guest'
    game_level = 1
# step 5
print( '-'*20 )
print( '현재 까지 입력 상황' )
print( 'gameTitle',   gameTitle )
print( 'player_name', player_name )
print( 'game_level',  game_level )
print( '-'*20 )
# step 6
# 인트로 (가로길이 40칸)
'''
========================================

+           게임제목(중앙정렬)           +
+            lv 레벨값                  +
+        "플레이어이름"의 연대기         +

========================================
           press any key !!
'''
print( '-'*40 )
print( '+{0:^38}+'.format(gameTitle) )
print( '+{0:^38}+'.format('lv : %s' % game_level) )
print( '+{0:^34}+'.format('"%s의 연대기'% player_name) )
print( '-'*40 )
print( '{0:^40}'.format('press any key!!') )















































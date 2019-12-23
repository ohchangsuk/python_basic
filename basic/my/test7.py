# 예외처리
# 코드는 잠재적으로 오류를 가질수 있다.
# 이때, s/w를 다운되지 않고, 혹은 그 정보를 수집하고,
# 문제없이 다음 단계로 진행 시키는 방법



'''
try:
    pass
except expression as identifier:
    pass
else:
    pass
finally:
    pass
'''
'''
# case1
try:# 예외가 발생할 만한 코드를 감싼다.
    print(1)
    print(1/0)
    print(2)
except Exception as e:# 예외가 발생하면 호출
    print(3,e)
else:# 예외없이 정상적으로 끝까지 작동되면 호출
    print(4)
finally:# 무조껀 수행
    print(5)
print(6)
'''
# case2
try:# 예외가 발생할 만한 코드를 감싼다.
    print(1)
    #print(1/0)
    print(2)
except Exception as identifier:# 예외가 발생하면 호출
    print(3,e)
else:# 예외없이 정상적으로 끝까지 작동되면 호출
    print(4)
finally:# 무조껀 수행
    print(5)
print(6)
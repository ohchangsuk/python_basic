# 모듈 내부에는 변수, 함수, 클레스등이 여러개 존재할수 있다
# 변수
PI = 3.14
name = '17시30분'
# 함수
def add( a, b):
    return a + b
# 클레스
# 클래스는 새로운 자료구조를 정의하는 형태
# 데이터 뿐만 아니라 행동(함수)도 같이 가질수 있는 자료 구조,
#맴버 변수 초기화(옵션)
#맴버 변수 초기화(옵션)
class Person:
    name = None
    def getName(self):
        print('person의 이름은 %s 역입니다' %self.name)
    def __init__( self, name ):
        print('객체 생성')
        #클레스 내부에서 맴버들을 사용할 경우 self.변수/ self.함수
        #맴버 변수 초기화
        self.name = name
    
    
    '''
    - SPEED, HP, EXP, LEVEL,COLOR, x, y 등 속성이 있다.
    
    
    '''



if __name__=='__main__':




if __name__ == '__main__':
    # 테스트
    print('본 모듈의 개발자가 직접 구동시 작동')
    print( add(1, 2) )
    A()
else:
    # 제 3자가 이 모듈을 가져다가 사용할때
    # __name__ => 파일명 => mod
    # 'mod' == '__main__' => False가 되니 else 코드를 타게 된다
    pass
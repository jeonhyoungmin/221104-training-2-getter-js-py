# 생성자 함수 연습하기 training-2
# 인스턴스의 프로퍼티(property)를 만들어주는 def __init__(): 함수
class RgbaColor:
    def __init__(self, red, green, blue, alpha = 1):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
    # 생성자 함수의 주요 기능 중 하나인 getter 기능
    # 파이썬은 새로운 키워드로 함수를 만드는 것 대신
    # 데코레이터 라는 개념으로 해당 함수의 성격을 정의 한다.
    # 아래의 @property라는 작성법이 대표적인 데코레이터 문법
    @property
    def rgba(self):
        # 템플릿 문자열을 .format()이라는 함수로 지원하는 것을 확인 할 수 있다.
        return 'rgba({}, {}, {}, {})'.format(self.red, self.green, self.blue, self.alpha)

pracRgbaColor = RgbaColor(200, 200, 200)
print(pracRgbaColor.__dict__) # Q-3 어떤 값이 나오는지 테스트 해보기
print(pracRgbaColor.rgba) # Q-4 어떤 값이 나오는지 테스트 해보기
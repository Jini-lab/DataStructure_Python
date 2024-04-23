class Sample:
  counter2 = 0
  def __init__(self):
    self.counter = 0

  def numEven(self, n):
    for k in range(n):
      if k % 2 == 0:
        self.counter +=1
        Sample.counter2 +=1

s1 = Sample()
s2 = Sample()
s1.numEven(15)
s2.numEven(15)
print(s1.counter, s1.counter2)

# 출력: 8 16
# counter2( Sample.counter2 )는 해당 클래스에서 하나만 존재하고,수 = 전역 변수
# self.counter은 각 객체마다 하나씩 존재 = 각 객체의 지역변수

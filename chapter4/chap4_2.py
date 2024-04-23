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

# numEven 메서드에서 self.counter를 사용하려면 self를 메서드의 첫 번째 매개변수로 가져와야 합니다.
# 매개변수로 호출해야지만, numEven 메소드에서 self를 통해 해당 인스턴스의 속성에 접근할 수 있습니다. 

class Sample:
    def __init__(self):
        self.counter =0
        
    def numEven(self, n):
        for k in range(n):
            if k % 2 == 0 :
                self.counter += 1
        return self.counter

    
s = Sample()
print("# of even integers =", s.numEven(15))


# numEven 메서드에서 self.counter를 사용하려면 self를 메서드의 첫 번째 매개변수로 가져와야 합니다.
# 매개변수로 호출해야지만, numEven 메소드에서 self를 통해 해당 인스턴스의 속성에 접근할 수 있습니다. 

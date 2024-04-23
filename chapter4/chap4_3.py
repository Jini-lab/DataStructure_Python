
# 순회 가능 클래스와 순회자의 구조 흐름을 보기 위한 것으로 코드 흐름만 본다.
# chapter5에 코드 설명 나옴.


class CircularLinkedList:
	def __init__(self):
		self.__tail = ListNode("dummy", None)
		self.__tail.next = self.__tail
		self.__numItems = 0

	def insert(self, i:int, newItem) -> None:
		if (i >= 0 and i <= self.__numItems):
			prev = self.getNode(i - 1)
			newNode = ListNode(newItem, prev.next)
			prev.next = newNode
			if i == self.__numItems:
				self.__tail = newNode
			self.__numItems += 1
		else:
			print("index", i, ": out of bound in insert()") 


	def __iter__(self):  # 순회자 객체 생성, 순회자 시작
		return CircularLinkedListIterator(self)

class CircularLinkedListIterator:

        # 메서드 __iter__() 수행한 결과로 클래스 Iterator 객체(순회자) 하나 만들어짐. 
	def __init__(self, alist):
		self.__head = alist.getNode(-1) 
		self.iterPosition = self.__head.next  


	# 객체에서 원소 하나 필요할 때마다 순회자의 메서드 __next__() 호출	
	def __next__(self):
		if self.iterPosition == self.__head:
			raise StopIteration
		else: 
			item = self.iterPosition.item
			self.iterPosition = self.iterPosition.next
			return item

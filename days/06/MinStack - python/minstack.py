class MinStack:

  def __init__(self):
    """
      initialize your data structure here.
      """
    self.data = []

  def push(self, x: int) -> None:
    self.data.append(x)

  def pop(self) -> None:
    self.data.pop(0)

  def top(self) -> int:
    if self.data:
      return self.data[-1]

  def getMin(self) -> int:
    min_num = float('inf')

    for num in self.data:
      if num is None:
        continue
      if num < min_num:
        min_num = num
    return min_num

# # [[],[-2],[0],[-3],[],[],[],[]]
# minStack = MinStack()
# minStack.push(None)
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# minStack.push(None)
# minStack.push(None)
# minStack.push(None)
# print(f"Original List: {minStack.data}")
# print(minStack.getMin()) # return -3
# minStack.pop()
# minStack.top()   # return 0
# minStack.getMin() # return -2
#
# print(minStack.data)

# minStack = MinStack()
# minStack.push(1)
# minStack.push(2)
# minStack.push(3)
# minStack.push(4)
# minStack.push(5)
# minStack.push(6)
# minStack.push(7)
# minStack.pop()
# print(minStack.data)
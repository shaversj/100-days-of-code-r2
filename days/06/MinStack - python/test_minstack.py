import unittest
from minstack import MinStack


class MyTestCase(unittest.TestCase):

  def test_push(self):
    # Given
    minStack = MinStack()
    minStack.push(None)
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.push(None)
    minStack.push(None)
    minStack.push(None)

    expected_output = [None, -2,0,-3,None,None,None]
    self.assertEqual(minStack.data, expected_output)

  def test_top(self):
    # Given
    # [1, 2, 3, 4, 5, 6, 7]
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(3)
    minStack.push(4)
    minStack.push(5)
    minStack.push(6)
    minStack.push(7)

    expected_output = 7
    self.assertEqual(minStack.top(), expected_output)

  def test_pop(self):
    # Given
    # [1, 2, 3, 4, 5, 6, 7]
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(3)
    minStack.push(4)
    minStack.push(5)
    minStack.push(6)
    minStack.push(7)

    expected_output = [2, 3, 4, 5, 6, 7]

    minStack.pop()
    self.assertEqual(expected_output, minStack.data)

  def test_getmin(self):
    minStack = MinStack()
    minStack.push(None)
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.push(None)
    minStack.push(None)
    minStack.push(None)

    self.assertEqual(-3, minStack.getMin())



if __name__ == '__main__':
  unittest.main()

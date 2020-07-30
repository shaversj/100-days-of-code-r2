class Stack:

    def __init__(self):
        self.stack = []

    def push(self, nums):

        if type(nums) is not list:
            self.stack.append(nums)
        else:
            for num in nums:
                self.stack.append(num)

    def pop(self):
        idx = -1
        len_of_stack = -len(self.stack)
        popped_nums = []

        while idx >= len_of_stack:
            if idx % 2 == 0:
                self.stack.pop(-1)
            else:
                popped_nums.append(self.stack.pop(-1))

            idx -= 1

        return " ".join(str(num) for num in popped_nums)






s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.pop())

p = Stack()
p.push([10, -2, 3, 4])
print(p.pop())
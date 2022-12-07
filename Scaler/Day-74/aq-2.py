from collections import deque


class Stack(object):

    def __init__(self) -> None:
        self.container = deque()

    def insert(self, value):
        self.container.append(value)

    def top(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()

    def get_length(self):
        return len(self.container)

    def printstack(self):
        print(self.container)

    def is_empty(self):
        return 1 if self.get_length() == 0 else 0


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):

        N = len(A)
        R = [-1] * N

        S = Stack()

        # Add first element in the stack to keep checkin from nex
        if A[0] is not None:
            S.insert(0)

        for i in range(1, N):
            while not S.is_empty() and A[S.top()] >= A[i]:
                S.pop()
            if not S.is_empty():
                R[i] = S.top()
            S.insert(i)

        return R

    def nextSmaller(self, A):

        N = len(A)
        R = [N] * N

        S = Stack()

        if N > 0:
            S.insert(N-1)

        for i in range(N-2, -1, -1):
            while not S.is_empty() and A[S.top()] >= A[i]:
                S.pop()
            if not S.is_empty():
                R[i] = S.top()
            S.insert(i)

        return R

    def largestRectangleArea(self, A):

        PS = self.prevSmaller(A)
        NS = self.nextSmaller(A)
        N = len(A)
        ANS = float('-inf')
        for i in range(N):
            RC = A[i] * (NS[i]-PS[i]-1)
            ANS = max(ANS, RC)

        return ANS


A = [3, 4, 5, 4, 2, 3]
A = [2, 1, 5, 6, 2, 3]
A = [31, 25, 94, 95, 50, 71]
X = Solution()


PS = X.prevSmaller(A)
NS = X.nextSmaller(A)
#R = X.largestRectangleArea(A)

print(PS)
print(NS)

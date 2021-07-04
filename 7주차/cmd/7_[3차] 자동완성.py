from collections import deque
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}  # dictionary
        self.val = 0
        self.flag = False

class Trie:
    def __init__(self):
        self.head = Node(None)
    def insert(self, string):
        cur = self.head
        for idx, s in enumerate(string):
            if s not in cur.children:
                cur.children[s] = Node(s)
                cur.children[s].val = cur.val
            else:
                cur.children[s].val = cur.val + 1
            cur = cur.children[s]
            if idx == len(string) - 1:  # 마지막글자 표시
                cur.flag = True
        cur.data = string
    def DFT(self):
        cur = self.head
        stack = [cur]
        while stack:
            cur = stack.pop()
            for i in cur.children.keys():
                if cur.children[i].val < cur.val:
                    cur.children[i].val = cur.val
                stack.append(cur.children[i])
    def BFT(self):
        answer = 0
        cur = self.head
        q = deque()
        q.append(cur)
        while q:
            cur = q.popleft()
            if cur.flag == True:  # 단어의 끝
                if cur.children:
                    answer += cur.val
                else:
                    answer += cur.val + 1
            for i in cur.children.keys():
                q.append(cur.children[i])
        return answer

def solution(words):
    # trie algorithm
    words = sorted(words)
    trie = Trie()
    for word in words:
        trie.insert(word)
    trie.DFT()
    return trie.BFT()
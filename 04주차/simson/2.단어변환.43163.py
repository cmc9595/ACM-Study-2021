answer = 51
def dfs(cur, target, words, index):
    global answer
    if cur == target:
        answer = min(index, answer)
        return
    for cand_word in get_change_list(cur, words):
        dfs(cand_word, target, [ word for word in words if word != cand_word ], index + 1)
        
    return
def get_change_list(cur, words):
    list = []
    for word in words:
        diff = 0
        for i in range(len(word)):
            if cur[i] != word[i]:
                diff += 1
        if diff == 1:
            list.append(word) 
    return list

def solution(begin, target, words):
    global answer
    if not target in words:
        return 0
    dfs(begin, target, words, 0)
    return answer

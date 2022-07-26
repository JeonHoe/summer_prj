# 연습문제
korean, english, math, science = 100, 86, 81, 91
def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, math, science)
print('높은 점수 :', max_score)
max_score = get_max_score(english, science)
print('높은 점수 :', max_score)

# 심사문제
korean, english, math, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)

def get_average(**kwargs):
    result = 0
    for score in kwargs.values():
        result += score
    return result / len(kwargs)
min_score, max_score = get_min_max_score(korean, english, math, science)
average = get_average(korean=korean, english=english, math=math, science=science)
print('낮은 점수 : {0:.2f}, 높은 점수 : {1:.2f}, 평균 점수 : {2:.2f}'.format(min_score, max_score, average))
min_score, max_score = get_min_max_score(english, science)
average = get_average(english=english, science=science)
print('낮은 점수 : {0:.2f}, 높은 점수 : {1:.2f}, 평균 점수 : {2:.2f}'.format(min_score, max_score, average))

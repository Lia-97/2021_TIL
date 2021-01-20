# # K번째수
# def solution(array, commands):
#     answer = []
#     for command in commands:
#         new_array = array[command[0]-1:command[1]]
#         new_array.sort()
#         answer.append(new_array[command[2]-1])
#     return answer
#
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# # 문자열 내 p와 y의 개수
#
# def solution(s):
#     sentence = s.lower()
#     if sentence.count('p') == sentence.count('y'):
#         return True
#     else:
#         return False
#
# print(solution('Pyy'))

# # 두 정수 사이의 합
#
# def solution(a, b):
#     answer = 0
#     if a <= b:
#         for i in range(a, b+1):
#             answer += i
#     if a > b:
#         for i in range(b, a+1):
#             answer += i
#     return answer
#
# print(solution(5,3))
#
# # 두 정수 사이의 합 (또 다른 풀이)
#
# def solution(a, b):
#     if a > b:
#         a, b = b, a
#     return sum(range(a, b+1))

# 문자열 내 마음대로 정렬하기


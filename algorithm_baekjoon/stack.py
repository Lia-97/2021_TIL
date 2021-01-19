# # 10773번 (제로)
#
# K = int(input())
# num = []
# for _ in range(K):
#     i = int(input())
#     if i != 0:
#         num.append(i)
#     else:
#         num.pop()
# print(sum(num))

# # 9012번 (괄호)
#
# T = int(input())
# for _ in range(T):
#     sentence = list(input())
#     sum = 0
#     for i in sentence:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')

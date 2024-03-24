# dic = {}
# name = input()
# height = eval(input())
# dic['name'] = height

# print('小明', dic['小明'])


# F = []
# F.append(0)
# F.append(1)
# N = eval(input())
# for i in range(N-2):
#     F.append(F[i] + F[i+1])
# print(F)

#输入指定的n
n = eval(input())

#指定输入n个数，换行间隔
score = []
for i in range(n):
    a = eval(input())
    score.append(a)
# score.sort()
# print(score)

#计算去掉一个最高分和最低分的平均值
score = score.sort()
score.pop(0)
score.pop(-1)
avg = sum(score) / len(score)

#输出最后得分
print(avg)
a,b,c=map(int,input().split())
num=a*b*c
def f(num):
    if num<10:
        return num
    return num+f(num%10)

print(f(num))
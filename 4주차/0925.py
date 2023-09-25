## 주민번호
ssno = "881120 - 1068234"
# 출생일은 1988년 11월 20일이고 성별은 1입니다.
yy = ssno[0:2]
mm = ssno[2:4]
dd = ssno[4:6]
s = ssno[9]
ssno = "881120 - 1068234"

print(f"출생일은 {yy}년 {mm}월 {dd}일이고, 성별은 {s}입니다.")

a = "a:b:c:d"
a = a.replace(":","#") # : -> #로 변경
print(a)

a = [1,3,5,4,2]
a.sort(reverse = True) #순서정렬
print(a)

a = ["Life", "is", "too", "short"]
result = " ".join(a)
print(result)
#스크릿 메서드

b = [1,2,3]
b.append(0)
print(b)

b2 = (1, 2, 3)
# b2.a  튜플은 append가 없다.
b3 = (4, 5)
b1 = b2+b3
print(b1)

print("="*20)
v = (1,2,3)
v = print(breakpoint)

lang = {1:"Python"}  # 오류
lang = {"name":"Python"} 

grade = {"kor": 90, "eng": 80, "math":70}

print(grade["eng"])
print(grade.keys())
print(grade.values())
print(grade.items())
# ^^
print(grade["eng"])
print(grade.keys())
eng_val = list(grade.values())
print(eng_val[1])
print(grade.items())

lst = [1,2,3,1,5,7,5]
lst = list(lst)
lst = set(lst)
a = [1,2,3]
b = a # a[:] 도 가능
b[1] = 999
print(a)

#if문 루프

#money = True
#if money:
#    print("택시타고 가라")
#    print("돈이 있으니")
#else:
#    print("걸어가라")


money = False # or True, False ,1,0
if money==True: #확실하게 true false
    print("택시타고 가라")
    print("돈이 있으니")
else:
    print("걸어가라")

print("="*10)

if 10==10.0:
    print("택시타고 가라") #데이터 타입이 다른데 True가 나옴
    print("돈이 있으니")
else:
    print("걸어가라")

print("="*10)


pocket = ["paper", "money", "cellphone"]
if "money" in pocket:
    print("돈이 있다.")
elif "card" in pocket:
    print("카드가 있다.")
else:
    print("아무것도 없다.")

score = 100
msg = "success" if score >= 60 else "failure"

## ^^^

if score >= 60:
    msg = "success"
else:
    msg = "failure"


ist= [1,2,3]
if ist == True:
    print(f"{ist} is True")
elif ist == False:
    print(f"{ist} is False")
else:
    print(f"{ist}" is None)


cnt = 0 
sum_amt = 0
while cnt < 10:
    sum_amt = sum_amt + cnt
    cnt = cnt +1
print(f"Sum amount is : {sum_amt}")


##구구단 while
i = 1
while i < 9:
    i = i + 1
    j = 1
    while j < 10:
        print(i, 'X', j, '=', i*j)
        j = j + 1
    if j == 9:
        break


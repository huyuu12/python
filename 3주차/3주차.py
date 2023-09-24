#02-5      88p       9/18


dic = {'name':'pey', 'phone':'01199991111', 'birth':'1118'}

a1= {1:'hi'}
print(a1)
a2 = {'a':[1, 2, 3]}
print(a2)
a3 = {1:'a'}
a3[2] = 'b'
print(a3)


#hong
    #과목 국어, 영어, 수학
    #점수 80 75 55
hong_grade = {'korean':80, 'eng;ish':75, 'math':55}
print(hong_grade)
print(hong_grade['korean'])

print(hong_grade.keys())
print(hong_grade['math'])
print("-----------------------------------------------")


chune_grade = {'korean':80, 'english':90, 'math':75}
print(chune_grade)

student_grade = [] #선언 필수 
#student_grade.append()

#student1 = {}
#student2 = {} #this is not

student_grade.append(chune_grade)
student_grade.append(hong_grade)
print(student_grade)

chune_grade["korean"] = 10
print(student_grade)
#append -> save 

print(student_grade[0]["english"])

#펼균값
avg = (student_grade[0]["english"]+student_grade[0]["korean"]+student_grade[0]["math"]) / 3
print(avg)





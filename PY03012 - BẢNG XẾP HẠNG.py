class Student:
    def __init__(self, FullName, SuccessSub, FreSub):
        self.Fullname = FullName
        self.SuccessSub = SuccessSub
        self.FreSub = FreSub

List = []

for _ in range(int(input())):
    name = input()
    successsub, fresub = map(int, input().split())
    List.append(Student(name, successsub, fresub))

List.sort(key = lambda x: (-x.SuccessSub, x.FreSub, x.Fullname))

for student in List:
    print(f"{student.Fullname} {student.SuccessSub} {student.FreSub}")
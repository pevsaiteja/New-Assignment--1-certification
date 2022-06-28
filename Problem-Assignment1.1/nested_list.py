if __name__=='__main__':
    students = []
    scores = []
    n= int(input())
    for N in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name, score])
    count = scores.count(min(scores))
    for i in range(count):
        scores.remove(min(scores))
    secondHigh = min(scores)
    students.sort()
    output = [x for x in students if x[i] == secondHigh]
    for i in output:
        print(i[0])

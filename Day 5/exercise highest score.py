student_scores=input("input a list of students heights:  ").split()
for n in range (0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)

#max( min())
biggest_score=0
for score in student_scores:
    
    if score>biggest_score:
        biggest_score=score
    
print(f"the heighest score is {biggest_score}")
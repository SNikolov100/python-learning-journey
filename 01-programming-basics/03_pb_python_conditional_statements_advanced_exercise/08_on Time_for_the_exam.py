hour_exam = int(input())
minutes_exam = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())

time_on_exam = (hour_exam * 60) + minutes_exam
time_on_arrive = (hour_arrive * 60) + minutes_arrive
difference_time = time_on_arrive - time_on_exam
result = ""
word_for_time = "before"

if difference_time < -30:
    result = "Early"
elif -30 <= difference_time <=0:
    result = "On time"
elif difference_time >0:
    result = "Late"
    word_for_time = "after"

hour_print = abs(difference_time) // 60
minutes_print = abs(difference_time) % 60

print(result)
if hour_print == 0 and minutes_print == 0:
    pass
elif hour_print == 0:
    print(f"{int(minutes_print)} minutes {word_for_time} the start")
elif hour_print > 0:
    print(f"{hour_print}:{int(minutes_print):02} hours {word_for_time} the start")

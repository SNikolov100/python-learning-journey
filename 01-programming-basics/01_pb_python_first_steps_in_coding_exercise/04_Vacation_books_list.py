pages = int(input())            # колко страници е книгата
pages_per_hours = int(input())  # колко страници чете за час
days = int(input())             # колко дена трябва да чете

total_hours_reading = pages // pages_per_hours
result = total_hours_reading // days

print(result)
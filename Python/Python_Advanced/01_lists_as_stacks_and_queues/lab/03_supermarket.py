from collections import deque
queue_customer = deque()

while True:
    command = input()
    if command == 'End':
        break
    if command == 'Paid':
        if len(queue_customer) > 0:
            for _ in range(len(queue_customer)):
                print(queue_customer.popleft())
    else:
        queue_customer.append(command)


print(f"{len(queue_customer)} people remaining.")



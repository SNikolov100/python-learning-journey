n_one, m_two = map(int, input().split())
set_one = set()
set_two = set()

for _ in range(n_one):
    set_one.add(input())
for _ in range(m_two):
    set_two.add(input())

print(*(set_one & set_two),sep="\n")
total = 0
numbers = []

for sec in ['첫', '두', '세']:
    temp = input(f'{sec} 번째 숫자를 입력하시오: ')
    numbers.append(temp)
    total += int(temp)

print(f'{", ".join(numbers)}의 평균은 {total / 3} 입니다.')

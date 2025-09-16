numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

nonnumbers: list[int] = numbers [:4] + numbers[5:]
p=sum(nonnumbers)/(len(nonnumbers)+1)
#print(p, type(p))
prop :list = [p]
#print(prop, type(prop))
numbers = numbers [:4] + prop + numbers[5:]

print(f"Измененный список: {numbers}")

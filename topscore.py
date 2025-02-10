filename = 'topscore.txt'
high_score=10
print(high_score)
with open(filename) as file_object:
	high_score= file_object.read()
print(high_score)

high_score=100
with open(filename, 'w') as file_object:
	file_object.write(str(high_score))

with open(filename) as file_object:
	high_score= file_object.read()
print(high_score)



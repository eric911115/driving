country = input('請問你在哪個國家:')
age = input('請問你現在幾歲:')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照ㄌ')
	else:
		print('你還不能考駕照ㄛ')
else:
	print('只能輸入台灣或美國!')
longText = "Lorem Ipsum is simply dummy text of the printing and pesetting industry. Lorem Ipsum has been the industry&#39;s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

text_list = longText.split()
#print(text_list)

count = 0
for i in text_list:
	count += len(i) # 486개의 공백의 제외한 문자수

#print(len(text_list)) # 91개의 방

space = len(text_list) - 1 # 90개의 공백

print('공백 수 :', space)
print('공백을 제외한 문자수 :', count)
print('공백을 포함한 문자수 :', count+space)
#print('단어 수 :', len(text_list))
print('단어 수 :', space + 1)
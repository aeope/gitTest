longText = "Lorem Ipsum is simply dummy text of the printing and pesetting industry. Lorem Ipsum has been the industry&#39;s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

def splitdata(data):
    splitdata = data.split()
    return splitdata, len(splitdata)

def count_character(data):
    count = 0
    for i in data :
        count += len(i)
    return count
 
data, count = splitdata(longText)
char_count = count_character(data)

print("공백 수 : ", count - 1)
print("공백을 제외한 문자수 : ", char_count)
print("공백을 포함한 문자수 : ", char_count + count - 1)
print("단어 수 : ", count)
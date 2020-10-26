# 구구단 생성 함수(시작값, 끝나는 값)
def gugudan(start, end):
	# 결과물 저장할 리스트 초기화
	result = []
	# 단수를 정해주는 for문(반복문)
	for i in range (start, end):
		# 1~9까지 해당 단에 곱해줄 숫자
		for j in range(1, 10):
			# 결과물을 생성 및 삽입
			result.append(f'{i} x {j} = {i*j}<br />')
		# 단수 구별자 삽입
		result.append('-'*20+'<br />')

	# 결과물 리턴
	return result


# 파일 업로드 함수
def upload(path, result):
	# 파일 열기
	with open (path, 'w') as f:
		# 결과물 for문(반복문)
		for r in result:
			# 결과물 업로드
			f.write(r)

# 사용자에게 입력받을 시작값
#start_input = int(input('시작값 : '))
# 사용자에게 입력받을 끝나는 값
#end_input = int(input('끝나는 값 : ')) + 1
start_input = 15
end_input = 18 + 1

# 구구단 함수 호출 및 결과물 반환받음
result = gugudan(start_input, end_input)

# 업로드 함수 호출
upload('/home/ubuntu/index.html', result)
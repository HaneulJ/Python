"""
다음과 같은 내용으로 구성되는 이차원 리스트를 생성한다.
	10, 12, 14, 16
  	18, 20, 22, 24
   	26, 28, 30, 32
   	34, 36, 38, 40
다음 결과를 출력한다.
	1행 1열의 데이터 : 10
   	3행 4열의 데이터 : 32
	행의 갯수 : 4
	열의 갯수 : 4
	3행의 데이터들 : 26 28 30 32
	2열의 데이터들 : 12 20 28 36
    왼쪽 대각선 데이터들 : 10 20 30 40
    오른쪽 대각선 데이터들 : 16 22 28 34
"""
data = [[10,12,14,16],
        [18,20,22,24],
        [26,28,30,32],
        [34,36,38,40]]

print("1행 1열의 데이터:", data[0][0])
print("3행 4열의 데이터:", data[2][3])
print("행의 갯수:", len(data))
print("열의 갯수:", len(data[0]))
print("3행의 데이터들:", data[2])
print("2열의 데이터들:",data[0][1], data[1][1], data[2][1], data[3][1])
print("왼쪽 대각선 데이터들:", data[0][0], data[1][1], data[2][2], data[3][3] )
print("오른쪽 대각선 데이터들:",data[0][3], data[1][2], data[2][1], data[3][0])

# 왼쪽 대각선: [행]=[열]
# 오른쪽 대각선: [+1][-1]

"""
print("왼쪽 대각선 데이터들:", end="")
for i in range(len(data)):
        print(data[i][i], end=" ")
j = len(data[0])

for i in range(len(data)):
        print(data[i][j-1], end=" ")
        j = j-1
"""
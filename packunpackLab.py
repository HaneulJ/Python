"""
다음 리스트를 생성하고
listv3 = [ 'p', 'y', 't', 'h', 'o', 'n' ]
(1) v1, v2, v3, v4, v5,v6 에 언 패킹해서 저장한 후에 각 변수의 값을 행 단위로 화면에 출력한
다.
(2) listv3 를 언패킹하여 print()  함수에 전달하여 출력한다.
(3) listv3 를 그냥 print()  함수에 전달하여 출력한다
"""
listv3 = [ 'p', 'y', 't', 'h', 'o', 'n' ]

# (1)
v1,v2,v3,v4,v5,v6 = listv3
print(v1,v2,v3,v4,v5,v6,sep="\n")

# (2) *함수: 함수를 각각 아규먼트로 호출하겠다
print(*listv3)

# (3)
print(listv3)

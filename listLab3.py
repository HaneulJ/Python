"""최댓값과 최솟값을 구하는 기능은 함수를 사용하지 않고 제어문으로 직접 구현한다.
1. listLab3.py 이라는 소스를 생성한다.
2. 다음 값들로 구성되는 리스트를 생성하여 listnum 에 저장한다.
   10, 5, 7, 21, 4, 8, 18
3. listnum 에 저장된 값들 중에서 최댓값 최솟값을 추출하여 출력한다.
"""

listnum = [10, 5, 7, 21, 4, 8, 18]

lmax = listnum[0]
lmin = listnum[0]
for i in range(1,len(listnum)):
    if lmax < listnum[i]:
        lmax = listnum[i]
    if lmin > listnum[i]:
        lmin = listnum[i]
print("최솟값: ", lmin, "최댓값: ", lmax)
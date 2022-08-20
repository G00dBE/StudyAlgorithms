# SWEA 2001
# 2차원 배열의 부분합
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 2차원 배열 입력
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):     # 전체 행렬에서 파리채 크기만큼의 부분행렬을 빼줌
            sum_ent = 0
            for k in range(M):    # 파리채 영역을 순회하며 원소를 합함
                for h in range(M):
                    sum_ent += arr[i+k][j+h]
                if max_sum < sum_ent:    # 최댓값을 리스트로 만들지 않고 구함
                    max_sum = sum_ent
    print(f"#{t+1} {max_sum}")

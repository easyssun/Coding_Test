from collections import deque

# 현재 칸이 청소되어 있는가
def clearance_of_current(r, c):
    return visited[r][c]

# 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는가 
def clearance_of_near_current(r, c):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in delta:
        if (r + dx > 0 and r + dx < N) and (c + dy > 0 and c + dy < M):
            if visited[r + dx][c + dy] == False and state[r + dx][c + dy] != 1:
                return True
            
    return False

# 바라보는 방향 기준 앞쪽 칸이 청소가 안된 빈칸인가?
def is_front_not_cleaned(r, c, d):
    if d == 0:
        return not visited[r - 1][c] and not state[r - 1][c]
    elif d == 1:
        return not visited[r][c + 1] and not state[r][c + 1]
    elif d == 2:
       return not visited[r + 1][c] and not state[r + 1][c]
    elif d == 3:
       return not visited[r][c - 1] and not state[r][c - 1]

# 바라보는 방향의 뒷쪽 칸이 벽인가?
def is_back_wall(r, c, d):
    if d == 0:
        if r + 1 <= N:
            return state[r + 1][c]
    elif d == 1:
        if c - 1 >= 0:
            return state[r][c - 1]
    elif d == 2:
        if r - 1 >= 0:
            return state[r - 1][c]
    elif d == 3:
        if c + 1 >= 0:
            return state[r][c + 1]
    

def go_forward(r, c, d):
    if d == 0:
        return r - 1, c
    elif d == 1:
        return r, c + 1
    elif d == 2:
       return r + 1, c
    elif d == 3:
       return r, c - 1

def go_backward(r, c, d):
    if d == 0:
        return r + 1, c
    elif d == 1:
        return r, c - 1
    elif d == 2:
       return r - 1, c
    elif d == 3:
       return r, c + 1

def roatate_ccw(d):
    rotated_d = d - 1
    if rotated_d < 0:
        rotated_d = 3
        
    return rotated_d
    
def clean(r, c):
    visited[r][c] = True

def logic(init_r, init_c, init_d):
    r, c, d = init_r, init_c, init_d
    
    while True:
        
        # 1) 현재칸이 청소되어 있지 않다면, 현재 칸 먼저 청소
        if (clearance_of_current(r, c)) == False:
            
            clean(r, c)

        # 2) 현재 칸 주변 4칸 중 청소를 안한 빈칸이 있다.
        # 2-1) Yes
        if (clearance_of_near_current(r, c)):
            
            # 반시계 방향으로 90도 회전한다
            d = roatate_ccw(d)
            
            # 바라보는 방향 기준 앞쪽 칸이 청소가 안된 빈칸이라면, 한 칸 전진한다.
            
            if (is_front_not_cleaned(r, c, d)):
                r, c = go_forward(r, c, d)
                
        # 2-2) No
        else:
            # 바라보는 방향의 뒤쪽 칸이 벽이다. 
            # Yes)
            
            if (is_back_wall(r, c, d)):
                # 작동을 멈춘다.
                return
            # No) 
            else:
                
                # 바라보는 방향을 유지한 채로 한 칸 후진한다. 
                r, c = go_backward(r, c, d)
    
if __name__ == "__main__":
    
    state = []
    
    # Get input
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    
    for _ in range(N):
        state.append(list(map(int, input().split())))
    
    visited = [[False] * M for _ in range(N)]
    
    logic(r, c, d)
    
    cleaned = 0
    
    for row in visited:
        cleaned += row.count(True)
    print(cleaned)
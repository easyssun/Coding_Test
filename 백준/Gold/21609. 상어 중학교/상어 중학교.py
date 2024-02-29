from collections import deque

RAINBOW = 0
BLACK = -1
EMPTY = -1000

def find_largest_group():
    global graph
    row_len = len(graph)
    col_len = len(graph[0])
    
    groups = []
    visited = [[False] * col_len for _ in range(row_len)]
    
    # 크기가 가장 큰 블록 그룹을 찾는다. 
    for row in range(row_len):
        for col in range(col_len):
            if not visited[row][col] and not graph[row][col] in [EMPTY, BLACK,0]:
                # group_info: [visited, rainbow, base_block]
                group_info = bfs(row, col)
                
                if group_info == False:
                    continue
                
                for visited_row, visited_col in group_info[0] + group_info[1]:
                    visited[visited_row][visited_col] = True
                
                groups.append(group_info)

    # 크기가 2 이상인 그룹이 없다면 return
    if len(groups) == 0:
        return False
    
    # 그러한 블록이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹
    # 그러한 블록도 여러 개라면 기준 블록의 행이 가장 큰 것
    # 그러한 블록도 여러 개라면 기준 블록의 열이 가장 큰 것
    groups.sort(key = lambda x : (-(len(x[0]) + len(x[1])), -len(x[1]), -x[2][0], -x[2][1]))
    
    largest_group = groups[0][0] + groups[0][1]
    
    return largest_group

def gravity():
    global graph
    row_len = len(graph)
    col_len = len(graph[0])
    
    for col in range(col_len):
        for row in range(row_len-1, -1, -1):
            cur_row = row
            while cur_row > 0 and graph[cur_row][col] == EMPTY:
                cur_row -= 1
            if cur_row != row and graph[cur_row][col] != BLACK:
                tmp = graph[cur_row][col]
                graph[row][col] = tmp
                graph[cur_row][col] = EMPTY
        
def rotate():
    global graph
    row_len = len(graph)
    col_len = len(graph[0])
    
    rotated_graph = [[0] * col_len for _ in range(row_len)]
    
    for row in range(row_len):
        for col in range(col_len):
            rotated_graph[col_len - 1 - col][row] = graph[row][col]
    
    graph = rotated_graph[:]
    
def bfs(r, c):
    global graph
    row_len = len(graph)
    col_len = len(graph[0])
    
    q = deque()
    visited = [[False] * col_len for _ in range(row_len)]
    visited_blocks = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rainbow = []
    
    q.append((r, c))
    visited[r][c] = True
    color = graph[r][c]

    if color != 0:
        visited_blocks.append((r, c))
    
    while q:
        cur_r, cur_c = q.popleft()
        
        for d_r, d_c in directions:
            next_r = cur_r + d_r
            next_c = cur_c + d_c
            
            if (next_r >= 0 and next_r < row_len) and (next_c >= 0 and next_c < col_len):
                if not visited[next_r][next_c]:
                    if graph[next_r][next_c] == color:
                        q.append((next_r, next_c))
                        visited[next_r][next_c] = True
                        visited_blocks.append((next_r, next_c))
                        
                    elif graph[next_r][next_c] == 0:
                        q.append((next_r, next_c))
                        visited[next_r][next_c] = True
                        rainbow.append((next_r, next_c))            
    
    for r, c in rainbow:
        visited[r][c] = False
    
    if len(visited_blocks) < 1 or len(visited_blocks) + len(rainbow) < 2:
        return False
    
    base_block = find_base_block(visited_blocks)
    
    return visited_blocks, rainbow, base_block
                  
def find_base_block(blocks):
    smallest_block = blocks[0]
    
    for row, col in blocks[1:]:
        
        # 행의 번호가 가장 작은 블록
        if row < smallest_block[0]:
            smallest_block = (row, col)
            
        # 그러한 블록이 여러개면 열의 번호가 가장 작은 블록
        elif row == smallest_block[0]:
            if col < smallest_block[1]:
              smallest_block = (row, col)  
    return smallest_block
    
def delete_group(group):
    global graph
    for x, y in group:
        graph[x][y] = EMPTY
    
    
if __name__ == "__main__":
    
    graph = []
    
    # input
    N, M = map(int, input().split())
    
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    score = 0
    
    while True:
        # find_largest_group
        largest_group = find_largest_group()
        if largest_group == False:
            break
        # score
        score += pow(len(largest_group), 2)
        
        # delete
        delete_group(largest_group)
        
        # gravity
        gravity()
        
        # rotate
        rotate()
        
        # gravity
        gravity()
    
    print(score)
from collections import deque
LEFT = 6
RIGHT = 2

first_dq = deque()
second_dq = deque()
third_dq = deque()
fourth_dq = deque()

dq_list = [None, first_dq, second_dq, third_dq, fourth_dq]

# 이거 대신 deque의 rotate 함수 쓰면 됨.
def rotate_clockwise(num_of_dq_to_rotate, rotate_direction):
    dq_list[num_of_dq_to_rotate].rotate(rotate_direction)
    # dq_to_rotate = dq_list[num_of_dq_to_rotate]
    # if rotate_direction:
    #   tmp = dq_to_rotate.pop()
    #   dq_to_rotate.appendleft(tmp)
    # else:
    #   tmp = dq_to_rotate.popleft()
    #   dq_to_rotate.append(tmp)
    
def check_near(num_of_dq_to_rotate):
    list_to_rotate = []
    
    num_of_left_dq = num_of_dq_to_rotate - 1
    num_of_right_dq = num_of_dq_to_rotate + 1
    
    dq_to_rotate = dq_list[num_of_dq_to_rotate]
    
    if num_of_left_dq > 0:
      left_dq = dq_list[num_of_left_dq]
      if left_dq[RIGHT] != dq_to_rotate[LEFT]:
        list_to_rotate.append(num_of_left_dq)
            
    if num_of_right_dq < 5:
      right_dq = dq_list[num_of_right_dq]
      if right_dq[LEFT] != dq_to_rotate[RIGHT]:
        list_to_rotate.append(num_of_right_dq)
            
    return list_to_rotate
def reverse_rotate_direction(direction):
  if direction == 1:
    return -1
  else:
    return 1

first = input()
second = input()
third = input()
fourth = input()

k = int(input())
rotate_list = []

for _ in range(0, k):
    rotate_list.append(tuple(map(int, input().split())))

for x in first:
  first_dq.append(x) 
for x in second:
  second_dq.append(x)
for x in third:
  third_dq.append(x) 
for x in fourth:
  fourth_dq.append(x) 

# # # -------------------------------
# first = "10001011"
# second = "10000011"
# third = "01011011"
# fourth = "00111101"

# for x in first:
#   first_dq.append(x) 
# for x in second:
#   second_dq.append(x)
# for x in third:
#   third_dq.append(x) 
# for x in fourth:
#   fourth_dq.append(x) 
# k = 5
# rotate_list = []
# rotate_list.append((1, 1))
# rotate_list.append((2, 1))
# rotate_list.append((3, 1))
# rotate_list.append((4, 1))
# rotate_list.append((1, -1))
# # # -------------------------------

for rotate in rotate_list:
    # print(f"동작: {rotate}")
    num_of_dq_to_rotate = rotate[0]
    rotate_direction = rotate[1]
    
    next_dqs_to_rotate = deque(check_near(num_of_dq_to_rotate))
    rotate_clockwise(num_of_dq_to_rotate, rotate_direction)
    rotated = [num_of_dq_to_rotate]
    # print(f"{num_of_dq_to_rotate}번째 톱니바퀴를 {rotate_direction}방향으로 회전")
    
    while len(next_dqs_to_rotate) != 0:
      
      next_dq_to_rotate = next_dqs_to_rotate.popleft()
      
      
      if next_dq_to_rotate in rotated:
        # print(f"{next_dq_to_rotate}번째 톱니바퀴는 continued")
        continue

      for tmp in check_near(next_dq_to_rotate):
        
        next_dqs_to_rotate.append(tmp)

      if abs(num_of_dq_to_rotate - next_dq_to_rotate) % 2 == 1:
        # print(f"{next_dq_to_rotate}번째 톱니바퀴를 {rotate_direction} 반대 방향으로 회전 ")
        
        rotate_clockwise(next_dq_to_rotate, reverse_rotate_direction(rotate_direction))
      else:
        # print(f"{next_dq_to_rotate}번째 톱니바퀴를 {rotate_direction}방향으로 회전 ")
        rotate_clockwise(next_dq_to_rotate, rotate_direction)
      
      

      rotated.append(next_dq_to_rotate)

score = 0    
if first_dq[0] == "1":
  score += 1
if second_dq[0] == "1":
  score += 2
if third_dq[0] == "1":
  score += 4
if fourth_dq[0] == "1":
  score += 8
print(score)
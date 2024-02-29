def solution(nums):
    set_nums = set(nums)
    
    if len(set_nums) < len(nums) / 2:
        answer = len(set_nums)
    else:        
        answer = len(nums) / 2
    return answer
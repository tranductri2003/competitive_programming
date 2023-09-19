def is_possible(mid, N, A, D):
    prev_passengers = 0
    
    for i in range(N):
        # Calculate the maximum passengers that can move to the current carriage
        max_move = min(mid - prev_passengers, D[i])
        
        # Check if it's possible to distribute passengers to the next carriage
        if max_move < 0:
            return False
        
        # Update the number of passengers in the current carriage
        prev_passengers = min(A[i], prev_passengers + max_move)
        
        # If there are still passengers left, it's not possible
        if prev_passengers < A[i]:
            return False
    
    return True

def find_min_Z(N, A, D):
    left, right = 0, sum(A)  # Initialize the search range
    
    while left < right:
        mid = (left + right) // 2
        
        if is_possible(mid, N, A, D):
            right = mid  # Reduce the upper bound
        else:
            left = mid + 1  # Increase the lower bound
    
    return left

# Read input
N = int(input())
A = list(map(int, input().split()))
D = list(map(int, input().split()))

# Find and print the minimum possible value of Z
result = find_min_Z(N, A, D)
print(result)

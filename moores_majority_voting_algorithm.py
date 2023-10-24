"""
### Boyer-Moore Majority Voting Algorithm to find Majority Element in an array

- To find out the majority element in a given array
- Constraint: Array is non-empty and the majority element always exists in the array
- details
    - **Majority element**
        - an element in an array that occurs more than n/2 times, where n is the length of the array
        - Occurrence count of majority element should be strictly greater than n/2
        - because of this constraint, only one majority element is possible in a given array
    - examples:
    [2, 1, 2] ⇒ 2
    [1,1,1] ⇒ 1
    [1,1,2] ⇒ 1
    
    **Constraints**
    
    - Array is non-empty and the majority element always exists in the array
    
    **Explanation**
    
    - Moore’s voting algorithm finds majority elements in tc O(n) and sc O(1)
    - the intuition ⇒
        - majority element will always have the largest number of occurence.
        - we intiailise  two variables candidate and count.
        - Iterate through the array
            - initialize first element as candidate
            - if A[i] == candidate, we increment count by 1
            - else decrement count by 1
            - at any point, count equals 0, A[i] will be the candidate.
    - This works on the assumption that there exists a majority element in A
"""

def solve(A):
    """ Boyer-Moore Majority Voting Algorithm """
    candidate=None # majority candidate
    count=0
    for i in range(len(A)):
        if count == 0:
            candidate = A[i]
        if A[i]!=candidate:
            count-=1
        elif A[i]==candidate:
            count+=1
    return candidate


print(solve([2, 1, 2])==2)
print(solve([1,1,1])==1)
print(solve([1,1,2])==1)
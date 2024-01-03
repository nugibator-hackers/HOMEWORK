def joseph(n, arr1, k, arr2) -> int:
    """Рассчитать количество платформ."""
    left = 0
    
    for i in range(k):
        for j in range(left, n):
            if arr2[i] == arr1[j]:
                arr1[left], arr1[j] = arr1[j], arr1[left]
                left += 1  
    for i in range(left, len(arr1)):
        for j in range(i, left, -1):
            if arr1[j] < arr1[j-1]:
                arr1[j], arr1[j-1] = arr1[j-1], arr1[j]
            else:
                break
    return arr1
 
def main() -> None:
    n = int(input())
    arr1: list = [int(array_counter) for array_counter in input().split(' ')]
    k = int(input())
    if k == 0:
        print(*joseph(n, arr1, k, []))
    else:
        arr2: list = [int(array_counter) for array_counter in input().split(' ')]
        print(*joseph(n, arr1, k, arr2))
 
if __name__ == '__main__': 
    main()

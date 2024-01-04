def cago(n, arr1, m, arr2):
    count = 0
    arr2 = sorted(arr2, reverse=True)
    min_number = min(arr1)
    if n > m:
        for i in range(m):
            if arr2[i] >= min_number:
                count += 1
    elif n < m: 
        for i in range(n):
            if arr2[i] >= min_number:
                count += 1           
    
    
    return count



def main():
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    m = int(input())
    arr2 = [int(x) for x in input().split()]
    print(cago(n, arr1, m, arr2))


if __name__ == '__main__':
    main()

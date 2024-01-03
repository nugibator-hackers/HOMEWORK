def joseph(n, arr) -> int:
    """Рассчитать количество платформ."""
    k = 0
    sum = 0
    count = 0
    for i in arr:
        sum += i
        k += 1
        if sum == (k * k - k) / 2:
                count += 1      
    return count
 
def main() -> None:
    n = int(input())
    arr: list = [int(array_counter) for array_counter in input().split(' ')]
    print(joseph(n, arr))
 
if __name__ == '__main__': 
    main()

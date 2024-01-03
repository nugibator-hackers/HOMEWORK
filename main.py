# 104042731
def mars_roverars(s) -> int: 
    """Рассчитать количество платформ.""" 
    if not s:
        return 0
    max_str = 0
    l = 0 
    uniq = set()
    for r in range(len(s)):
        while s[r] in uniq:
            uniq.remove(s[l])
            l += 1
        uniq.add(s[r])
        max_str = max(max_str, r-l+1)
    return max_str        
 
def main() -> None: 
    s = str(input())  
    print(mars_roverars(s)) 
 
if __name__ == '__main__': 
    main()

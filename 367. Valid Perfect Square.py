def isPerfectSquare(self, num: int) -> bool:
    for i in range(int(num**0.5)):
        if(i**2==num):return True
    
    return False

print(isPerfectSquare(self=1,num=9))
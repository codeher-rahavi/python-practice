class Solution:
    def lemonadeChange(bills) -> bool:
        five,ten=0,0
        for i in bills:
            if i==5:
                five+=1
            elif i==10:
                if five>=1:
                    five-=1
                    ten+=1
                else:
                    return False
            elif i==20:
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False

        return True
print(Solution.lemonadeChange([5,5,5,10,20]))
#description
#by Baltazar1697
height = int(input())#max disks
fromPole = str(input())# number
toPole = str(input())
withPole = str(input())
counter = 0
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
    
moveTower(height,fromPole, toPole, withPole)
# к-во ходов 2^n-1
print(counter)
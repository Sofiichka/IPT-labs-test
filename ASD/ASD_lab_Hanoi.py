#description
#by Baltazar1697
counter = 0
def moveTower(height,fromPole, toPole, withPole):
    global counter
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        print("moving disk from",fromPole,"to",toPole)
        counter+=1
        moveTower(height-1,withPole,toPole,fromPole)
    return counter
#Average: O(log(N)) time | O(log(N)) space
#Worst:   O(N) time | O(N) space

def findClosetValueInBst(tree, target):
    return findClosestValueInBstHeight(tree, target, float("inf"))

def findClosestValueInBstHeight(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs (target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHeight(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHeight(tree.right, target, closest)
    else:
        return closest

#Average: O(log(N)) time | O(1) space
#Worst:   O(N) time | O(1) space

def findClosetValueInBst(tree, target):
    return findClosestValueInBstHeight(tree, target, float("inf"))

def findClosestValueInBstHeight(tree, target, closest):
    currentNode = tree
    while currentNode is not Node:
        if abs(target - closest) > abs (target - tree.value):
            closest = tree.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


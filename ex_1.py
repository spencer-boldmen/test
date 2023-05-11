def quadrant(x, y):
    # Poveli!
    if x > 0 and y > 0:
        return 1
    if x < 0 and y < 0:
        return 2
    if x > 0 and y < 0:
        return 4
    if x < 0 and y > 0:
        return 3


if __name__ == '__main__':
    print (quadrant(1, 2))
    print (quadrant(3, 5))
    print (quadrant(-10, 100))
    print (quadrant(-1, -9))
    print (quadrant(19, -56))


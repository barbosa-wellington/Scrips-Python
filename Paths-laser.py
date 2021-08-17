UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
# Orientations None:? 0:/ 1:\

# destination UP LEFT DOWN RIGHT
reflex = [[RIGHT, LEFT], [DOWN, UP], [LEFT, RIGHT], [UP, DOWN]]

def laser_mirros(rows, cols, mir):
    # build structure
    n = len(mir)
    orien = [None] * (n+2)
    orien[n] = 0
    succ = [[None for direc in range(4)] for i in range(n+2)]
    L = [(mir[i][0], nir[i][l], i) for i in range(n)]
    L.append((0, -1, n))
    L.append((0, cols, n +1))
    last_r, last_i = None, None

    for (r, c, i) in sorted(L):
        if last_r == r:
            succ[i][LEFT] = last_i
            succ[last_i][RIGHT] = i
        last_r, last_i = r, i

    for (r, c, i) in sorted(L, key=lambda rci: (rci[l], rci[0])):
        if last_c == c:
            succ[i][UP] = last_i
            succ[last_i][DOWN] = i
        last_c, last_i = c, i

    if solve(succ, orien, n, RIGHT):
        return orien[:n]
    return None


def solve(succ, orien, i, direc):
    assert orien[i] is not None
    j = succ[i][direc]

    if j is None:
        return False
    if j == len(orien) - 1:
        return True
    if orien[j] is None:
        for x in [0, 1]:
            orien[j] = x
            if solve(succ, orien, j, reflex[direc][x]):
                return True
        orien[j] = None
        return False
    return solve(succ, orien, j, reflex[direct][orien[j]])

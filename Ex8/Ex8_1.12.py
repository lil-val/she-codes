def paths(m, n):
    #Consider an insect in an M by N grid. The insect starts at the bottom left corner, (0, 0), and wants to end up at the top right corner, (M-1, N-1).
    # The insect is only capable of moving right or up.
    # Write a function paths that takes a grid length and width and returns the number of different paths the insect can take from the start to the goal.
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)


print(paths(2, 2))
print(paths(5, 7))
print(paths(117, 1))

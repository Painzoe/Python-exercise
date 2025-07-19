diameter = int(input("Please enter an even integer number for diameter of the diamond: "))

if diameter % 2 != 0:
    print("Please enter an even integer number!")
else:

    def left_space_top(row, diameter):
        for i in range(diameter // 2 - row):
            print(" ", end="")

    def middle_space_top(row):
        for i in range(row * 2):
            print(" ", end="")

    def top_part(diameter):
        for i in range(diameter // 2 + 1):
            left_space_top(i, diameter)
            print("/", end="")
            middle_space_top(i)
            print("\\")

    def left_space_bottom(row, diameter):
        for i in range(diameter // 2 - row - 1, -1, -1):
            print(" ", end="")

    def middle_space_bottom(row):
        for i in range(row * 2):
            print(" ", end="")

    def bottom_part(diameter):
        for i in range(diameter // 2, -1, -1):
            left_space_bottom(i, diameter)
            print("\\", end="")
            middle_space_bottom(i)
            print("/")

    def diamond(diameter):
        top_part(diameter)
        bottom_part(diameter)

    diamond(diameter)







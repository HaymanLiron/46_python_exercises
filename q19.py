def bottle_or_bottles(x):
    return "bottle" + ("s" if x != 1 else "")


def write_x_bottles_song(x):
    # generates the 99 bottles of beer song
    # accounting for plural issues when it's only 1 bottle
    if x == 0:
        return
    else:
        print(str(x) + " " + bottle_or_bottles(x) + " of beer on the wall, "
              + str(x) + " " + bottle_or_bottles(x) + " of beer.")
        print("Take one down, pass it around, " + str(x - 1) + " " +
              bottle_or_bottles(x) + " of beer on the wall.")
        write_x_bottles_song(x - 1)


write_x_bottles_song(99)
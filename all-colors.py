def iterate_colors():
    for r in range(256):
        for g in range(256):
            for b in range(256):
                yield (r, g, b)

for color in iterate_colors():
    print("#{:02X}{:02X}{:02X}".format(color[0], color[1], color[2]))
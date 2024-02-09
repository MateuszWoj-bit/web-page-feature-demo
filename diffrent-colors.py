from math import sqrt

def hex_to_rgb(hex_color):
    """Convert hexadecimal color code to RGB values."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def color_distance(color1, color2):
    """Calculate Euclidean distance between two colors in RGB space."""
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

colors = [
    "#F08080", "#F0FFFF", "#98FB98", "#FFD700", "#800080", "#FFFF00", "#7FFFD4", "#808080",
    "#FFE4B5", "#B8860B", "#FFFFE0", "#F0F8FF", "#F5DEB3", "#FFA07A", "#00FFFF", "#66CDAA",
    "#00CED1", "#EE82EE", "#FFA500", "#FFFAFA", "#D8BFD8", "#A9A9A9", "#FF0000", "#708090",
    "#800000", "#FAEBD7", "#FF00FF", "#FFFACD", "#7CFC00", "#FFFAF0", "#4B0082", "#008B8B",
    "#B0C4DE", "#D2B48C", "#696969", "#DCDCDC", "#EEE8AA", "#9400D3", "#00008B", "#F0E68C",
    "#A52A2A", "#5F9EA0", "#8B0000", "#FFFFF0", "#191970", "#FFC0CB", "#40E0D0", "#808000",
    "#FA8072", "#556B2F", "#F5F5DC", "#7B68EE", "#B0E0E6", "#DDA0DD", "#000000", "#C71585",
    "#00FA9A", "#BA55D3", "#6A5ACD", "#6495ED", "#F5F5F5", "#FAFAD2", "#FFDAB9", "#FFE4E1",
    "#8FBC8F", "#FFDEAD", "#FF7F50", "#9370DB", "#7FFF00", "#FFEBCD", "#00FFFF", "#9932CC",
    "#E0FFFF", "#8B4513", "#FF6347", "#CD853F", "#F4A460", "#C0C0C0", "#20B2AA", "#0000CD",
    "#BC8F8F", "#FFEFD5", "#FFB6C1", "#8B008B", "#006400", "#3CB371", "#DEB887", "#90EE90",
    "#FFFFFF", "#6B8E23", "#2F4F4F", "#A0522D", "#FF1493", "#008080", "#FAF0E6", "#DB7093",
    "#F0FFF0", "#FF4500", "#9ACD32", "#8A2BE2", "#4169E1", "#00BFFF", "#FFF8DC", "#E9967A",
    "#87CEFA", "#FF00FF", "#AFEEEE", "#32CD32", "#DC143C", "#F8F8FF", "#2E8B57", "#1E90FF",
    "#008000", "#D2691E", "#000080", "#FFE4C4", "#00FF7F", "#E6E6FA", "#4682B4", "#CD5C5C",
    "#FFF0F5", "#DA70D6", "#DAA520", "#ADFF2F", "#D3D3D3", "#FDF5E6", "#BDB76B", "#00FF00",
    "#FF69B4", "#228B22", "#B22222", "#ADD8E6", "#483D8B", "#FFF5EE", "#F5FFFA", "#778899",
    "#FF8C00", "#48D1CC", "#87CEEB", "#663399", "#0000FF"
]

rgb_colors = [hex_to_rgb(color) for color in colors]

threshold = 33

noticeably_different_colors = []

for i, color1 in enumerate(rgb_colors):
    noticeably_different = True
    for j, color2 in enumerate(rgb_colors):
        if i != j and color_distance(color1, color2) <= threshold:
            noticeably_different = False
            break
    if noticeably_different:
        noticeably_different_colors.append(colors[i])

print("Noticeably different colors:", noticeably_different_colors)
print("Number of noticeably different colors:", len(noticeably_different_colors))

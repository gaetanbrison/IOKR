#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on November 2021
@authors:
Gaëtan Brison <gaetan.brison@ip-paris.fr>
"""

import numpy as np

# standard SVG colors
STANDARD_COLORS = np.array(
    [
        "blue",
        "red",
        "green",
        "orange",
        "purple",
        "yellow",
        "fuchsia",
        "olive",
        "aqua",
        "brown",
    ]
)

# 100 RGB colors of coolwarm color map.
COOLWARM_RGB = np.array(
    [
        [58, 76, 192],
        [60, 79, 195],
        [64, 84, 199],
        [66, 88, 202],
        [70, 93, 207],
        [72, 96, 209],
        [76, 102, 214],
        [80, 107, 218],
        [82, 110, 220],
        [86, 115, 224],
        [88, 118, 226],
        [92, 123, 229],
        [96, 128, 232],
        [99, 131, 234],
        [103, 136, 237],
        [105, 139, 239],
        [109, 144, 241],
        [112, 147, 243],
        [116, 151, 245],
        [120, 155, 247],
        [123, 158, 248],
        [127, 162, 250],
        [130, 165, 251],
        [134, 169, 252],
        [138, 173, 253],
        [141, 175, 253],
        [145, 179, 254],
        [148, 181, 254],
        [152, 185, 254],
        [155, 187, 254],
        [159, 190, 254],
        [163, 193, 254],
        [166, 195, 253],
        [170, 198, 253],
        [172, 200, 252],
        [176, 203, 251],
        [180, 205, 250],
        [183, 207, 249],
        [187, 209, 247],
        [189, 210, 246],
        [193, 212, 244],
        [197, 213, 242],
        [199, 214, 240],
        [202, 216, 238],
        [205, 217, 236],
        [208, 218, 233],
        [210, 218, 231],
        [214, 219, 228],
        [217, 220, 224],
        [219, 220, 222],
        [222, 219, 218],
        [224, 218, 215],
        [227, 217, 211],
        [230, 215, 207],
        [231, 214, 204],
        [234, 211, 199],
        [236, 210, 196],
        [237, 207, 192],
        [239, 206, 188],
        [241, 203, 184],
        [242, 200, 179],
        [243, 198, 176],
        [244, 195, 171],
        [245, 193, 168],
        [246, 189, 164],
        [246, 186, 159],
        [246, 183, 156],
        [247, 179, 151],
        [247, 177, 148],
        [247, 173, 143],
        [246, 169, 138],
        [246, 166, 135],
        [245, 161, 130],
        [245, 158, 127],
        [244, 154, 123],
        [243, 150, 120],
        [242, 145, 115],
        [240, 141, 111],
        [239, 137, 108],
        [237, 132, 103],
        [236, 128, 100],
        [234, 123, 96],
        [231, 117, 92],
        [230, 114, 89],
        [227, 108, 84],
        [225, 104, 82],
        [222, 98, 78],
        [220, 94, 75],
        [217, 88, 71],
        [214, 82, 67],
        [211, 77, 64],
        [207, 70, 61],
        [205, 66, 58],
        [201, 59, 55],
        [197, 50, 51],
        [194, 45, 49],
        [190, 35, 45],
        [187, 26, 43],
        [182, 13, 40],
        [179, 3, 38],
    ]
)

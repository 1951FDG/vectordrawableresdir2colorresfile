# by 1951FDG, James Bennett, Orsiris de Jong, Wilson Mar, Ayush Pareek, Paarth Neekhara

import colorsys
import csv
import os
import re
import sys
from collections import Counter
from fnmatch import fnmatch
from typing import NamedTuple, Tuple, Union

import numpy as np

from scipy import spatial

HEX_COLOR_RE = re.compile(r"^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$")
HEX_XML_COLOR_RE = re.compile(r"\"(#[a-fA-F0-9]{3}|#[a-fA-F0-9]{6})\"")

IntegerRGB = NamedTuple("IntegerRGB", [("red", int), ("green", int), ("blue", int)])
IntTuple = Union[IntegerRGB, Tuple[int, int, int]]

# Paste in contents of rgbcsv2colorarray.py.txt below:
RGB = np.array(
    [
        [255, 235, 238],
        [255, 205, 210],
        [239, 154, 154],
        [229, 115, 115],
        [239, 83, 80],
        [244, 67, 54],
        [229, 57, 53],
        [211, 47, 47],
        [198, 40, 40],
        [183, 28, 28],
        [255, 138, 128],
        [255, 82, 82],
        [255, 23, 68],
        [213, 0, 0],
        [252, 228, 236],
        [248, 187, 208],
        [244, 143, 177],
        [240, 98, 146],
        [236, 64, 122],
        [233, 30, 99],
        [216, 27, 96],
        [194, 24, 91],
        [173, 20, 87],
        [136, 14, 79],
        [255, 128, 171],
        [255, 64, 129],
        [245, 0, 87],
        [197, 17, 98],
        [243, 229, 245],
        [225, 190, 231],
        [206, 147, 216],
        [186, 104, 200],
        [171, 71, 188],
        [156, 39, 176],
        [142, 36, 170],
        [123, 31, 162],
        [106, 27, 154],
        [74, 20, 140],
        [234, 128, 252],
        [224, 64, 251],
        [213, 0, 249],
        [170, 0, 255],
        [237, 231, 246],
        [209, 196, 233],
        [179, 157, 219],
        [149, 117, 205],
        [126, 87, 194],
        [103, 58, 183],
        [94, 53, 177],
        [81, 45, 168],
        [69, 39, 160],
        [49, 27, 146],
        [179, 136, 255],
        [124, 77, 255],
        [101, 31, 255],
        [98, 0, 234],
        [232, 234, 246],
        [197, 202, 233],
        [159, 168, 218],
        [121, 134, 203],
        [92, 107, 192],
        [63, 81, 181],
        [57, 73, 171],
        [48, 63, 159],
        [40, 53, 147],
        [26, 35, 126],
        [140, 158, 255],
        [83, 109, 254],
        [61, 90, 254],
        [48, 79, 254],
        [227, 242, 253],
        [187, 222, 251],
        [144, 202, 249],
        [100, 181, 246],
        [66, 165, 245],
        [33, 150, 243],
        [30, 136, 229],
        [25, 118, 210],
        [21, 101, 192],
        [13, 71, 161],
        [130, 177, 255],
        [68, 138, 255],
        [41, 121, 255],
        [41, 98, 255],
        [225, 245, 254],
        [179, 229, 252],
        [129, 212, 250],
        [79, 195, 247],
        [41, 182, 246],
        [3, 169, 244],
        [3, 155, 229],
        [2, 136, 209],
        [2, 119, 189],
        [1, 87, 155],
        [128, 216, 255],
        [64, 196, 255],
        [0, 176, 255],
        [0, 145, 234],
        [224, 247, 250],
        [178, 235, 242],
        [128, 222, 234],
        [77, 208, 225],
        [38, 198, 218],
        [0, 188, 212],
        [0, 172, 193],
        [0, 151, 167],
        [0, 131, 143],
        [0, 96, 100],
        [132, 255, 255],
        [24, 255, 255],
        [0, 229, 255],
        [0, 184, 212],
        [224, 242, 241],
        [178, 223, 219],
        [128, 203, 196],
        [77, 182, 172],
        [38, 166, 154],
        [0, 150, 136],
        [0, 137, 123],
        [0, 121, 107],
        [0, 105, 92],
        [0, 77, 64],
        [167, 255, 235],
        [100, 255, 218],
        [29, 233, 182],
        [0, 191, 165],
        [232, 245, 233],
        [200, 230, 201],
        [165, 214, 167],
        [129, 199, 132],
        [102, 187, 106],
        [76, 175, 80],
        [67, 160, 71],
        [56, 142, 60],
        [46, 125, 50],
        [27, 94, 32],
        [185, 246, 202],
        [105, 240, 174],
        [0, 230, 118],
        [0, 200, 83],
        [241, 248, 233],
        [220, 237, 200],
        [197, 225, 165],
        [174, 213, 129],
        [156, 204, 101],
        [139, 195, 74],
        [124, 179, 66],
        [104, 159, 56],
        [85, 139, 47],
        [51, 105, 30],
        [204, 255, 144],
        [178, 255, 89],
        [118, 255, 3],
        [100, 221, 23],
        [249, 251, 231],
        [240, 244, 195],
        [230, 238, 156],
        [220, 231, 117],
        [212, 225, 87],
        [205, 220, 57],
        [192, 202, 51],
        [175, 180, 43],
        [158, 157, 36],
        [130, 119, 23],
        [244, 255, 129],
        [238, 255, 65],
        [198, 255, 0],
        [174, 234, 0],
        [255, 253, 231],
        [255, 249, 196],
        [255, 245, 157],
        [255, 241, 118],
        [255, 238, 88],
        [255, 235, 59],
        [253, 216, 53],
        [251, 192, 45],
        [249, 168, 37],
        [245, 127, 23],
        [255, 255, 141],
        [255, 255, 0],
        [255, 234, 0],
        [255, 214, 0],
        [255, 248, 225],
        [255, 236, 179],
        [255, 224, 130],
        [255, 213, 79],
        [255, 202, 40],
        [255, 193, 7],
        [255, 179, 0],
        [255, 160, 0],
        [255, 143, 0],
        [255, 111, 0],
        [255, 229, 127],
        [255, 215, 64],
        [255, 196, 0],
        [255, 171, 0],
        [255, 243, 224],
        [255, 224, 178],
        [255, 204, 128],
        [255, 183, 77],
        [255, 167, 38],
        [255, 152, 0],
        [251, 140, 0],
        [245, 124, 0],
        [239, 108, 0],
        [230, 81, 0],
        [255, 209, 128],
        [255, 171, 64],
        [255, 145, 0],
        [255, 109, 0],
        [251, 233, 231],
        [255, 204, 188],
        [255, 171, 145],
        [255, 138, 101],
        [255, 112, 67],
        [255, 87, 34],
        [244, 81, 30],
        [230, 74, 25],
        [216, 67, 21],
        [191, 54, 12],
        [255, 158, 128],
        [255, 110, 64],
        [255, 61, 0],
        [221, 44, 0],
        [239, 235, 233],
        [215, 204, 200],
        [188, 170, 164],
        [161, 136, 127],
        [141, 110, 99],
        [121, 85, 72],
        [109, 76, 65],
        [93, 64, 55],
        [78, 52, 46],
        [62, 39, 35],
        [250, 250, 250],
        [245, 245, 245],
        [238, 238, 238],
        [224, 224, 224],
        [189, 189, 189],
        [158, 158, 158],
        [117, 117, 117],
        [97, 97, 97],
        [66, 66, 66],
        [33, 33, 33],
        [236, 239, 241],
        [207, 216, 220],
        [176, 190, 197],
        [144, 164, 174],
        [120, 144, 156],
        [96, 125, 139],
        [84, 110, 122],
        [69, 90, 100],
        [55, 71, 79],
        [38, 50, 56],
        [0, 0, 0],
        [255, 255, 255],
    ]
)

# Paste in contents of rgbcsv2colordict.py.txt below:
MATERIALDESIGN_HEX_TO_NAMES = {
    "#ffebee": "Red 50",
    "#ffcdd2": "Red 100",
    "#ef9a9a": "Red 200",
    "#e57373": "Red 300",
    "#ef5350": "Red 400",
    "#f44336": "Red 500",
    "#e53935": "Red 600",
    "#d32f2f": "Red 700",
    "#c62828": "Red 800",
    "#b71c1c": "Red 900",
    "#ff8a80": "Red A100",
    "#ff5252": "Red A200",
    "#ff1744": "Red A400",
    "#d50000": "Red A700",
    "#fce4ec": "Pink 50",
    "#f8bbd0": "Pink 100",
    "#f48fb1": "Pink 200",
    "#f06292": "Pink 300",
    "#ec407a": "Pink 400",
    "#e91e63": "Pink 500",
    "#d81b60": "Pink 600",
    "#c2185b": "Pink 700",
    "#ad1457": "Pink 800",
    "#880e4f": "Pink 900",
    "#ff80ab": "Pink A100",
    "#ff4081": "Pink A200",
    "#f50057": "Pink A400",
    "#c51162": "Pink A700",
    "#f3e5f5": "Purple 50",
    "#e1bee7": "Purple 100",
    "#ce93d8": "Purple 200",
    "#ba68c8": "Purple 300",
    "#ab47bc": "Purple 400",
    "#9c27b0": "Purple 500",
    "#8e24aa": "Purple 600",
    "#7b1fa2": "Purple 700",
    "#6a1b9a": "Purple 800",
    "#4a148c": "Purple 900",
    "#ea80fc": "Purple A100",
    "#e040fb": "Purple A200",
    "#d500f9": "Purple A400",
    "#aa00ff": "Purple A700",
    "#ede7f6": "Deep Purple 50",
    "#d1c4e9": "Deep Purple 100",
    "#b39ddb": "Deep Purple 200",
    "#9575cd": "Deep Purple 300",
    "#7e57c2": "Deep Purple 400",
    "#673ab7": "Deep Purple 500",
    "#5e35b1": "Deep Purple 600",
    "#512da8": "Deep Purple 700",
    "#4527a0": "Deep Purple 800",
    "#311b92": "Deep Purple 900",
    "#b388ff": "Deep Purple A100",
    "#7c4dff": "Deep Purple A200",
    "#651fff": "Deep Purple A400",
    "#6200ea": "Deep Purple A700",
    "#e8eaf6": "Indigo 50",
    "#c5cae9": "Indigo 100",
    "#9fa8da": "Indigo 200",
    "#7986cb": "Indigo 300",
    "#5c6bc0": "Indigo 400",
    "#3f51b5": "Indigo 500",
    "#3949ab": "Indigo 600",
    "#303f9f": "Indigo 700",
    "#283593": "Indigo 800",
    "#1a237e": "Indigo 900",
    "#8c9eff": "Indigo A100",
    "#536dfe": "Indigo A200",
    "#3d5afe": "Indigo A400",
    "#304ffe": "Indigo A700",
    "#e3f2fd": "Blue 50",
    "#bbdefb": "Blue 100",
    "#90caf9": "Blue 200",
    "#64b5f6": "Blue 300",
    "#42a5f5": "Blue 400",
    "#2196f3": "Blue 500",
    "#1e88e5": "Blue 600",
    "#1976d2": "Blue 700",
    "#1565c0": "Blue 800",
    "#0d47a1": "Blue 900",
    "#82b1ff": "Blue A100",
    "#448aff": "Blue A200",
    "#2979ff": "Blue A400",
    "#2962ff": "Blue A700",
    "#e1f5fe": "Light Blue 50",
    "#b3e5fc": "Light Blue 100",
    "#81d4fa": "Light Blue 200",
    "#4fc3f7": "Light Blue 300",
    "#29b6f6": "Light Blue 400",
    "#03a9f4": "Light Blue 500",
    "#039be5": "Light Blue 600",
    "#0288d1": "Light Blue 700",
    "#0277bd": "Light Blue 800",
    "#01579b": "Light Blue 900",
    "#80d8ff": "Light Blue A100",
    "#40c4ff": "Light Blue A200",
    "#00b0ff": "Light Blue A400",
    "#0091ea": "Light Blue A700",
    "#e0f7fa": "Cyan 50",
    "#b2ebf2": "Cyan 100",
    "#80deea": "Cyan 200",
    "#4dd0e1": "Cyan 300",
    "#26c6da": "Cyan 400",
    "#00bcd4": "Cyan 500",
    "#00acc1": "Cyan 600",
    "#0097a7": "Cyan 700",
    "#00838f": "Cyan 800",
    "#006064": "Cyan 900",
    "#84ffff": "Cyan A100",
    "#18ffff": "Cyan A200",
    "#00e5ff": "Cyan A400",
    "#00b8d4": "Cyan A700",
    "#e0f2f1": "Teal 50",
    "#b2dfdb": "Teal 100",
    "#80cbc4": "Teal 200",
    "#4db6ac": "Teal 300",
    "#26a69a": "Teal 400",
    "#009688": "Teal 500",
    "#00897b": "Teal 600",
    "#00796b": "Teal 700",
    "#00695c": "Teal 800",
    "#004d40": "Teal 900",
    "#a7ffeb": "Teal A100",
    "#64ffda": "Teal A200",
    "#1de9b6": "Teal A400",
    "#00bfa5": "Teal A700",
    "#e8f5e9": "Green 50",
    "#c8e6c9": "Green 100",
    "#a5d6a7": "Green 200",
    "#81c784": "Green 300",
    "#66bb6a": "Green 400",
    "#4caf50": "Green 500",
    "#43a047": "Green 600",
    "#388e3c": "Green 700",
    "#2e7d32": "Green 800",
    "#1b5e20": "Green 900",
    "#b9f6ca": "Green A100",
    "#69f0ae": "Green A200",
    "#00e676": "Green A400",
    "#00c853": "Green A700",
    "#f1f8e9": "Light Green 50",
    "#dcedc8": "Light Green 100",
    "#c5e1a5": "Light Green 200",
    "#aed581": "Light Green 300",
    "#9ccc65": "Light Green 400",
    "#8bc34a": "Light Green 500",
    "#7cb342": "Light Green 600",
    "#689f38": "Light Green 700",
    "#558b2f": "Light Green 800",
    "#33691e": "Light Green 900",
    "#ccff90": "Light Green A100",
    "#b2ff59": "Light Green A200",
    "#76ff03": "Light Green A400",
    "#64dd17": "Light Green A700",
    "#f9fbe7": "Lime 50",
    "#f0f4c3": "Lime 100",
    "#e6ee9c": "Lime 200",
    "#dce775": "Lime 300",
    "#d4e157": "Lime 400",
    "#cddc39": "Lime 500",
    "#c0ca33": "Lime 600",
    "#afb42b": "Lime 700",
    "#9e9d24": "Lime 800",
    "#827717": "Lime 900",
    "#f4ff81": "Lime A100",
    "#eeff41": "Lime A200",
    "#c6ff00": "Lime A400",
    "#aeea00": "Lime A700",
    "#fffde7": "Yellow 50",
    "#fff9c4": "Yellow 100",
    "#fff59d": "Yellow 200",
    "#fff176": "Yellow 300",
    "#ffee58": "Yellow 400",
    "#ffeb3b": "Yellow 500",
    "#fdd835": "Yellow 600",
    "#fbc02d": "Yellow 700",
    "#f9a825": "Yellow 800",
    "#f57f17": "Yellow 900",
    "#ffff8d": "Yellow A100",
    "#ffff00": "Yellow A200",
    "#ffea00": "Yellow A400",
    "#ffd600": "Yellow A700",
    "#fff8e1": "Amber 50",
    "#ffecb3": "Amber 100",
    "#ffe082": "Amber 200",
    "#ffd54f": "Amber 300",
    "#ffca28": "Amber 400",
    "#ffc107": "Amber 500",
    "#ffb300": "Amber 600",
    "#ffa000": "Amber 700",
    "#ff8f00": "Amber 800",
    "#ff6f00": "Amber 900",
    "#ffe57f": "Amber A100",
    "#ffd740": "Amber A200",
    "#ffc400": "Amber A400",
    "#ffab00": "Amber A700",
    "#fff3e0": "Orange 50",
    "#ffe0b2": "Orange 100",
    "#ffcc80": "Orange 200",
    "#ffb74d": "Orange 300",
    "#ffa726": "Orange 400",
    "#ff9800": "Orange 500",
    "#fb8c00": "Orange 600",
    "#f57c00": "Orange 700",
    "#ef6c00": "Orange 800",
    "#e65100": "Orange 900",
    "#ffd180": "Orange A100",
    "#ffab40": "Orange A200",
    "#ff9100": "Orange A400",
    "#ff6d00": "Orange A700",
    "#fbe9e7": "Deep Orange 50",
    "#ffccbc": "Deep Orange 100",
    "#ffab91": "Deep Orange 200",
    "#ff8a65": "Deep Orange 300",
    "#ff7043": "Deep Orange 400",
    "#ff5722": "Deep Orange 500",
    "#f4511e": "Deep Orange 600",
    "#e64a19": "Deep Orange 700",
    "#d84315": "Deep Orange 800",
    "#bf360c": "Deep Orange 900",
    "#ff9e80": "Deep Orange A100",
    "#ff6e40": "Deep Orange A200",
    "#ff3d00": "Deep Orange A400",
    "#dd2c00": "Deep Orange A700",
    "#efebe9": "Brown 50",
    "#d7ccc8": "Brown 100",
    "#bcaaa4": "Brown 200",
    "#a1887f": "Brown 300",
    "#8d6e63": "Brown 400",
    "#795548": "Brown 500",
    "#6d4c41": "Brown 600",
    "#5d4037": "Brown 700",
    "#4e342e": "Brown 800",
    "#3e2723": "Brown 900",
    "#fafafa": "Grey 50",
    "#f5f5f5": "Grey 100",
    "#eeeeee": "Grey 200",
    "#e0e0e0": "Grey 300",
    "#bdbdbd": "Grey 400",
    "#9e9e9e": "Grey 500",
    "#757575": "Grey 600",
    "#616161": "Grey 700",
    "#424242": "Grey 800",
    "#212121": "Grey 900",
    "#eceff1": "Blue Grey 50",
    "#cfd8dc": "Blue Grey 100",
    "#b0bec5": "Blue Grey 200",
    "#90a4ae": "Blue Grey 300",
    "#78909c": "Blue Grey 400",
    "#607d8b": "Blue Grey 500",
    "#546e7a": "Blue Grey 600",
    "#455a64": "Blue Grey 700",
    "#37474f": "Blue Grey 800",
    "#263238": "Blue Grey 900",
    "#000000": "Black",
    "#ffffff": "White",
}

# The Material Design named colors.
MATERIALDESIGN_NAMES_TO_HEX = dict(zip(MATERIALDESIGN_HEX_TO_NAMES.values(), MATERIALDESIGN_HEX_TO_NAMES.keys()))


def normalize_hex(hex_value: str) -> str:
    """
    Normalize a hexadecimal color value to 6 digits, lowercase.
    """
    match = HEX_COLOR_RE.match(hex_value)
    if match is None:
        raise ValueError("'{}' is not a valid hexadecimal color value.".format(hex_value))
    hex_digits = match.group(1)
    if len(hex_digits) == 3:
        hex_digits = "".join(2 * s for s in hex_digits)
    return "#{}".format(hex_digits.lower())


def _normalize_integer_rgb(value: int) -> int:
    """
    Internal normalization function for clipping integer values into
    the permitted range (0-255, inclusive).
    """
    return 0 if value < 0 else 255 if value > 255 else value


def normalize_integer_triplet(rgb_triplet: IntTuple) -> IntegerRGB:
    """
    Normalize an integer ``rgb()`` triplet so that all values are
    within the range 0-255 inclusive.
    """
    return IntegerRGB._make(_normalize_integer_rgb(value) for value in rgb_triplet)


def hex_to_rgb(hex_value: str) -> IntegerRGB:
    """
    Convert a hexadecimal color value to a 3-tuple of integers
    suitable for use in an ``rgb()`` triplet specifying that color.
    """
    int_value = int(normalize_hex(hex_value)[1:], 16)
    return IntegerRGB(int_value >> 16, int_value >> 8 & 0xFF, int_value & 0xFF)


def rgb_to_hex(rgb_triplet: IntTuple) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal value for that color.
    """
    return "#{:02x}{:02x}{:02x}".format(*normalize_integer_triplet(rgb_triplet))


def glob_path_match(path, pattern_list):
    """
    Checks if path is in a list of glob style wildcard paths
    :param path: path of file / directory
    :param pattern_list: list of wildcard patterns to check for
    :return: Boolean
    """
    return any(fnmatch(path, pattern) for pattern in pattern_list)


def get_files_recursive(root, d_exclude_list=None, f_exclude_list=None, ext_include_list=None, primary_root=None):
    """
    Walk a path to recursively find files
    Modified version of https://stackoverflow.com/a/56077673 that includes file ext inclusion list
    :param root: path to explore
    :param d_exclude_list: list of root relative directories paths to exclude
    :param f_exclude_list: list of filenames without paths to exclude
    :param ext_include_list: list of file extensions to include, ex: ['.log', '.bak']
    :param primary_root: Only used for internal recursive exclusion lookup, don't pass an argument here
    :return: list of files found in path
    """

    if d_exclude_list is not None:
        # Make sure we use a valid os separator for exclusion lists, this is done recursively :(
        d_exclude_list = [os.path.normpath(d) for d in d_exclude_list]
    else:
        d_exclude_list = []
    if f_exclude_list is None:
        f_exclude_list = []
    if ext_include_list is None:
        ext_include_list = []

    files = [
        os.path.join(root, f)
        for f in os.listdir(root)
        if os.path.isfile(os.path.join(root, f))
        and not glob_path_match(f, f_exclude_list)
        and os.path.splitext(f)[1] in ext_include_list
    ]
    dirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
    for d in dirs:
        p_root = os.path.join(primary_root, d) if primary_root is not None else d
        if not glob_path_match(p_root, d_exclude_list):
            files_in_d = get_files_recursive(
                os.path.join(root, d), d_exclude_list, f_exclude_list, ext_include_list, primary_root=p_root
            )
            if files_in_d:
                for f in files_in_d:
                    files.append(os.path.join(root, f))
    return files


def rgb_to_name(rgb_triplet: IntTuple) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.
    If there is no matching name, ``ValueError`` is raised.
    """

    rgb = np.array(rgb_triplet)
    nearest_rgb = RGB[spatial.KDTree(RGB).query(rgb)[1]]
    hex_value = rgb_to_hex(IntegerRGB(nearest_rgb[0], nearest_rgb[1], nearest_rgb[2]))
    try:
        name = MATERIALDESIGN_HEX_TO_NAMES[hex_value]
    except KeyError:
        raise ValueError("'{}' has no defined color name in {}".format(hex_value, MATERIALDESIGN_HEX_TO_NAMES))
    diff = (
        "("
        + "{0:+d}".format(nearest_rgb[0] - rgb[0])
        + ", "
        + "{0:+d}".format(nearest_rgb[1] - rgb[1])
        + ", "
        + "{0:+d}".format(nearest_rgb[2] - rgb[2])
        + ")"
    )
    print('Closest color to ({}, {}, {}) is "{}": "{}", {}.'.format(rgb[0], rgb[1], rgb[2], hex_value, name, diff))

    return name


def hex_to_hsv(hex_value: str):
    r, g, b = hex_to_rgb(hex_value)
    return colorsys.rgb_to_hsv(r, g, b)


def get_colors(root: str) -> Counter:
    ctr = Counter()
    for drawable in get_files_recursive(root, ext_include_list=[".xml"]):
        with open(drawable) as file:
            for line in file.readlines():
                m = HEX_XML_COLOR_RE.findall(line)
                if m:
                    ctr.update(m)

    return ctr


def save_csv(in_file: str, out_file: str):
    with open(in_file, newline="") as fin, open(out_file, "w", newline="") as fout:
        rdr = csv.DictReader(fin)
        fieldnames = ["_Red", "_Green", "_Blue"]
        fieldnames.extend(rdr.fieldnames)
        wrtr = csv.DictWriter(fout, fieldnames=fieldnames)
        wrtr.writeheader()
        for row in rdr:
            hex_value = row["_Hex"]
            r, g, b = hex_to_rgb(hex_value)
            row["_Red"] = r
            row["_Green"] = g
            row["_Blue"] = b
            wrtr.writerow(row)


def save_xml(in_file: str, out_file: str):
    iterable = get_colors(in_file)
    hex_values = list(iterable)

    # print(hex_values)
    hex_values.sort(key=hex_to_hsv)
    # print(hex_values)

    out_f = open(out_file, "w")

    out_f.write('<?xml version="1.0" encoding="utf-8"?>')
    out_f.write("\r\n")
    out_f.write("<resources>")
    out_f.write("\r\n")

    for color in hex_values:
        cnt = iterable[color]
        name = rgb_to_name(hex_to_rgb(color))
        material_color = MATERIALDESIGN_NAMES_TO_HEX[name]

        if cnt > 1:
            comment_1 = " " + "<!--" + "Number of times used: " + '"' + str(cnt) + '"' + "-->"
        else:
            comment_1 = " " + "<!--" + "Used only once!" + "-->"

        if color != material_color:
            comment_2 = " " + "<!--" + "color don't match, closest color: " + '"' + material_color + '"' + "-->"
        else:
            comment_2 = ""

        out_f.write("    " + '<color name="' + name.replace(" ", "_").lower() + '">' + color.upper() + "</color>")
        out_f.write(comment_1)
        out_f.write(comment_2)
        out_f.write("\r\n")

    out_f.write("</resources>")
    out_f.write("\r\n")
    out_f.close()


if __name__ == "__main__":
    # def main(argv):
    try:
        dir_in = sys.argv[1]
    except IndexError:
        print("Usage: " + sys.argv[0] + " -i <inputdir> -o <outputfile>")
        sys.exit(2)

# Provide default file_out name argument if not provided:
if __name__ == "__main__":
    # def main(argv):
    try:
        file_out = sys.argv[2]
    except IndexError:
        file_out = "colors" + ".xml"

# Change this accordingly
# save_csv("@Material-Design.palette.csv", "@Material-Design-Color.palette.csv")

save_xml(dir_in, file_out)

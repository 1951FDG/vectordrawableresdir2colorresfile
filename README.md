# Converts a vector drawable resource directory into a color resource file

This is used to find and replace usages of colors in vector drawables (e.g., to force usage of colors in the Material Design spec only).

## Table of Contents

<details>
<summary>"Click to expand"</summary>

-   [Installation](#installation)
-   [Usage](#usage)
-   [Requirements](#requirements)
-   [Feedback](#feedback)
-   [Credits](#credits)
-   [Built with](#built-with)
-   [Attributions](#attributions)
-   [Acknowledgments](#acknowledgments)

</details>

## Installation

```bash
# Common dependencies
python3 -m pip install numpy
python3 -m pip install scipy
```

## Usage

```bash
cd vectordrawableresdir2colorresfile
python3 vectordrawableresdir2colorresfile.py ../MyApplication/app/src/main/res/drawable
```

## Requirements

To run the Python script you'll need:

-   [Python 3.6.0 or higher](https://www.python.org/downloads/)

## Feedback

Feel free to send us feedback by submitting an [issue](https://github.com/1951FDG/vectordrawableresdir2colorresfile/issues). Bug reports, feature requests, patches, and well-wishes are always welcome.

> **Note**:
> Pull requests are welcome. For major changes, please submit an issue first to discuss what you would like to change.

## Credits

-   [Optimized RGB-To-ColorName](https://github.com/ayushoriginal/Optimized-RGB-To-ColorName)
    -   Modified [rgbcsv2rgbarray.py](rgbcsv2colorarray.py)
    -   Modified [rgbcsv2colordict.py](rgbcsv2colordict.py)

## Built with

-   [Atom](https://atom.io/)

## Attributions

-   [Material Design Color Palette](https://github.com/anseki/vscode-color/blob/master/palettes/%40Material-Design.palette.csv)
-   [Webcolors](https://github.com/ubernostrum/webcolors)

## Acknowledgments

Special thanks to [Optimized RGB-To-ColorName](https://github.com/ayushoriginal/Optimized-RGB-To-ColorName) for the algorithm that identifies the name of a color closest to an RGB value provided as input.

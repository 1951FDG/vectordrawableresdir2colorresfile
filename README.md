# vectordrawableresdir2colorresfile

Converts a vector drawable resource directory into a color resource file.

This is used to find and replace usages of colors in vector drawables (e.g., to force usage of colors in the Material Design spec only).

## Table of Contents

<details>
<summary>"Click to expand"</summary>

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Advanced usage](#advanced-usage)
- [Requirements](#requirements)
- [Feedback](#feedback)
- [Credits](#credits)
- [Built with](#built-with)
- [Attributions](#attributions)
- [Acknowledgments](#acknowledgments)

</details>

## Prerequisites

```sh
pip3 install -r requirements.txt
```

## Usage

The command below will output a `colors.xml` file in directory `vectordrawableresdir2colorresfile`

```sh
cd vectordrawableresdir2colorresfile
python3 vectordrawableresdir2colorresfile.py $project/app/src/main/res/drawable
```

## Advanced usage

To ensure the script has no external dependencies, an array and dictionary is used instead of input files.

If you want to use other color palettes:

```sh
python3 rgbcsv2colorarray.py @Material-Design-Color.palette.csv
```

Open output file `rgbcsv2colorarray.py.txt` and paste content into vectordrawableresdir2colorresfile.py

```sh
python3 rgbcsv2colordict.py @Material-Design-Color.palette.csv
```

Open output file `rgbcsv2colordict.py.txt` and paste content into vectordrawableresdir2colorresfile.py

## Requirements

To run the Python script you'll need:

- Python 3.6.0 or higher

## Feedback

Feel free to send us feedback by submitting an [issue](https://github.com/1951FDG/vectordrawableresdir2colorresfile/issues). Bug reports, feature requests, patches, and well-wishes are always welcome.

> **Note**:
> Pull requests are welcome. For major changes, please submit an issue first to discuss what you would like to change.

## Credits

- [Optimized RGB-To-ColorName](https://github.com/ayushoriginal/Optimized-RGB-To-ColorName)
    - Modified [rgbcsv2rgbarray.py](rgbcsv2colorarray.py)
    - Modified [rgbcsv2colordict.py](rgbcsv2colordict.py)

## Built with

- [Atom](https://atom.io)

## Attributions

- [Material Design Color Palette](https://github.com/anseki/vscode-color/blob/master/palettes/%40Material-Design.palette.csv)
- [Webcolors](https://github.com/ubernostrum/webcolors)

## Acknowledgments

Special thanks to [Optimized RGB-To-ColorName](https://github.com/ayushoriginal/Optimized-RGB-To-ColorName) for the algorithm that identifies the name of a color closest to an RGB value provided as input.

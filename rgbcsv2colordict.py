# by 1951FDG, Wilson Mar

from __future__ import print_function

import csv
import os.path
import sys
import time
import timeit

# Begin timer:
start_time = timeit.default_timer()


def program(*args):
    # do whatever
    pass


# Provide default file_in name argument if not provided:
if __name__ == "__main__":
    # def main(argv):
    try:
        file_in = sys.argv[1]
    except IndexError:  # getopt.GetoptError:
        print("Usage: " + sys.argv[0] + " -i <inputfile> -o <outputfile>")
        sys.exit(2)

# Exit if file_in not found:
if os.path.exists(file_in) and os.access(file_in, os.R_OK):
    with open(file_in, newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for i in reader:
            header_rows = (
                "# "
                + time.strftime("%Y-%m-%d %H:%M (local time)")
                + " "
                + sys.argv[0]
                + " START: rowcount="
                + str(sum(1 for _ in f))
                + "."
            )
            print(header_rows)
else:
    print(
        "# "
        + time.strftime("%Y-%m-%d %H:%M (local time)")
        + " "
        + sys.argv[0]
        + " ABORTED. Either file "
        + file_in
        + " is missing or is not readable."
    )
    sys.exit()

# Provide default file_out name argument if not provided:
if __name__ == "__main__":
    # def main(argv):
    try:
        file_out = sys.argv[2]
    except IndexError:  # getopt.GetoptError:
        # Name output file by appending .txt to the name:
        file_out = sys.argv[0] + ".txt"

# Send STDOUT to a file:
stdout = sys.stdout  # remember the handle to the real standard output.
sys.stdout = open(file_out, "w")

# Print in black format:

with open(file_in, newline="") as in_f:
    reader = csv.DictReader(in_f, delimiter=",")
    print("HEX_TO_NAMES = {")
    rownum = 0
    for i in reader:
        print("    " + '"' + i["_Hex"] + '": "' + i["_Title"] + '"' + ",")
        rownum = rownum + 1
    print("}")

footer_rows = (
    "# "
    + time.strftime("%Y-%m-%d")
    + " "
    + os.path.basename(sys.argv[0])
    + " "
    + os.path.basename(file_out)
    + " output "
    + str(rownum)
    + " rows."
)
print(footer_rows, end="")  # no NewLine

# Close the file every time:
sys.stdout.close()

sys.stdout = stdout  # Restore regular stdout.

# End timer:
elapsed = timeit.default_timer() - start_time
print(
    "# "
    + time.strftime("%Y-%m-%d %H:%M (local time)")
    + " "
    + sys.argv[0]
    + " END: ran for "
    + "{:.2f}".format(elapsed * 1000)
    + " secs."
)
print(footer_rows)

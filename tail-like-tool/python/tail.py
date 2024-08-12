#!/usr/bin/env python3
# https://docs.python.org/3/tutorial/inputoutput.html
"""
Exercise:
---------
  Implement a tail(1)-like tool, which prints last N lines (provided as a param) from a file

  Arguments:
  ----------
  +===============+=========+=======================================================================+
  |   Argument    |  Type   |                              Description                              |
  +===============+=========+=======================================================================+
  | --file <file> | string  | The path to the <file> to be processed                                |
  +---------------+---------+-----------------------------------------------------------------------+
  | -n <number>   | integer | Last <number> of lines to be printed.                                 |
  +---------------+---------+-----------------------------------------------------------------------+
  | -f            | bool    | Watch for the new entries and print them on stdout until interrupted. |
  +---------------+---------+-----------------------------------------------------------------------+
  ################################################################################################### OR
  Parameters:
  -----------
  +===============+=========+=======================================================================+
  |   Parameter   |  Type   |                              Description                              |
  +===============+=========+=======================================================================+
  | file          | string  | The path to the file to be processed.                                 |
  +---------------+---------+-----------------------------------------------------------------------+
  | lines.        | integer | Number of lines to be printed from the end of the file                |
  +---------------+---------+-----------------------------------------------------------------------+
  | follow        | bool    | Watch for the new entries and print them on stdout until interrupted  |
  +---------------+---------+-----------------------------------------------------------------------+
"""

class Tail():
    def __init__(self):
        self.input_file = "./inputs.txt"
        with open(self.input_file, "a") as f:
            for i in range(1, 100):
                f.write(f"This is the line number {i}\n")
    
    def get_inputs(self):
        self.inputs = []
        with open(self.input_file, "r") as inputs:
            for line in inputs.readlines():
                self.inputs.append(line)
        return self.inputs


if __name__ == "__main__":
    tail = Tail()
    print(tail.get_inputs())



#
# SPDX-FileCopyrightText: 2020 John Samuel <johnsamuelwrites@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

import csv
import re
from shexstatements.shexstatementsparser import ShExStatementLexerParser

class CSV:
  @staticmethod
  def generate_shex_from_data_string(data):
    shexstatement = ""
    try:
      lexerparser = ShExStatementLexerParser()
      lexerparser.build()
      lexerparser.buildparser()
      tokens = lexerparser.input(data)
      result = lexerparser.parse(data)
      shexstatement = result.generate_shex()
    except Exception as e:
      print("Unable to parse. Error: " + str(e))
    return shexstatement
    
  @staticmethod
  def generate_shex_from_csv(filepath, delim=",", skip_header=False):
    shexstatement = ""
    try:
      pattern = '^\s*$'
      data = ""
      with open(filepath, 'r') as csvfile:
       csvreader = csv.reader(csvfile, delimiter=delim)
       rowno = 0
       for row in csvreader:
         rowno = rowno + 1
         if skip_header and rowno == 1:
          continue 
         line = ""
         for value in row:
           if value and not re.match(pattern, value):
             if not line:
               line = value
             else:
               line = line + "|" + value
         data = data + line + "\n"
      shexstatement = CSV.generate_shex_from_data_string(data)
    except Exception as e:
      print("Unable to read file. Error: " + str(e))
    return shexstatement


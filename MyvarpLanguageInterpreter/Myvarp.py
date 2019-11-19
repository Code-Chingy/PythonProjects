import os
import sys

from MyvarpCompiler import MyvarpCompile
from MyvarpRunner import MyvarpRun
from utils.base.myvarp_script_interpreter import MyvarpScriptInterpreter

args = sys.argv

"""

Author : chingy
This script defines words that are passes in.
could be a word or a bunch of words
use Myvarp.py -h or --help for help


        session = MyvarpScriptInterpreter()
        # session.read("", _return=True)
        while True:
            if session.process_output == "...":
                line = input('   ... ')
                session.add_line(line)
                session.run_line()
            else:
                line = input('mv >>> ')

                if str(line) == 'exit()' or str(line) == 'quit()' or str(line) == ':q':
                    break
                elif str(line) == 'clear()' or str(line) == 'clean()':
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    session.add_line(line)
                    session.run_line()

"""


def main(argv):
    if len(argv) > 0:
        if argv[0] == "-h" or argv[0] == "-help":
            print("\nhelp on Myvarp ..how to run how to convert to python file")
        else:
            MyvarpCompile(argv[0])
    else:
        print(
            "##############################################################################################################")
        print(
            "##                                  Myvarp By TechupStudio @Copyright 2018                                  ##")
        print(
            "##                                          Version 1.0 Build 0001                                          ##")
        print(
            "##############################################################################################################\n")

        session = MyvarpScriptInterpreter()

        while True:

            if session.is_comments_active():
                line = input('   ... ')
                session.add_line(line+"\n")
                session.run_script()
            else:
                line = input('mv >>> ')

                if str(line) == 'exit()' or str(line) == 'quit()' or str(line) == ':q':
                    break
                elif str(line) == 'clear()' or str(line) == 'clean()':
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    session.add_line(line+"\n")
                    session.run_script()


if __name__ == "__main__":
    main(args[1:])

# # !/usr/bin/python3
# import sys, getopt
#
# def main(argv):
#     inputfile = ''
#     outputfile = ''
#     try:
#         opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
#     except getopt.GetoptError:
#         print('test.py -i <inputfile> -o <outputfile>')
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print('test.py -i <inputfile> -o <outputfile>')
#             sys.exit()
#         elif opt in ("-i", "--ifile"):
#             inputfile = arg
#         elif opt in ("-o", "--ofile"):
#             outputfile = arg
#             print('Input file is "', inputfile)
#             print('Output file is "', outputfile)
#
#
# if __name__ == "__main__":
#     main(sys.argv[1:])
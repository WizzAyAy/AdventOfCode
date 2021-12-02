# wget on the url of the input for a day
import sys
import os
from dotenv import load_dotenv

load_dotenv()
sessionID = os.getenv('session')

if len(sys.argv) != 2:
    print("[DAY]")

day = sys.argv[2]

mkdir = "mkdir Day" + str(day)

os.system(mkdir)

curl = "curl \"https://adventofcode.com/2021/day/"+str(day)+"/input\" -H \"Cookie: " \
       "session=" + sessionID + ">\" > Day" + str(day) + "/input.txt"

os.system(curl)

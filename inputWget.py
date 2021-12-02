# wget on the url of the input for a day
import sys
import os
from dotenv import load_dotenv

load_dotenv()
sessionID = os.getenv('session')

if len(sys.argv) != 4:
    print("[FILE_NAME] [URL] [DAY]")

file_name = sys.argv[1].replace(" ", "")
url = sys.argv[2]
day = sys.argv[3]

mkdir = "mkdir Day" + str(day)

os.system(mkdir)

touch = "touch Day" + str(day) + "/" + file_name + ".py"
os.system(touch)

curl = "curl \"https://adventofcode.com/2021/day/1/input\" -H \"Cookie: " \
       "session=" + sessionID + ">\" "

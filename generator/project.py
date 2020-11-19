from model.project import Project
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 20
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.ascii_lowercase + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(name="", status="", view_status="", description="")] + [
    Project(name=random_string("project-name", 10), status=random.choice(["development", "release"]), view_status=random.choice(["private", "public"]), description="desc" + str(random.randrange(50)))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out_file:
    jsonpickle.set_encoder_options("json", indent=2)
    out_file.write(jsonpickle.encode(testdata))
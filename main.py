import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--func_way", type=str)
parser.add_argument("--mark_way", type=str, default="markup.txt")
parser.add_argument("--save_test", type=str, default="tests")
args = parser.parse_args()

def func(a, b):
    return a ** 2 + 2 * a * b + b ** 2

template = '''import unittest

class Main(unittest.TestCase):
    def test(self):
        [T]
try: unittest.main()
except: pass'''

meta_ = open(args.mark_way, "r").read()

meta_ = re.sub(r"\t", "", meta_)

res_prepare = meta_.split("\n")
res = ""
for i in res_prepare[1:]:
    data = re.sub(r":","", res_prepare[0]) + "(" + re.search(r"(\d+, \d+)", i)[0] + ")"
    result = re.sub(re.search(r"(\d+, \d+)", i)[0], " ", i)
    result = re.search(r"\d+", result)[0]
    res += "self.assertEqual({}, {})".format(data, result) + "\n        "

result = re.sub(r"\[T]", res[:-2], template)
result = "from " + args.func_way + " import " + re.sub(r":", "", res_prepare[0]) + "\n" + result

with open(args.save_test + ".py", "w") as file:
	file.write(result)

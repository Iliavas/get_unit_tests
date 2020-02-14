import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--func_path", type=str)
parser.add_argument("--mark_path", type=str, default="markup.txt")
parser.add_argument("--save_test", type=str, default="tests")
args = parser.parse_args()

template = '''import unittest

class Main(unittest.TestCase):
    def test(self):
        [T]
try: unittest.main()
except: pass'''

meta_ = open(args.mark_path, "r").read()

meta_ = re.sub(r"\t", "", meta_)

res_prepare = meta_.split("\n")
res = ""
for i in res_prepare[1:]:
    data = re.sub(r":","", res_prepare[0])  + ', '.join(re.findall(r"[^,]+", re.search(r"\(.*\)", i)[0])) 
    print(i)
    result = re.sub(r"\(.+\)", "", i)
    result = re.search(r"[^,]+", result)[0]
    res += "self.assertEqual({}, {})".format(data, result) + "\n        "

result = re.sub(r"\[T]", res[:-2], template)
result = "from " + args.func_path + " import " + re.sub(r":", "", res_prepare[0]) + "\n" + result

with open(args.save_test + ".py", "w") as file:
	file.write(result)

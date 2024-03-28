import argparse
import json
import random
parser = argparse.ArgumentParser(description="キラキラジェネレーター（仮） 制作:GNUWood (2024)",add_help=True)

parser.add_argument('-n','--name', help="最初に来る名前を指定します。")
parser.add_argument('-c','--count', help="生成数を指定します。", type=int, default=1)

args = parser.parse_args()
if args.name:
    name = args.name
else:
    name = "きりたん"

with open("dict.json", "r") as f:
    data = json.load(f)

if args.count:
    for i in range(args.count):
        print(f"""{name}
{random.choice(data["middle"])}
{random.choice(data["end"])}
""")
else:
    print(f"""{name}
{random.choice(data["middle"])}
{random.choice(data["end"])}""")

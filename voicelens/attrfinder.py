import argparse
import json
import os
import re

attr_pattern = re.compile(r'\{(?P<attr>[a-zA-Z0-9_]+)\}')


def main() : 
    parser = argparse.ArgumentParser()
    parser.add_argument('webpage', type=str)
    args = parser.parse_args()

    with open(args.webpage) as f : 
        webpage = f.read()

    targets = {name : "" for name in attr_pattern.findall(webpage)}

    with open('targets.json', 'w') as f : 
        f.write(json.dumps(targets))

  


if __name__ == '__main__' : 
    main()


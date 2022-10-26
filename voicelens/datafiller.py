import argparse
import json
import os



def main() : 
    parser = argparse.ArgumentParser()
    parser.add_argument('webpage', type=str)
    parser.add_argument('contents', type=str)
    parser.add_argument('out', type=str)
    args = parser.parse_args()

    with open(args.webpage) as f : 
        webpage = f.read()

    with open(args.contents) as f : 
        contents = json.loads(f.read())

    try : 
        mapped_page = webpage.format(**contents)
    except BaseException as e:
        print(f'abort with : {e}')
        exit(0)
    
    with open(args.out, 'w') as f : 
        f.write(mapped_page)


if __name__ == '__main__' : 
    main()


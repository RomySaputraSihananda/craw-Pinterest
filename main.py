from argparse import ArgumentParser;
from Pinterest import Pinterest, logging
from json import dumps
import os 

if(__name__ == '__main__'):
    argp: ArgumentParser = ArgumentParser()
    argp.add_argument("--keyword", '-k', type=str, default='Freya')
    argp.add_argument("--size", '-s', type=int, default=10)
    argp.add_argument("--download", '-d', type=bool, default=False)
    argp.add_argument("--output", '-o', type=str, default='data')
    args = argp.parse_args()

    pinterest: Pinterest = Pinterest()

    if(not os.path.exists(args.output)):
            os.makedirs(args.output)

    with open(f'{args.output}/{args.keyword}.json', 'w') as file:
        file.write(dumps(pinterest.search(keyword=args.keyword, size=args.size, download=args.download, output=args.output), indent=2, ensure_ascii=False))

    logging.info('finish.....')
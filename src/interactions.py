import argparse
from api_connections import translate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='text to translate')
    parser.add_argument('-s', '--src', default=None, help='origin language of the text')
    parser.add_argument('-d', '--dest', default=None, help='destiny language of the translation')
    parser.add_argument('-v', '--verbose', help='show more information', action='store_true')

    args = parser.parse_args()

    tr = translate(args.text, args.src, args.dest)

    if args.verbose:
        print('original text: %s' % tr.origin)
        print('translated text: %s' % tr.text)
        print('origin language: %s' % tr.src)
        print('destiny language: %s' % tr.dest)
    else:
        print(tr.text)

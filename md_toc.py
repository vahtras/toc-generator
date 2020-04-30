def toc(stream):
    toc = {}
    page = 1
    for line in stream:

        if line.startswith('---'):
            page += 1
        if line.startswith('#'):
            toc[line.strip()] = page

    retstr = "# TOC\n"
    for k, v in toc.items():
        if k.startswith('# '):
            h1 = k.strip('# ')
            retstr += f"* [{h1}](#{v})\n"
        if k.startswith('## '):
            h2 = k.strip('## ')
            retstr += f"  + [{h2}](#{v})\n"

    return retstr


def main():

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='File name')

    args = parser.parse_args()

    with open(args.filename) as f:
        print(toc(f))


if __name__ == "__main__":
    main()

from Pinterest import Pinterest

if(__name__ == '__main__'):
    pinterest: Pinterest = Pinterest()

    print(pinterest.search('video hinata hyuga', size=5))
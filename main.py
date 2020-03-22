from my_file import my_open


def main():
    with my_open('my_file.py') as f:
        print f.read(1000)

    with my_open('stam.txt', 'w') as f:
        print f.write('I love bananas')

    try:
        f = my_open(r'my_file.py')
        print f.read(1000)
    finally:
        f.close()


if __name__ == '__main__':
    main()

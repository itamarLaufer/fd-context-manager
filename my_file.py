import os


class MyFile(object):
    MODES = {'r': os.O_RDONLY, 'w': os.O_WRONLY}

    def __init__(self, path, mode):
        self.path = path
        self.fd = None
        if mode in self.MODES:
            self.mode = self.MODES[mode]
        else:
            raise ValueError('An illegal mode was passed!')
        self.fd = os.open(self.path, self.mode)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fd:
            self.close()

    def read(self, n=1):
        return os.read(self.fd, n)

    def write(self, content):
        os.write(self.fd, content)

    def close(self):
        os.close(self.fd)


def my_open(path, mode='r'):
    return MyFile(path, mode)

from abc import ABC, abstractmethod


class Reader(ABC):
    def __init__(self, path):
        self.path = path
        self.content = ''
        self.parse()

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, new_content):
        self._content = new_content

    @abstractmethod
    def parse(self):
        pass


class Linereader(Reader):
    def parse(self):
        with open(self.path, "r") as file:
            self.content = [line.strip() for line in file.readlines()]


class Flatreader(Reader):
    def parse(self):
        with open(self.path, "r") as file:
            self.content = file.read()

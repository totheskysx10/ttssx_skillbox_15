import os


class ModifiedFile:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        if os.path.exists(self.filename):
            self.file = open(self.filename, self.mode, encoding='UTF-8')
        else:
            print("файл не существует, создаем его в режиме записи")
            self.file = open(self.filename, 'w', encoding='UTF-8')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return True

import time
GEMINI_API_KEY = 'AIzaSyAKu9Q7-mhKylp8zZKBwxatsM6IfUmaAPA'

USE_FULL_PIPELINE = False

RAW_ARTICLE_PATH = 'data/raw_article.txt'

class SaveToCache:
    def __init__(self, path: str, text: str, rewrite: bool = False):
        self.path = path
        self.text = text
        self.rewrite = rewrite

    def save(self):
        if not self.rewrite:
            timestamp = str(int(time.time()))
            self.path += f'_{timestamp}'
        self.path = f'cache/{self.path}.txt'

        mode = 'w' if self.rewrite else 'x'
        try:
            with open(self.path, mode) as file:
                file.write(self.text)
        except FileExistsError:
            if self.rewrite:
                with open(self.path, 'w') as file:
                    file.write(self.text)
            else:
                print(
                    f"File '{self.path}' already exists. Set 'rewrite=True' to overwrite.")


if __name__ == '__main__':
    filename = __file__.rsplit('/', 1)[-1][:-3]
    saver = SaveToCache(filename, 'test\ntest2', rewrite=True)
    saver.save()

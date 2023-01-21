class NewsFeed:
    def __init__(self):
        self.posts = []
        self._watchers = []

    def register(self, watcher):
        self._watchers.append(watcher)

    def post(self, message):
        self.posts.append(message)
        for w in self._watchers:
            w.notify(message)


class User:
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f'{self.name} got a new notification: "{message}"')


if __name__ == "__main__":
    nf = NewsFeed()
    nf.register(User("Adam"))
    nf.post("Hello!")
    nf.register(User("Kate"))
    nf.post("Hello again!")

class System:
    def __init__(self):
        self.status = "down"
        self.watchers = []

    def add_watcher(self, watcher):
        self.watchers.append(watcher)

    def change_status(self, new_status):
        self.status = new_status
        for w in self.watchers:
            w.notify(new_status)


class SystemNotifications:
    def notify(self, status):
        print(f"Your system changed status to {status}")


class UserInterface:
    def notify(self, status):
        if status == "up":
            print("Bringing up the UI")


if __name__ == "__main__":
    s = System()
    s.add_watcher(SystemNotifications())
    s.add_watcher(UserInterface())

    s.change_status("up")

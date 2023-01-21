import os
import requests


class User:
    def status(self):
        user = os.environ.get("USER") or os.environ.get("USERNAME")
        return f"Current user: {user}"


class Directory:
    def status(self):
        return f"Current working dir: {os.getcwd()}"


class Internet:
    def status(self):
        try:
            internet_ok = requests.get("https://google.com").status_code == 200
        except requests.exceptions.ConnectionError:
            internet_ok = False
        connection = "ok" if internet_ok else "offline"
        return f"Internet connection: {connection}"


class CheckSystem:
    _systems = [User(), Directory(), Internet()]

    def status(self):
        for s in self._systems:
            print(s.status())


if __name__ == "__main__":
    cs = CheckSystem()
    cs.status()

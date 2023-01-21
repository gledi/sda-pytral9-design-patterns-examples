import os
import requests


class User:
    def status(self):
        user = os.environ.get("USER") or os.environ.get("USERNAME")
        return f"Current user: {user}"


class Directory:
    def status(self):
        return f"Current working dir: {os.getcwd()}"


class CheckSystem:
    _systems = [User(), Directory()]

    def status(self):
        for s in self._systems:
            print(s.status())
        try:
            internet_ok = requests.get("https://google.com").status_code == 200
        except requests.exceptions.ConnectionError:
            internet_ok = False
        connection = "ok" if internet_ok else "offline"
        print(f"Internet connection: {connection}")


if __name__ == "__main__":
    cs = CheckSystem()
    cs.status()

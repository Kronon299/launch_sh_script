from dataclasses import dataclass


class TaskMain:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self.__state = "New"

    def __str__(self):
        return f"Task name: {self._name}\nTask description: {self._description}"

    def __repr__(self):
        return self.__str__()

    def progress(self):
        if self.__state == "New":
            self.__state = "In Progress"
            print('Task state was set to "In Progress"')
        elif self.__state == "In Progress":
            print('Task state was set to "Done"')
            self.__state = "Done"
        else:
            print('Task state is already "Done"')


@dataclass
class User:
    name: str


from dataclasses import dataclass


class Task:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self.__state = "New"

    def __str__(self):
        return f"Task name: {self._name}\nTask description: {self._description}"

    def __repr__(self):
        return str(self)

    def progress(self):
        if self.__state == "New":
            self.__state = "In Progress"
            print('Task state was set to "In Progress"')
        elif self.__state == "In Progress":
            print('Task state was set to "Done"')
            self.__state = "Done"
        else:
            print('Task state is already "Done"')

    def get_state(self):
        return self.__state


@dataclass
class User:
    name: str


class MainTaskHandler:
    def __init__(self):
        self.active_user = None
        self.active_task = None
        self.command = None
        self.data = {}

    def ask_for_command(self):
        self.command = str(input('please, input a command: '))
        return self.command

    def create_user(self, name: str):
        self.active_user = User(name)
        self.data[self.active_user.name] = []

    def create_task(self, user: str, task_name: str, task_description: str):
        self.active_task = Task(name=task_name, description=task_description)
        if user in self.data:
            self.data[user].append(self.active_task)
        else:
            self.create_user(user)
            self.create_task(user=user, task_name=task_name, task_description=task_description)


if __name__ == '__main__':
    handler = MainTaskHandler()
    while True:
        command = handler.ask_for_command()
        if command.lower() == 'exit':
            break

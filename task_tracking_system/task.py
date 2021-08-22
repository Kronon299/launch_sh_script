from models import User, Task, Session, Base


class MainTaskHandler:
    def __init__(self):
        self.active_user = None
        self.active_task = None
        self.command = None
        self.session = Session()  # Is it ok?
        Base.metadata.create_all()

    def ask_for_command(self):
        self.command = str(input('please, input a command: '))
        return self.command

    def create_user(self, name: str):
        self.active_user = User(username=name)
        self.session.add(self.active_user)
        self.session.commit()
        print(f'User created: {self.active_user}')
        return self.active_user

    def create_task(self, task_name: str, task_description: str):
        if not self.active_user:
            pass
        self.active_task = Task(title=task_name, description=task_description, user_id=self.active_user.id)
        self.session.add(self.active_task)
        self.session.commit()
        print(f'Task created: {self.active_task}')
        return self.active_task

    def check_active_user(self):
        return self.active_user


if __name__ == '__main__':
    handler = MainTaskHandler()
    handler.create_user(name='matt')
    # while True:
    #     command = handler.ask_for_command()
    #     if command.lower() == 'exit':
    #         break

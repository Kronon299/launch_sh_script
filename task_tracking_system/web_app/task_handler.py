from models.models import User, Task, Session, Base
from sqlalchemy.orm.exc import NoResultFound


class MainTaskHandler:
    def __init__(self):
        self.active_user = None
        self.active_task = None
        self.session = Session()
        Base.metadata.create_all()

    def ask_for_command(self):
        command = str(input('please, input a command: ')).lower()
        print(self.workflow(command=command))
        return command

    def create_user(self, name: str):
        """
        Create a new user
        :param name: User name
        :return: active user
        """
        self.active_user = User(name=name)
        self.session.add(self.active_user)
        self.session.commit()
        print(f'User created: {self.active_user}')
        return self.active_user

    def get_users(self):
        # self.active_user_init()
        users = self.session.query(User).all()
        return users

    def active_user_init(self):
        if self.active_user:
            return self.active_user
        else:
            self.active_user = self.ask_for_user()
            return self.active_user

    def ask_for_user(self):
        user_name = str(input('please, input a user name: ')).lower()
        try:
            user_obj = self.session.query(User).filter(
                User.username == user_name,
            ).one()
            print(f'User {user_obj} found in the database and selected as current active user')
        except NoResultFound:
            print(f'User {user_name} was not found in the database and will be created.')
            user_obj = self.create_user(user_name)
        return user_obj

    def create_task(self, task_name: str, task_description: str):
        if not self.active_user:
            self.active_user = self.active_user_init()
        self.active_task = Task(title=task_name, description=task_description, user_id=self.active_user.id)
        self.session.add(self.active_task)
        self.session.commit()
        print(f'Task created: {self.active_task}')
        return self.active_task

    def get_tasks(self):
        self.active_user_init()
        tasks = self.session.query(Task).filter(
            Task.user_id == self.active_user.id
        ).all()
        return tasks

    def select_task(self):
        task_number = int(input('please, input a task number: '))
        task = self.session.query(Task).filter(
            Task.id == task_number
        ).first()
        if task:
            self.active_task = task
            return self.active_task

    def workflow(self, command: str):
        if command == 'help':
            return 'Help text will be here.'
        elif command == 'show user':
            return f'Active user: {self.active_user_init()}'
        elif command == 'create user':
            return f'Active user: {self.ask_for_user()}'
        elif command == 'show task':
            if self.active_task:
                return f'Active task: {self.active_task}'
            else:
                return 'No active task'
        elif command == 'show all tasks':
            tasks_list = [(task.id, task.title, task.state) for task in self.get_tasks()]
            return f'Tasks for {self.active_user}: {tasks_list}'
        elif command == 'select task':
            if self.select_task():
                return f'Task selected: {self.active_task}'
            else:
                return f'Task did not selected. Current active task: {self.active_task}'
        elif command == 'create task':
            task_name = str(input('please, input a task name: ')).lower()
            task_description = str(input('please, input a task description: ')).lower()
            self.create_task(task_name=task_name, task_description=task_description)
        elif command == 'set in progress':
            if self.active_task:
                self.active_task.state = 'in progress'
                self.session.add(self.active_task)
                self.session.commit()
                return f'State "in progress" was set for task {self.active_task.title}'
            else:
                return 'Task was not selected, try command "select task".'
        elif command == 'set done':
            if self.active_task:
                self.active_task.state = 'done'
                self.session.add(self.active_task)
                self.session.commit()
                return f'State "done" was set for task {self.active_task.title}'
            else:
                return 'Task was not selected, try "select task" command.'
        else:
            return 'Please, input a correct command.'


if __name__ == '__main__':
    handler = MainTaskHandler()
    # handler.ask_for_user()
    # handler.create_user(name='matt')
    while True:
        ask_command = handler.ask_for_command()
        if ask_command.lower() == 'exit':
            handler.session.close()
            break

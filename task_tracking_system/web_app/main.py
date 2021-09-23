from app import app
from task_handler import MainTaskHandler

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True
    )
    handler = MainTaskHandler()

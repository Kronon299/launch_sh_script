from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship

engine = create_engine("sqlite:///example.db")
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)

    tasks = relationship("Task", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    description = Column(String(256), nullable=True)
    state = Column(String(256), nullable=False, default='new')
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    user = relationship(User, back_populates="tasks")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, user={self.user_id}, state={self.state})"

    def __repr__(self):
        return str(self)


def create_user(username: str) -> User:
    """
    :param username:
    :return:
    """

    u = User(username=username)
    print("id before:", u.id)
    session.add(u)
    session.commit()
    print("id after:", u.id)
    return u


if __name__ == '__main__':
    Base.metadata.create_all()
    session = Session()
    try:
        u = create_user("sam")
    except IntegrityError:
        print('this user name already exists')

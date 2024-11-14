from time import sleep


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False) -> None:
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self) -> str:
        return self.title

    def __contains__(self, string):
        return string.lower() in self.title.lower()


class User:
    def __init__(self, nickname: str, password: str, age: int) -> None:
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return (self.nickname, self.password, self.age) == (other.nickname, other.password, other.age)
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        if isinstance(other, User):
            return (self.nickname, self.password, self.age) != (other.nickname, other.password, other.age)
        return NotImplemented

    def __str__(self) -> str:
        return self.nickname


class UrTube:
    users: list = []
    videos: list = []
    current_user: User = None

    def log_in(self, nickname: str, password: str) -> None:
        if (nickname, hash(password)) in map(lambda u: (u.nickname, u.password), self.__class__.users):
            self.__class__.current_user = next(filter(lambda u: u.nickname == nickname and u.password is hash(password),
                                            self.__class__.users))

    def register(self, nickname: str, password: str, age: int) -> None:
        user = User(nickname, password, age)
        if user.nickname not in map(lambda u: u.nickname, self.__class__.users):
            self.__class__.users.append(user)
            self.__class__.current_user = user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self) -> None:
        self.__class__.current_user = None

    def add(self, *args: Video) -> None:
        for arg in args:
            if arg not in self.__class__.videos:
                self.__class__.videos.append(arg)

    def get_videos(self, title: str) -> list:
        return [str(video) for video in self.__class__.videos if title.lower() in video.title.lower()]

    def watch_video(self, title: str) -> None:
        if self.__class__.current_user:
            for video in self.__class__.videos:
                if title == video.title:
                    if not video.adult_mode or (video.adult_mode and self.__class__.current_user.age >= 18):
                        for sec in range(video.time_now + 1, video.duration + 1):
                            print(sec, end=' ')
                            sleep(1)
                        else:
                            print('Конец видео')
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')

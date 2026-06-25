# Паттерн «Facade»

## Идея
Facade даёт один простой вход в набор сложных подсистем.

## Пример

```python
class Audio:
    def on(self) -> str:
        return "audio on"


class Video:
    def on(self) -> str:
        return "video on"


class HomeTheaterFacade:
    def __init__(self) -> None:
        self.audio = Audio()
        self.video = Video()

    def start_movie(self) -> list[str]:
        return [self.audio.on(), self.video.on()]
```

## Когда применять

- если наружу нужен один удобный метод;
- если подсистем много, а пользоваться ими неудобно;
- если нужно скрыть порядок вызовов.

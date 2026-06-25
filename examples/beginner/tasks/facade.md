# Задача: Facade

## Условие
Есть несколько подсистем, но наружу нужен один простой метод.

## Идея
Фасад прячет сложность и даёт короткий интерфейс.

## Решение

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

## Когда удобно

- если пользовательский код не должен знать детали подсистем;
- если нужно скрыть длинную последовательность вызовов;
- если хочется один простой вход в сложную логику.

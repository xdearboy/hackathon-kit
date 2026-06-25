# Паттерн «Адаптер»

## Идея
Адаптер нужен, когда два объекта не совпадают по интерфейсу, но их надо заставить работать вместе.

Типичный случай:

- одно устройство умеет вызывать `connect_to_hdmi()`;
- другое устройство умеет только `connect_usb_c()`;
- адаптер переводит один интерфейс в другой.

## Задача

Есть ноутбук с HDMI и проектор с USB-C. Нужно сделать адаптер, чтобы ноутбук мог подключить проектор как будто это HDMI-устройство.

## Решение

```python
class Laptop:
    def connect_to_hdmi(self, device):
        return device.connect_to_hdmi()


class Projector:
    def connect_usb_c(self):
        return "📽️ Проектор: принимаю сигнал через USB-C"


class USBToHDMIAdapter:
    def __init__(self, projector):
        self.projector = projector

    def connect_to_hdmi(self):
        return self.projector.connect_usb_c()


laptop = Laptop()
projector = Projector()
adapter = USBToHDMIAdapter(projector)

print(laptop.connect_to_hdmi(adapter))
```

## Что здесь важно

- `Laptop` работает только с методом `connect_to_hdmi()`.
- `Projector` умеет только `connect_usb_c()`.
- `USBToHDMIAdapter` добавляет нужный метод `connect_to_hdmi()`, но внутри вызывает `connect_usb_c()`.

## Как запомнить

Адаптер не меняет объект внутри. Он просто даёт ему удобный интерфейс снаружи.

## Частая форма в задачах

```python
class Target:
    def request(self):
        return "target"


class Adaptee:
    def specific_request(self):
        return "adaptee"


class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()
```

## Когда использовать

- если чужой класс уже написан и менять его неудобно;
- если надо подружить старый код с новым интерфейсом;
- если в задаче специально просят паттерн Adapter.

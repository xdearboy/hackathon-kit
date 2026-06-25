# Задача: Adapter

## Условие
Есть ноутбук, который умеет подключаться только по HDMI. Есть проектор, который принимает только USB-C.
Нужно сделать адаптер, чтобы ноутбук мог работать с проектором без изменения его кода.

## Идея
Ноутбук вызывает `connect_to_hdmi()`. Адаптер сам хранит проектор и внутри вызывает у него `connect_usb_c()`.

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
```

## Вывод

```python
laptop = Laptop()
projector = Projector()
adapter = USBToHDMIAdapter(projector)
print(laptop.connect_to_hdmi(adapter))
```

# Строки

## Срезы
Срезы работают быстро и читаются хорошо.

```python
s = "hackathon"
print(s[0])
print(s[:4])
print(s[4:])
print(s[::-1])
```

Индексы:

- `s[i]` — один символ;
- `s[a:b]` — от `a` до `b - 1`;
- `s[a:b:c]` — с шагом `c`;
- строка неизменяемая, поэтому менять символ по месту нельзя.

## Полезные методы

- `split`, `rsplit`
- `strip`, `lstrip`, `rstrip`
- `find`, `replace`
- `startswith`, `endswith`
- `join`

```python
text = "  hello, world  "
parts = text.strip().split(", ")
print(parts)
print("-".join(["a", "b", "c"]))
```

Ещё чаще нужны:

```python
text = "abracadabra"
print(text.find("cad"))
print(text.count("a"))
print(text.replace("a", "A"))
print(text.startswith("ab"))
print(text.endswith("ra"))
```

Разбиение строк:

```python
line = "1  2   3"
print(line.split())
print("a,b,c".split(","))
```

## f-строки
Самый удобный способ собрать строку.

```python
name = "Arseniy"
score = 42
print(f"{name}: {score}")
print(f"{score:.2f}")
```

Полезно помнить:

```python
value = 12.34567
print(f"{value:.1f}")
print(f"{value:08.2f}")
print(f"{name=!r}")
```

## Регулярки
Используй для поиска, валидации и вырезания шаблонов.

```python
import re

text = "id=123; user=alice"
match = re.search(r"id=(\d+)", text)
if match:
    print(match.group(1))

words = re.findall(r"[a-z]+", text)
print(words)
```

Частые шаблоны:

```python
re.findall(r"\d+", "a1 b22 c333")
re.sub(r"\s+", " ", "a   b    c")
re.fullmatch(r"[a-z_][a-z0-9_]*", "var_1")
```

Когда нужна регулярка:

- извлечь числа, email, теги, id;
- проверить формат строки;
- заменить множество похожих фрагментов.

## Практика

```python
def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())
```

```python
def is_palindrome(text: str) -> bool:
    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]
```

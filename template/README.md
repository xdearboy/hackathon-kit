# Template Guide

## Как использовать

1. Открой `template/main.py`.
2. Замени `src/solution.py` на логику своей задачи.
3. Если задача совсем простая, оставь `solve_procedural()`.
4. Запускай через `uv run python main.py < input.txt`.

## Мини-пример

Если надо прочитать `n` и вывести сумму `n` чисел:

`main.py`:

```python
from src.solution import Solution


def main() -> None:
    print(Solution().solve(), end="")


if __name__ == "__main__":
    main()
```

`src/solution.py`:

```python
class Solution:
    def solve(self) -> str:
        n = int(input())
        values = list(map(int, input().split()))
        return f"{sum(values[:n])}\n"
```

## Как быстро адаптировать

- читать строки через `input()`;
- список чисел делать через `list(map(int, input().split()))`;
- ответ возвращать строкой;
- если ответов много, собирать их в список и потом делать `"\n".join(...)`.

## Когда упростить ещё сильнее

- если вход маленький, не усложняй I/O;
- если формат стандартный, пиши решение прямо в `solve()`;
- если нужен быстрый прототип, можно начать с procedural-версии и потом при желании перенести в класс.

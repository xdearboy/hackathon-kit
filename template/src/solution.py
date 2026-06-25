class Solution:
    def solve(self) -> str:
        n = int(input())
        values = list(map(int, input().split()))
        return f"{sum(values[:n])}\n"


def solve_procedural() -> str:
    n = int(input())
    values = list(map(int, input().split()))
    return f"{sum(values[:n])}\n"

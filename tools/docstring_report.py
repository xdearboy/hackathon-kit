import ast
import sys
from pathlib import Path


def iter_python_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(file_path for file_path in path.rglob("*.py") if "__pycache__" not in file_path.parts)


def report_file(file_path: Path) -> int:
    tree = ast.parse(file_path.read_text(encoding="utf-8"), filename=str(file_path))
    missing = 0

    for node in ast.walk(tree):
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and ast.get_docstring(node) is None:
            print(f"{file_path}:{node.lineno} {node.__class__.__name__} {node.name}")
            missing += 1

    return missing


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/docstring_report.py path", file=sys.stderr)
        return 2

    target = Path(sys.argv[1]).resolve()
    if not target.exists():
        print(f"Path not found: {target}", file=sys.stderr)
        return 2

    total = 0
    for file_path in iter_python_files(target):
        total += report_file(file_path)

    if total == 0:
        print("No missing docstrings found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

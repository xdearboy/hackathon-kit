import ast
import sys
from pathlib import Path


def format_args(args: ast.arguments) -> str:
    items = [arg.arg for arg in args.posonlyargs + args.args if arg.arg != "self"]
    if args.vararg:
        items.append(f"*{args.vararg.arg}")
    items.extend(arg.arg for arg in args.kwonlyargs)
    if args.kwarg:
        items.append(f"**{args.kwarg.arg}")
    return ", ".join(items)


def build_skeleton(node: ast.AST) -> str:
    if isinstance(node, ast.ClassDef):
        return f'"""{node.name}."""'
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = format_args(node.args)
        if args:
            return f'"""{node.name}.\n\nArgs:\n    {args}.\n"""'
        return f'"""{node.name}."""'
    raise TypeError(type(node))


def walk(nodes: list[ast.stmt], prefix: str = "") -> None:
    for node in nodes:
        if isinstance(node, ast.ClassDef):
            name = f"{prefix}{node.name}"
            if ast.get_docstring(node) is None:
                print(f"{name}:\n{build_skeleton(node)}\n")
            walk(node.body, f"{name}.")
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            name = f"{prefix}{node.name}"
            if ast.get_docstring(node) is None:
                print(f"{name}:\n{build_skeleton(node)}\n")
            walk(node.body, f"{name}.")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/docstring_skeleton.py path", file=sys.stderr)
        return 2

    file_path = Path(sys.argv[1]).resolve()
    tree = ast.parse(file_path.read_text(encoding="utf-8"), filename=str(file_path))
    walk(tree.body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

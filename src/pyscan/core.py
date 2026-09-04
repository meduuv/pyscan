import ast


def scan_source(source):
    """Return a compact structural report for Python source code."""
    tree = ast.parse(source)
    imports = []
    functions = []
    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
    return {
        "lines": len(source.splitlines()),
        "imports": sorted(set(imports)),
        "functions": sorted(functions),
        "classes": sorted(classes),
    }

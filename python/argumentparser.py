from rich.tree import Tree
from rich.pretty import Pretty


def get_type_str(type_str: str) -> str:
    _, t, _ = str(type_str).split("'")
    return t


def inspect_ArgumentParser(obj, tree: Tree) ->  None:
    if "argparse." in get_type_str(type(obj)):
        obj = obj.__dict__

    for key, val in obj.items():
        if val and "argparse." in get_type_str(type(val)):
            branch = tree.add(f"[red]{key}[/red]")
            inspect_ArgumentParser(val, branch)
        else:
            linestr = f"[dim][steel_blue1]{key}[/steel_blue1] ([yellow]{type(val)}[/yellow])"
            if not val:
                linestr = f"{linestr}: [slate_blue3]{val}[/slate_blue3]"
            elif isinstance(val, str):
                linestr = f"{linestr}: [green]\"{val}\"[/green]"
            linestr += "[/dim]"
            temp_branch = tree.add(linestr)
            if val and not isinstance(val, str):
                temp_branch.add(Pretty(val))
from pathlib import Path

import tests


def abs_path_to_project(relative_path: str) -> str:
    return str(Path(tests.__file__).parent.parent.joinpath(relative_path))

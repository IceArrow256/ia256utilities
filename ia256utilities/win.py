import enum
import os
import pathlib as pl


class LinkType(enum.Enum):
    D = 0
    H = 1
    J = 2


def mklink(src: str, dst: str, link_type: LinkType):
    """
    src - specifies the path (relative or absolute) that the new symbolic link refers to.
    dst - specifies the name of the symbolic link that is being created.
    link_type:
        LinkType.D - creates a directory symbolic link. By default, mklink creates a file symbolic link.
        LinkType.H - creates a hard link instead of a symbolic link.
        LinkType.J - creates a Directory Junction.
    """
    if link_type == LinkType.D:
        arg = "d"
    elif link_type == LinkType.H:
        arg = "h"
    elif link_type == LinkType.J:
        arg = "j"
    else:
        raise ValueError("link_type must be 0, 1, 2")
    if os.path.exists(dst):
        os.rmdir(dst)
    pl.Path(dst).parent.mkdir(parents=True, exist_ok=True)
    os.system(f'mklink /{arg} "{dst}" "{src}"')

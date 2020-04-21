import hashlib


def get_sha256(file_path: str) -> str:
    """
    Gets a hash(SHA-256) of a file by the path
    """
    with open(file_path, "rb") as f:
        b = f.read()
        readable_hash = hashlib.sha256(b).hexdigest()
    return readable_hash

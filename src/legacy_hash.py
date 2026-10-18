"""DEMO: kode tidak aman untuk menguji Quality Gate. Jangan di-merge ke main."""
import hashlib


def weak_hash(password: str) -> str:
    return hashlib.md5(password.encode("utf-8")).hexdigest()
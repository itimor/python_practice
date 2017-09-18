def md5(text):
    import hashlib
    m = hashlib.md5()
    t = text.encode(encoding="utf-8")
    m.update(t)
    return m.hexdigest()
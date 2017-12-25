from scripts import mongodb


def mongo_test():
    assert mongodb.test() is False
    mongodb.install()
    assert mongodb.test() is True
    mongodb.uninstall()
    assert mongodb.test() is False

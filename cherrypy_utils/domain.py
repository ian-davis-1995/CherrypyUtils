_domain = "/"


def set_domain(new_domain):
    global _domain
    _domain = new_domain


def get_domain():
    return _domain


def get_domain_for_template():
    return _domain if _domain != "/" else ""

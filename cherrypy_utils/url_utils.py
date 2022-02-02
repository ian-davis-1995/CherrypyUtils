def combine_url(domain, *parts):
    if domain == "/":
        return "/" + "/".join(parts)

    return "/" + domain.strip("/") + "/" + "/".join(parts)

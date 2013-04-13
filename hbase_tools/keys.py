from decorators import initialize_date


@initialize_date(to_datestr=True)
def human_date(date=None):
    return date


@initialize_date(to_datestr=True)
def reversed_human_date(date=None):
    """Returns a date formatted like 8000-93-95

    The numbers can be thought of as days until 9999-99-99"""
    def filtered(x):
        if x == "-":
            return x
        return str(9 - int(x))

    return "r" + "".join([filtered(x) for x in date])

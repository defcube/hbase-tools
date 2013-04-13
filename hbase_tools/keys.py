from decorators import initialize_date


@initialize_date(to_datestr=True)
def human_date(date=None):
    return date


@initialize_date(to_datestr=True)
def reversed_human_date(date=None):
    def filtered(x):
        if x == "-":
            return x
        return str(9 - int(x))

    return "r" + "".join([filtered(x) for x in date])

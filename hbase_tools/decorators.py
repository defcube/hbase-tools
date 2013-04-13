from datetime import datetime
import inspect


def initialize_date(to_datestr=False):
    """
    Looks for an argument named "date" and initializes it to today if it's None
    """

    def f(func):
        date_arg_pos = inspect.getargspec(func).args.index('date')

        def filter_date(d):
            if d is None:
                d = datetime.now()
            if to_datestr:
                return d.strftime("%Y-%m-%d")
            else:
                return d

        def f2(*args, **kwargs):
            if len(args) >= date_arg_pos + 1:
                args = list(args)
                args[date_arg_pos] = filter_date(args[date_arg_pos])
            else:
                kwargs["date"] = filter_date(kwargs.get("date", None))
            return func(*args, **kwargs)

        return f2

    return f

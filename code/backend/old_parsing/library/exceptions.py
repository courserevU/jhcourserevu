from parsing.library.utils import pretty_json


class PipelineException(Exception):
    """Data-pipeline exception class.
    Should never be constructed directly. Use:
        - PipelineError
        - PipelineWarning
    """

    def __init__(self, data, *args):
        """Construct PipelineError instance.
        Add data to args.
        Args:
            data: Prettified if possible.
            *args
        """
        if isinstance(data, dict):
            try:
                data = pretty_json(data)
            except TypeError:
                pass
        super(PipelineException, self).__init__(data, *args)

    def __str__(self):
        """String representation of error with newlines.
        Returns:
            str
        """
        return "\n" + "\n".join(map(str, self.args))


class PipelineError(PipelineException):
    """Data-pipeline error class."""


class PipelineWarning(PipelineException, UserWarning):
    """Data-pipeline warning class."""


class ParseError(PipelineError):
    """Parser error class."""


class ParseWarning(PipelineWarning):
    """Parser warning class."""


class ParseJump(PipelineWarning):
    """Parser exception used for control flow."""
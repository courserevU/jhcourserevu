from abc import ABCMeta, abstractmethod

from parsing.library.ingestor import Ingestor
from parsing.library.requester import Requester


class BaseParser(metaclass=ABCMeta):
    """Abstract base parser for data pipeline parsers.
    Attributes:
        extractor (:obj:`parsing.library.extractor.Extractor`)
        ingestor (:obj:`parsing.library.ingestor.Ingestor`)
        requester (:obj:`parsing.library.requester.Requester`)
        school (:obj:`str`): School that parser is for.
    """

    def __init__(
        self,
        school,
        config=None,
        output_path=None,
        output_error_path=None,
        break_on_error=True,
        break_on_warning=False,
        skip_duplicates=True,
        display_progress_bar=False,
        validate=True,
        tracker=None,
    ):
        """Create base parser instance.
        Args:
            school (str): The subject school.
            config (None, dict, optional): Configuration dictionary.
            output_path (None, str, optional)
            output_error_path (None, str, optional)
            break_on_error (bool, optional)
            break_on_warning (bool, optional)
            skip_duplicates (bool, optional): TODO
            display_progress_bar (bool, optional)
            validate (bool, optional): Flag to validate or not.
            tracker (None, Tracker, optional): Tracker to track parse.
        """
        self.school = school
        self.requester = Requester()
        self.tracker = tracker
        self.ingestor = Ingestor(
            config,
            output_path,
            break_on_error=break_on_error,
            break_on_warning=break_on_warning,
            skip_duplicates=skip_duplicates,
            display_progress_bar=display_progress_bar,
            validate=validate,
            tracker=self.tracker,
        )

    @abstractmethod
    def start(self, **kwargs):
        """Start the parse.
        Args:
            **kwargs: expanded in child parser.
        """

    def end(self):
        """Finish the parse."""
        self.ingestor.end()
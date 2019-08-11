from abc import ABCMeta, abstractmethod


class AbstractSingletonFangModel(ABCMeta):
    """
    This is an abstract, singleton class for model implementation classes to
    inherit.

    Why singleton? Some models like homoglyph may have an expensive
    initialization like setting up translation tables.
    """

    _singleton_registry = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._singleton_registry:
            cls._singleton_registry[cls] =\
                super(AbstractSingletonFangModel, cls).__call__(*args, **kwargs)
        return cls._singleton_registry[cls]

    @abstractmethod
    def defang(self, ioc: str):
        """Defangs an indicator of compromise.

        Keyword arguments:
        ioc -- the indicator of compromise
        """

    @abstractmethod
    def refang(self, text: str):
        """Refangs a piece of text.

        Keyword arguments:
        text -- the text to refang
        """

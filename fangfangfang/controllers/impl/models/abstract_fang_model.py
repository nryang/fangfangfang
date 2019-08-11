from abc import ABCMeta, abstractmethod


class AbstractSingletonFangModel(ABCMeta):

    _singleton_registry = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._singleton_registry:
            cls._singleton_registry[cls] =\
                super(AbstractSingletonFangModel, cls).__call__(*args, **kwargs)
        return cls._singleton_registry[cls]

    @abstractmethod
    def defang(self, ioc: str):
        pass

    @abstractmethod
    def refang(self, text: str):
        pass

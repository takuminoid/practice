import abc

class ConfigInfo(metaclass=abc.ABCMeta):
    CLASS_NAME = "AppInfoLoader4"
    
    @abc.abstractmethod
    def get_version(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_class_name(self):
        raise NotImplementedError
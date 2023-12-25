# インスタンスが常に一つであることを保証する
class RegisterNote():
    __instance = None
    
    def __init__(self):
        if RegisterNote.__instance is None:
            RegisterNote.__instance = self
    
    def _register_note(self):
        pass

    @staticmethod
    def get_instance():
        return RegisterNote.__instance

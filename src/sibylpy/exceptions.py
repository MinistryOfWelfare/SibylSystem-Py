class GeneralException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        
class InvalidTokenException(GeneralException):
    def __init__(self) -> None:
        super().__init__(message="Token is invalid")
        
class InvalidPermissionRangeException(GeneralException):
    def __init__(self, message: str) -> None:
        super().__init__(message)
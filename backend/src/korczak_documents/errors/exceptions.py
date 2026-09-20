class AppError(Exception):
    def __init__(self, message: str, code: str = "application_error", status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code


class NotFoundError(AppError):
    def __init__(self, message: str = "Recurso não encontrado"):
        super().__init__(message, code="not_found", status_code=404)


class ValidationError(AppError):
    def __init__(self, message: str = "Dados inválidos"):
        super().__init__(message, code="validation_error", status_code=422)

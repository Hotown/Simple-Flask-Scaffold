from app.exception.BaseException import set_error_message


def formErrorException():
    code = 200
    data = 'validate error'

    return set_error_message(code,data)
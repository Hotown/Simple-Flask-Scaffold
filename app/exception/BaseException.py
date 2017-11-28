from app.exception.global_error_handle import handle_error


def set_error_message(code,data):
    return handle_error({'code': code, 'data': data})



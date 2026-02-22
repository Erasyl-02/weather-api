class ApiException(Exception):
    pass

class BadRequestError(ApiException):
    '''HTTP Status code 400'''
    pass

class EndpointError(ApiException):
    '''HTTP Status code 404'''
    pass

class AuthenticationError(ApiException):
    '''HTTP Status code 401'''
    pass

class TooManyRequestsError(ApiException):
    '''HTTP Status code 429'''
    pass

class ExternalServerError(ApiException):
    '''HTTP Status code 500'''
    pass
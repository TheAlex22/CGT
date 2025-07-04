# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import helpers as module_0


def test_case_0():
    int_0 = 309
    var_0 = module_0.has_message_body(int_0)
    assert var_0 is True
    assert module_0.STATUS_CODES == {
        100: b"Continue",
        101: b"Switching Protocols",
        102: b"Processing",
        103: b"Early Hints",
        200: b"OK",
        201: b"Created",
        202: b"Accepted",
        203: b"Non-Authoritative Information",
        204: b"No Content",
        205: b"Reset Content",
        206: b"Partial Content",
        207: b"Multi-Status",
        208: b"Already Reported",
        226: b"IM Used",
        300: b"Multiple Choices",
        301: b"Moved Permanently",
        302: b"Found",
        303: b"See Other",
        304: b"Not Modified",
        305: b"Use Proxy",
        307: b"Temporary Redirect",
        308: b"Permanent Redirect",
        400: b"Bad Request",
        401: b"Unauthorized",
        402: b"Payment Required",
        403: b"Forbidden",
        404: b"Not Found",
        405: b"Method Not Allowed",
        406: b"Not Acceptable",
        407: b"Proxy Authentication Required",
        408: b"Request Timeout",
        409: b"Conflict",
        410: b"Gone",
        411: b"Length Required",
        412: b"Precondition Failed",
        413: b"Request Entity Too Large",
        414: b"Request-URI Too Long",
        415: b"Unsupported Media Type",
        416: b"Requested Range Not Satisfiable",
        417: b"Expectation Failed",
        418: b"I'm a teapot",
        422: b"Unprocessable Entity",
        423: b"Locked",
        424: b"Failed Dependency",
        426: b"Upgrade Required",
        428: b"Precondition Required",
        429: b"Too Many Requests",
        431: b"Request Header Fields Too Large",
        451: b"Unavailable For Legal Reasons",
        500: b"Internal Server Error",
        501: b"Not Implemented",
        502: b"Bad Gateway",
        503: b"Service Unavailable",
        504: b"Gateway Timeout",
        505: b"HTTP Version Not Supported",
        506: b"Variant Also Negotiates",
        507: b"Insufficient Storage",
        508: b"Loop Detected",
        510: b"Not Extended",
        511: b"Network Authentication Required",
    }
    var_1 = var_0.__repr__()
    assert var_1 == "True"


def test_case_1():
    bool_0 = module_0.is_atty()
    assert bool_0 is False
    assert module_0.STATUS_CODES == {
        100: b"Continue",
        101: b"Switching Protocols",
        102: b"Processing",
        103: b"Early Hints",
        200: b"OK",
        201: b"Created",
        202: b"Accepted",
        203: b"Non-Authoritative Information",
        204: b"No Content",
        205: b"Reset Content",
        206: b"Partial Content",
        207: b"Multi-Status",
        208: b"Already Reported",
        226: b"IM Used",
        300: b"Multiple Choices",
        301: b"Moved Permanently",
        302: b"Found",
        303: b"See Other",
        304: b"Not Modified",
        305: b"Use Proxy",
        307: b"Temporary Redirect",
        308: b"Permanent Redirect",
        400: b"Bad Request",
        401: b"Unauthorized",
        402: b"Payment Required",
        403: b"Forbidden",
        404: b"Not Found",
        405: b"Method Not Allowed",
        406: b"Not Acceptable",
        407: b"Proxy Authentication Required",
        408: b"Request Timeout",
        409: b"Conflict",
        410: b"Gone",
        411: b"Length Required",
        412: b"Precondition Failed",
        413: b"Request Entity Too Large",
        414: b"Request-URI Too Long",
        415: b"Unsupported Media Type",
        416: b"Requested Range Not Satisfiable",
        417: b"Expectation Failed",
        418: b"I'm a teapot",
        422: b"Unprocessable Entity",
        423: b"Locked",
        424: b"Failed Dependency",
        426: b"Upgrade Required",
        428: b"Precondition Required",
        429: b"Too Many Requests",
        431: b"Request Header Fields Too Large",
        451: b"Unavailable For Legal Reasons",
        500: b"Internal Server Error",
        501: b"Not Implemented",
        502: b"Bad Gateway",
        503: b"Service Unavailable",
        504: b"Gateway Timeout",
        505: b"HTTP Version Not Supported",
        506: b"Variant Also Negotiates",
        507: b"Insufficient Storage",
        508: b"Loop Detected",
        510: b"Not Extended",
        511: b"Network Authentication Required",
    }


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "y0I{}=d *+"
    list_0 = [str_0, str_0, str_0]
    module_0.is_entity_header(list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    dict_0 = {}
    default_0 = module_0.Default(**dict_0)
    assert module_0.STATUS_CODES == {
        100: b"Continue",
        101: b"Switching Protocols",
        102: b"Processing",
        103: b"Early Hints",
        200: b"OK",
        201: b"Created",
        202: b"Accepted",
        203: b"Non-Authoritative Information",
        204: b"No Content",
        205: b"Reset Content",
        206: b"Partial Content",
        207: b"Multi-Status",
        208: b"Already Reported",
        226: b"IM Used",
        300: b"Multiple Choices",
        301: b"Moved Permanently",
        302: b"Found",
        303: b"See Other",
        304: b"Not Modified",
        305: b"Use Proxy",
        307: b"Temporary Redirect",
        308: b"Permanent Redirect",
        400: b"Bad Request",
        401: b"Unauthorized",
        402: b"Payment Required",
        403: b"Forbidden",
        404: b"Not Found",
        405: b"Method Not Allowed",
        406: b"Not Acceptable",
        407: b"Proxy Authentication Required",
        408: b"Request Timeout",
        409: b"Conflict",
        410: b"Gone",
        411: b"Length Required",
        412: b"Precondition Failed",
        413: b"Request Entity Too Large",
        414: b"Request-URI Too Long",
        415: b"Unsupported Media Type",
        416: b"Requested Range Not Satisfiable",
        417: b"Expectation Failed",
        418: b"I'm a teapot",
        422: b"Unprocessable Entity",
        423: b"Locked",
        424: b"Failed Dependency",
        426: b"Upgrade Required",
        428: b"Precondition Required",
        429: b"Too Many Requests",
        431: b"Request Header Fields Too Large",
        451: b"Unavailable For Legal Reasons",
        500: b"Internal Server Error",
        501: b"Not Implemented",
        502: b"Bad Gateway",
        503: b"Service Unavailable",
        504: b"Gateway Timeout",
        505: b"HTTP Version Not Supported",
        506: b"Variant Also Negotiates",
        507: b"Insufficient Storage",
        508: b"Loop Detected",
        510: b"Not Extended",
        511: b"Network Authentication Required",
    }
    set_0 = {default_0}
    module_0.is_hop_by_hop_header(set_0)


def test_case_4():
    default_0 = module_0.Default()
    assert module_0.STATUS_CODES == {
        100: b"Continue",
        101: b"Switching Protocols",
        102: b"Processing",
        103: b"Early Hints",
        200: b"OK",
        201: b"Created",
        202: b"Accepted",
        203: b"Non-Authoritative Information",
        204: b"No Content",
        205: b"Reset Content",
        206: b"Partial Content",
        207: b"Multi-Status",
        208: b"Already Reported",
        226: b"IM Used",
        300: b"Multiple Choices",
        301: b"Moved Permanently",
        302: b"Found",
        303: b"See Other",
        304: b"Not Modified",
        305: b"Use Proxy",
        307: b"Temporary Redirect",
        308: b"Permanent Redirect",
        400: b"Bad Request",
        401: b"Unauthorized",
        402: b"Payment Required",
        403: b"Forbidden",
        404: b"Not Found",
        405: b"Method Not Allowed",
        406: b"Not Acceptable",
        407: b"Proxy Authentication Required",
        408: b"Request Timeout",
        409: b"Conflict",
        410: b"Gone",
        411: b"Length Required",
        412: b"Precondition Failed",
        413: b"Request Entity Too Large",
        414: b"Request-URI Too Long",
        415: b"Unsupported Media Type",
        416: b"Requested Range Not Satisfiable",
        417: b"Expectation Failed",
        418: b"I'm a teapot",
        422: b"Unprocessable Entity",
        423: b"Locked",
        424: b"Failed Dependency",
        426: b"Upgrade Required",
        428: b"Precondition Required",
        429: b"Too Many Requests",
        431: b"Request Header Fields Too Large",
        451: b"Unavailable For Legal Reasons",
        500: b"Internal Server Error",
        501: b"Not Implemented",
        502: b"Bad Gateway",
        503: b"Service Unavailable",
        504: b"Gateway Timeout",
        505: b"HTTP Version Not Supported",
        506: b"Variant Also Negotiates",
        507: b"Insufficient Storage",
        508: b"Loop Detected",
        510: b"Not Extended",
        511: b"Network Authentication Required",
    }


def test_case_5():
    default_0 = module_0.Default()
    assert module_0.STATUS_CODES == {
        100: b"Continue",
        101: b"Switching Protocols",
        102: b"Processing",
        103: b"Early Hints",
        200: b"OK",
        201: b"Created",
        202: b"Accepted",
        203: b"Non-Authoritative Information",
        204: b"No Content",
        205: b"Reset Content",
        206: b"Partial Content",
        207: b"Multi-Status",
        208: b"Already Reported",
        226: b"IM Used",
        300: b"Multiple Choices",
        301: b"Moved Permanently",
        302: b"Found",
        303: b"See Other",
        304: b"Not Modified",
        305: b"Use Proxy",
        307: b"Temporary Redirect",
        308: b"Permanent Redirect",
        400: b"Bad Request",
        401: b"Unauthorized",
        402: b"Payment Required",
        403: b"Forbidden",
        404: b"Not Found",
        405: b"Method Not Allowed",
        406: b"Not Acceptable",
        407: b"Proxy Authentication Required",
        408: b"Request Timeout",
        409: b"Conflict",
        410: b"Gone",
        411: b"Length Required",
        412: b"Precondition Failed",
        413: b"Request Entity Too Large",
        414: b"Request-URI Too Long",
        415: b"Unsupported Media Type",
        416: b"Requested Range Not Satisfiable",
        417: b"Expectation Failed",
        418: b"I'm a teapot",
        422: b"Unprocessable Entity",
        423: b"Locked",
        424: b"Failed Dependency",
        426: b"Upgrade Required",
        428: b"Precondition Required",
        429: b"Too Many Requests",
        431: b"Request Header Fields Too Large",
        451: b"Unavailable For Legal Reasons",
        500: b"Internal Server Error",
        501: b"Not Implemented",
        502: b"Bad Gateway",
        503: b"Service Unavailable",
        504: b"Gateway Timeout",
        505: b"HTTP Version Not Supported",
        506: b"Variant Also Negotiates",
        507: b"Insufficient Storage",
        508: b"Loop Detected",
        510: b"Not Extended",
        511: b"Network Authentication Required",
    }
    str_0 = default_0.__str__()
    assert str_0 == "<Default>"


def test_case_6():
    bool_0 = module_0.is_atty()
    assert bool_0 is False
    assert module_0.STATUS_CODES == {
        100: b"Continue",
        101: b"Switching Protocols",
        102: b"Processing",
        103: b"Early Hints",
        200: b"OK",
        201: b"Created",
        202: b"Accepted",
        203: b"Non-Authoritative Information",
        204: b"No Content",
        205: b"Reset Content",
        206: b"Partial Content",
        207: b"Multi-Status",
        208: b"Already Reported",
        226: b"IM Used",
        300: b"Multiple Choices",
        301: b"Moved Permanently",
        302: b"Found",
        303: b"See Other",
        304: b"Not Modified",
        305: b"Use Proxy",
        307: b"Temporary Redirect",
        308: b"Permanent Redirect",
        400: b"Bad Request",
        401: b"Unauthorized",
        402: b"Payment Required",
        403: b"Forbidden",
        404: b"Not Found",
        405: b"Method Not Allowed",
        406: b"Not Acceptable",
        407: b"Proxy Authentication Required",
        408: b"Request Timeout",
        409: b"Conflict",
        410: b"Gone",
        411: b"Length Required",
        412: b"Precondition Failed",
        413: b"Request Entity Too Large",
        414: b"Request-URI Too Long",
        415: b"Unsupported Media Type",
        416: b"Requested Range Not Satisfiable",
        417: b"Expectation Failed",
        418: b"I'm a teapot",
        422: b"Unprocessable Entity",
        423: b"Locked",
        424: b"Failed Dependency",
        426: b"Upgrade Required",
        428: b"Precondition Required",
        429: b"Too Many Requests",
        431: b"Request Header Fields Too Large",
        451: b"Unavailable For Legal Reasons",
        500: b"Internal Server Error",
        501: b"Not Implemented",
        502: b"Bad Gateway",
        503: b"Service Unavailable",
        504: b"Gateway Timeout",
        505: b"HTTP Version Not Supported",
        506: b"Variant Also Negotiates",
        507: b"Insufficient Storage",
        508: b"Loop Detected",
        510: b"Not Extended",
        511: b"Network Authentication Required",
    }
    bool_1 = module_0.has_message_body(bool_0)
    assert bool_1 is True
    var_0 = module_0.has_message_body(bool_0)
    assert var_0 is True
    var_1 = var_0.__repr__()
    assert var_1 == "True"
    default_0 = module_0.Default()
    str_0 = default_0.__str__()
    assert str_0 == "<Default>"
    var_2 = var_0.__repr__()
    assert var_2 == "True"

import pytest
from sanic.router import Router
from sanic.exceptions import MethodNotAllowed, NotFound, SanicException
from sanic_routing.route import Route
@pytest.fixture
def router():
    return Router()
@pytest.fixture
def handler():
    async def sample_handler(request):
        return True
    return sample_handler
def test_add_route_with_host(router, handler):
    route = router.add("/test", ["GET"], handler, host="example.com")
    assert route.extra.hosts == ["example.com"]
def test_method_not_allowed(router, handler):
    router.add("/test", ["GET"], handler)
    router.finalize()
    with pytest.raises(MethodNotAllowed):
        router.get("/test", "POST", None)
def test_multiple_hosts(router, handler):
    routes = router.add(
        "/test",
        ["GET"],
        handler,
        host=["example.com", "api.example.com"]
    )
    assert len(routes) == 2
    assert isinstance(routes, list)
def test_find_route_by_view_name(router, handler):
    route = router.add("/test", ["GET"], handler, name="test_route")
    router.finalize()
    found_route = router.find_route_by_view_name("test_route")
    assert found_route == route
def test_normalize_uri_with_type_hints(router):
    async def handler(request, user_id: int, name: str):
        return True
    normalized = router._normalize("/user/<user_id>/name/<name>", handler)
    assert normalized == "/user/<user_id:int>/name/<name:str>"
def test_invalid_parameter_names(router, handler):
    router.add("/test/<__invalid>", ["GET"], handler)
    with pytest.raises(SanicException):
        router.finalize()
def test_router_properties(router, handler):
    # Add various types of routes
    router.add("/static", ["GET"], handler)
    router.add("/dynamic/<param>", ["GET"], handler)
    router.add("/regex/<param:[0-9]{4}>", ["GET"], handler)
    router.finalize()
    assert len(router.routes_static) == 1
    assert len(router.routes_dynamic) == 1
    assert len(router.routes_regex) == 1
    assert len(router.routes_all) == 3
def test_route_overwrite(router, handler):
    # First route
    router.add("/test", ["GET"], handler, name="test_route")
    # Overwrite with new route
    new_route = router.add("/test", ["GET"], handler, name="test_route", overwrite=True)
    router.finalize()
    found_route = router.find_route_by_view_name("test_route")
    assert found_route == new_route
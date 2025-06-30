import pytest
from unittest.mock import MagicMock, patch
from sanic.exceptions import SanicException, NotFound, MethodNotAllowed
from router import Router, Route, RouteHandler, HTTP_METHODS


# Test suite for Router

@pytest.fixture
def router():
    return Router()

@pytest.fixture
def mock_route():
    return MagicMock(Route)

@pytest.fixture
def mock_handler():
    return MagicMock(RouteHandler)


# Test suite for the get method
def test_get_route(router, mock_route):
    path = "/test/route"
    method = "GET"
    host = None

    # Mock the resolve method to return a mock route
    router.resolve = MagicMock(return_value=(mock_route, mock_handler, {}))
    route, handler, match_info = router.get(path, method, host)

    # Ensure the route is returned correctly
    assert route == mock_route
    assert handler == mock_handler
    assert match_info == {}


# Test suite for routes_static property
def test_routes_static(router, mock_route):
    router.static_routes = {("static",): mock_route}
    route_dict = router.routes_static

    assert isinstance(route_dict, dict)
    assert mock_route in route_dict.values()


# Test suite for routes_dynamic property
def test_routes_dynamic(router, mock_route):
    router.dynamic_routes = {("dynamic",): mock_route}
    route_dict = router.routes_dynamic

    assert isinstance(route_dict, dict)
    assert mock_route in route_dict.values()


# Test suite for routes_regex property
def test_routes_regex(router, mock_route):
    router.regex_routes = {("regex",): mock_route}
    route_dict = router.routes_regex

    assert isinstance(route_dict, dict)
    assert mock_route in route_dict.values()



# Test suite for _normalize method (helper for routes)
def test_normalize_uri(router, mock_handler):
    uri = "/test/<param:int>"
    handler = mock_handler

    # Normalize the route URI and ensure that the parameter is handled correctly
    normalized_uri = router._normalize(uri, handler)
    assert normalized_uri == "/test/<param:int>"


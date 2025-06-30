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
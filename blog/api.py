from ninja import NinjaAPI, Schema


api = NinjaAPI()


class HelloSchema(Schema):
    name: str = "World"


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # Unauthenticated users don't have the following fields, so provide defaults.
    email: str = None
    first_name: str = None
    last_name: str = None


class Error(Schema):
    message: str


@api.get("/me", response=UserSchema)
def me(request):
    return request.user


@api.get("/me", response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Du bist nicht authentifiziert!"}
    return request.user


@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"


@api.get("/math/{a}und{b}")
def math(request, a: int, b: int):
    return f"Addition: {a + b}  Multiplication: {a * b}"
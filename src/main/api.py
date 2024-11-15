from ninja  import NinjaAPI,Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController
api=NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController )
api.add_router("/waitlist/","waitlists.api.router")


class UserSchema(Schema): 
    username:str
    is_authenticated:bool
    email:str=None


@api.get("/hello")
def hello(request):
    print(request)
    return {"Message":"hello world"}


@api.get("/me",response=UserSchema,auth=JWTAuth())
def me(request):
    print("pavi",request.user)
    return request.user   
from api.model.base import BaseResponse


class Message(BaseResponse):
    detail: str = "Object deleted successfully"

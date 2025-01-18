from sanic import Request, json
from sanic.views import HTTPMethodView

from api.decorators.require_login import require_login
from api.models.internal.jwt_data import JWT_Data
from api.utils.json_loader import load_form_data


class FormsRoot(HTTPMethodView):
    @require_login()
    async def get(self, request: Request, jwt_data: JWT_Data, slug: str):
        try:
            data = load_form_data(slug)
            return json(data)
        except FileNotFoundError:
            return json(
                {
                    "error": "Not Found",
                    "message": "The form template for the provided slug could not be found.",
                },
                404,
            )
        except Exception as e:
            return json({"error": "Internal Server Error", "message": str(e)}, 500)

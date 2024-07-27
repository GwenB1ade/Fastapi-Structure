from starlette_admin.contrib.sqla import Admin, ModelView
from database import engine

from app.auth.models import UserModel

admin = Admin(engine)

admin.add_view(
    ModelView(UserModel)
)
from src.api.factory import create_app
from src.config import settings
import uvicorn

app = create_app()


def main():
    uvicorn.run(
        "main:app",
        reload=True,
        host=settings.API_HOST,
        port=settings.API_PORT,
        use_colors=True,
    )


if __name__ == "__main__":
    main()

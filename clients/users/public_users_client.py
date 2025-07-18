import allure
from httpx import Response

from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.public_http_buider import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.routes import APIRoutes


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/user
    """

    @allure.step("Create user")
    @tracker.track_coverage_httpx(APIRoutes.USERS)
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с login, password
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.REGISTRATION, json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())

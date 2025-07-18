import allure
from httpx import Response

from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserPasswordRequestSchema
from tools.routes import APIRoutes


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/user
    """

    @allure.step("Get user")
    @tracker.track_coverage_httpx(f"{APIRoutes.USER}")
    def get_user_api(self) -> Response:
        """
         Метод получение информации о пользователе по токену

        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get(f"{APIRoutes.USER}")

    @allure.step("Get users")
    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}")
    def get_users_api(self) -> Response:
        """
         Метод получения логинов последних 100 зарегистрированных пользователей

        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get(f"{APIRoutes.USERS}")

    @allure.step("Update user")
    @tracker.track_coverage_httpx(f"{APIRoutes.USER}")
    def update_user_password_api(self, request: UpdateUserPasswordRequestSchema) -> Response:
        """
         Метод обновления пароля у пользователя

        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.put(f"{APIRoutes.USER}", json=request.model_dump(by_alias=True))


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))

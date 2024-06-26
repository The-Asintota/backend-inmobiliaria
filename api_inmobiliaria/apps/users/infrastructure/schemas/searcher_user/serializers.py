from apps.users.domain.constants import SearcherUser
from drf_spectacular.utils import (
    extend_schema_serializer,
    OpenApiExample,
)


SearcherUserRegisterSerializerSchema = extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="data_valid",
            summary="Register a new user with role searcheruser.",
            description=f"A valid user registration data. The following validations will be applied:\n- **full_name:** This field is required, must not exceed {SearcherUser.FULL_NAME_MAX_LENGTH.value} characters and must contain letters and spaces.\n- **email:** This field is required and must not exceed {SearcherUser.EMAIL_MAX_LENGTH.value} characters, must follow standard email format, and must not be in use.\n- **password:** This field is required and should be between {SearcherUser.PASSWORD_MIN_LENGTH.value} and {SearcherUser.PASSWORD_MAX_LENGTH.value} characters. It should not be a common password or contain only numbers. \n- **confirm_password:** This field is required and should match the password field.",
            value={
                "full_name": "Nombre Apellido",
                "email": "user1@email.com",
                "password": "contraseña1234",
                "confirm_password": "contraseña1234",
            },
            request_only=True,
        ),
    ],
)

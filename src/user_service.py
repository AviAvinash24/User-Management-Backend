import uuid

# In-memory user storage
_USERS = []


def create_user(name: str, email: str) -> dict:
    """
    Create a new user after validating input.
    """
    _validate_user_input(name, email)

    user = {
        "id": str(uuid.uuid4()),
        "name": name.strip(),
        "email": email.strip().lower(),
    }

    _USERS.append(user)
    return user


def get_all_users() -> list:
    """
    Return all created users.
    """
    return list(_USERS)


def _validate_user_input(name: str, email: str) -> None:
    if not name or not name.strip():
        raise ValueError("User name is required")

    if not email or not email.strip():
        raise ValueError("User email is required")

    if _email_exists(email):
        raise ValueError("User with this email already exists")


def _email_exists(email: str) -> bool:
    return any(user["email"] == email.strip().lower() for user in _USERS)
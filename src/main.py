from user_service import create_user, get_all_users


def main():
    try:
        create_user("Avi", "avi@example.com")
        create_user("Test User", "test@example.com")

        users = get_all_users()
        print(users)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
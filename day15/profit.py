def create_profile(**kwargs: object) -> None:
    """Print profile details."""
    for key, value in kwargs.items():
        print(f"{key.title()}: {value}")


create_profile(
    name="Manisha",
    city="Bangalore",
    skill="Python",
    role="Software Intern"
)
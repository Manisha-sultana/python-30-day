def average(*args: float) -> float:
    """Calculate the average of given numbers."""
    if not args:
        return 0.0
    return sum(args) / len(args)


print(average(10, 20, 30))
print(average(5, 10, 15, 20))
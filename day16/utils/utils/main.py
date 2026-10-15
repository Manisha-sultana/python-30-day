try:
    from .math_utils import add, multiply
except ImportError:
    try:
        from utils.utils.math_utils import add, multiply
    except ImportError:
        try:
            from day16.utils.utils.math_utils import add, multiply
        except ImportError:
            from math_utils import add, multiply


def main():
    print("Addition:", add(10, 5))
    print("Multiplication:", multiply(10, 5))


if __name__ == "__main__":
    main()
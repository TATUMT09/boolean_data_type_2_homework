def main(number):
    """
    Check a "number" is both positive and even
    Args:
        number: int
    Returns:
        bool
    """
    # Write your code here
    return number%2==0 , number>=0
print(main(5))
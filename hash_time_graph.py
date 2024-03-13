import hashlib
from timeit import Timer
from hash_time_graph import hash_time_graph

DEFAULT_TEXT_SIZES = [10, 100, 1000, 10000]

def hash_time(text_sizes: list = DEFAULT_TEXT_SIZES) -> dict:
    """
        Method returing time of hashing operation on texts of given lengths.

        Parameters:
        ----------------------------
            text_sizes (list) -> list of text sizes for hashing operation
        
        Returns:
        ----------------------------
            dict:
                Key (int) -> size of hashed text

                Value (float) -> time of hashing
    """
    time_results = []
    for size in text_sizes:
        message = "x" * int(size)
        generate_hash = lambda message=message: hashlib.sha256(message.encode()).hexdigest()
        t = Timer(generate_hash)
        time_results.append(t.timeit(number=1000))

    return {key: value for key, value in zip(text_sizes, time_results)}

import hashlib
from datetime import datetime


class HashText:
    DEFAULT_HASH_LENGTH = 16

    @staticmethod
    def hash_text(text: str, hash_length: int = DEFAULT_HASH_LENGTH) -> dict:
        """
            Method returning the hash values of the given text computed using every algorithm available in hashlib.

            Parameters:
            ----------------------------
                text str -> The text to be hashed.

                hash_length (int, optional) -> The hash length required for SHAKE-128 and SHAKE-256 algorithms.

            Returns:
            ----------------------------
                dict:
                    Key (str) -> name of the hashing algorithm.
                    Value (tuple) -> tuple containing: (Byte hash value, Hexadecimal hash value, Hash tim,)
        """
        result = {}
        for algorithm in hashlib.algorithms_available:
            h = hashlib.new(algorithm)
            h.update(text.encode())
            start_time = datetime.now()
            try:
                byte_hash = h.digest()
                hex_hash = h.hexdigest()
            except TypeError:
                byte_hash = h.digest(hash_length)
                hex_hash = h.hexdigest(hash_length)
            elapsed_time = datetime.now() - start_time
            result[algorithm] = (byte_hash, hex_hash, elapsed_time)
        return result


    @staticmethod
    def hash_input():
        """
            Method hashing user input text using every algorithm available in hashlib.
            Prompts the user to enter text to be hashed and optionally specify the hash length.
        """
        text = input('Enter text to hash:\n')
        length = input("Enter hash length (optional, leave empty to skip')")
        if length:
            results = HashText.hash_text(text=text, hash_length=int(length))
        else:
            results = HashText.hash_text(text=text)

        for algorithm, data in results.items():
            print(f"\nAlgorithm: {algorithm}\nByte Hash: {data[0]}\nHexadecimal Hash: {data[1]}\nElapsed Time: {data[2]}\n")


if __name__ == "__main__":
    pass

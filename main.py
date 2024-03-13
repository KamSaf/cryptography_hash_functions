import hashlib
from datetime import datetime


class Hash:
    # Ubuntu 22.04.4 LTS (Jammy Jellyfish) (accessed on: 13.03.2024)
    UBUNTU_DESKTOP_HASH = "071d5a534c1a2d61d64c6599c47c992c778e08b054daecc2540d57929e4ab1fd"
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
            results = Hash.hash_text(text=text, hash_length=int(length))
        else:
            results = Hash.hash_text(text=text)

        for algorithm, data in results.items():
            print(f"\nAlgorithm: {algorithm}\nByte Hash: {data[0]}\nHexadecimal Hash: {data[1]}\nElapsed Time: {data[2]}\n")


    @staticmethod
    def file_hash(file_path: str) -> str:
        """
            Method returning hash of a file using the sha256 algorithm.

            Parameters:
            ----------------------------
                file_path (str) -> path to file to be hashed

            Returns:
            ----------------------------
                str -> sha256 hash of a given file
        """
        with open(file=file_path, mode='rb') as file:
            digest = hashlib.file_digest(file, "sha256")
        return digest.hexdigest()


    @staticmethod
    def check_ubuntu_hash(file_path: str, ubuntu_hash: str = UBUNTU_DESKTOP_HASH) -> bool:
        """
            Method checking if hash of ubuntu file is valid.

            Parameters:
            ----------------------------
                file_path (str) -> path to file to be hashed

                ubuntu_hash (str) -> valid hash of an ubuntu file

            Returns:
            ----------------------------
                bool -> True if file is valid, False if not
        """
        return Hash.file_hash(file_path=file_path) == ubuntu_hash


if __name__ == "__main__":
    pass

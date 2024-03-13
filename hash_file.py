import hashlib


class HashFiles:
    # Ubuntu 22.04.4 LTS (Jammy Jellyfish) (accessed on: 13.03.2024)
    UBUNTU_DESKTOP_HASH = "071d5a534c1a2d61d64c6599c47c992c778e08b054daecc2540d57929e4ab1fd"

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
        return HashFiles.file_hash(file_path=file_path) == ubuntu_hash


if __name__ == "__main__":
    pass

from hash_file import HashFile as hash
import hashlib
import os


class TestHashFile:

    def test_hash_file(self):
        TEST_FILE_HASH = "44746a095378b05ef6fe14c4ec2f6ce0e892ad616d7193a0ab362caf813e4a54"
        TEST_FILE_CONTENT = "this is testing content"
        TEST_FILE_PATH = "tests/test_file.txt"
        open(TEST_FILE_PATH, "w").write(TEST_FILE_CONTENT)
        func_output = hash.hash_file(file_path=TEST_FILE_PATH)
        os.remove(TEST_FILE_PATH)
        assert func_output == TEST_FILE_HASH

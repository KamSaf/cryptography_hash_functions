from datetime import timedelta
from hash_text import HashText as hash
import hashlib


class TestHashText:

    def test_hash_text(self):
        TEXT = b'this is testing text'
        AVAIBLE_ALGORITHMS = hashlib.algorithms_available
        DEFAULT_HASH_LENGTH = 16
        func_result = hash.hash_text(TEXT)
        assert isinstance(func_result, dict)
        assert len(func_result) == len(AVAIBLE_ALGORITHMS)

        for algorithm, data in func_result.items():
            h = hashlib.new(algorithm)
            h.update(TEXT)

            assert algorithm in AVAIBLE_ALGORITHMS
            assert isinstance(data, tuple)
            assert len(data) == 3
            if algorithm in ('shake_128', 'shake_256'):
                assert data[0] == h.digest(DEFAULT_HASH_LENGTH)
                assert data[1] == h.hexdigest(DEFAULT_HASH_LENGTH)
            else:
                assert data[0] == h.digest()
                assert data[1] == h.hexdigest()
            assert isinstance(data[2], timedelta)

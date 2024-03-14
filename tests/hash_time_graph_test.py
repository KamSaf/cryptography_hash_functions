from hash_time_graph import HashTimeGraph as hash
from os import listdir, mkdir, path
from shutil import rmtree


class TestHashText:

    def test__generate_hash(self):
        TEST_TEXT = "this is testing text"
        TEST_TEST_HASH = "0c0f74e463cf9577ee54e1e199e7693f5aad3059b0cb3e94fa38151bfd821c7c"
        assert TEST_TEST_HASH == hash._HashTimeGraph__generate_hash(text=TEST_TEXT)

    def test_hash_time_default_sizes(self):
        function_result = hash.hash_time()
        assert list(function_result.keys()) == hash.DEFAULT_TEXT_SIZES
        for item in function_result.values():
            assert isinstance(item, float)

    def test_hash_time(self):
        TEST_TEXT_SIZES = [20, 200, 2000, 20000]
        function_result = hash.hash_time(text_sizes=TEST_TEXT_SIZES)
        assert list(function_result.keys()) == TEST_TEXT_SIZES
        for item in function_result.values():
            assert isinstance(item, float)

    def test_hash_time_graph(self):
        TEST_GRAPH_FILE_PATH = "tests/test_graphs/"
        if not path.exists(TEST_GRAPH_FILE_PATH):
            mkdir(TEST_GRAPH_FILE_PATH)
        hash.hash_time_graph(hash.hash_time(), as_image=True, out_path=TEST_GRAPH_FILE_PATH)
        for file_name in listdir(TEST_GRAPH_FILE_PATH + 'graphs/'):
            file_exists = file_name.startswith('graph_') and file_name.endswith('.png')
        rmtree(TEST_GRAPH_FILE_PATH)
        assert file_exists is True

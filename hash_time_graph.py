import hashlib
import plotly.express as px
import os
from datetime import datetime
from timeit import Timer


class HashTimeGraph:
    DEFAULT_TEXT_SIZES = [10, 100, 1000, 10000]

    @staticmethod
    def __generate_hash(text: str) -> str:
        """
            Method returning hash of a text using the sha256 algorithm.

            Parameters:
            ----------------------------
                text (str) -> text to be hashed

            Returns:
            ----------------------------
                str -> sha256 hash of a given text
        """
        return hashlib.sha256(text.encode()).hexdigest()

    @staticmethod
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
            text = "x" * int(size)
            t = Timer(lambda text=text: HashTimeGraph.__generate_hash(text=text))
            time_results.append(t.timeit(number=1000))
        return {key: value for key, value in zip(text_sizes, time_results)}

    @staticmethod
    def hash_time_graph(hash_time_results: dict, as_image: bool = False, out_path: str = None):
        """
            Method creating graph for given time results of hashing texts.

            Parameters:
            ----------------------------
                hash_time_results (dict):
                    Key (int) -> size of hashed text

                    Value (float) -> time of hashing

                as_image (bool) - flag for defining whether the graph should be rendered or outputted to an image file

                out_path (str) - path where images/ directory containing graphs will be created
        """
        fig = px.bar(x=hash_time_results.keys(), y=hash_time_results.values(), title='Hashing time of sha256 algorithm:')
        fig.update_xaxes(type='category', title='Message length').update_yaxes(title='Execution time')

        if as_image:
            path = str(out_path) + ("graphs/") if out_path else "graphs/"
            if not os.path.exists(path):
                os.mkdir(path)
            fig.write_image(f"{path}/graph_{datetime.now()}.png")
        else:
            fig.show()


if __name__ == "__main__":
    pass

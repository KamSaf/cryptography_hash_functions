import hashlib
import plotly.express as px
import os
from datetime import datetime
from timeit import Timer
from hash_time_graph import hash_time_graph

class HashTimeGraph:
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
            print(path)
            if not os.path.exists(path):
                os.mkdir(path)
            fig.write_image(f"{path}/graph_{datetime.now()}.png")
        else:
            fig.show()
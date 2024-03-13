import plotly.express as px
import os
from datetime import datetime


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














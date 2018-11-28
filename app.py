#!/usr/bin/env python3

import sys
from typing import Dict, List

import flask
import flask_restful

from cluster.cluster import KMeansClustering
from cluster.blog import parse_blogs

app = flask.Flask(__name__)
api = flask_restful.Api(app)


class KMeansREST(flask_restful.Resource):
    @staticmethod
    def get(iterations: int) -> Dict[int, List[str]]:
        blogs = parse_blogs("data/blogdata.txt")
        k_means_clustering = KMeansClustering(blogs, iterations)

        result = {}  # type: Dict[int, List[str]]
        for centroid in k_means_clustering.centroids:
            result[centroid.number] = []
            for blog in centroid.blogs:
                result[centroid.number].append(blog.name)
        return result


api.add_resource(KMeansREST, "/api/k-means-clustering/<int:iterations>")


@app.route("/", defaults={"filename": None})
@app.route("/<filename>")
def ui(filename: str) -> flask.Response:
    if not filename:
        filename = "index.html"
    return flask.send_from_directory("ui", filename, cache_timeout=1)


def main() -> int:
    app.run(host=len(sys.argv) > 1 and sys.argv[1] or "127.0.0.1")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3

import sys
from typing import Dict, List, Optional

import flask
import flask_restful

from cluster.k_means import KMeansClustering
from cluster.hierarchical import HierarchicalClustering, Cluster
from cluster.blog import parse_blogs

app = flask.Flask(__name__)
api = flask_restful.Api(app)
blogs = parse_blogs("data/blogdata.txt")
k_means_clustering = KMeansClustering(blogs)
hierarchical_clustering = HierarchicalClustering(blogs)


class KMeansREST(flask_restful.Resource):
    @staticmethod
    def get(iterations: int) -> Dict[int, List[str]]:
        result = {}  # type: Dict[int, List[str]]
        for centroid in k_means_clustering.compute(iterations):
            result[centroid.number] = []
            for blog in centroid.blogs:
                result[centroid.number].append(blog.name)
        return result


api.add_resource(KMeansREST, "/api/k-means-clustering/<int:iterations>")


class HierarchicalREST(flask_restful.Resource):
    def get(self) -> Dict[int, List[str]]:
        result = {}  # type: Dict
        root = hierarchical_clustering.compute()
        self._to_dict(root, result)
        return result

    def _to_dict(self,
                 cluster: Optional[Cluster],
                 result: Dict,
                 direction: str="root") -> None:
        if cluster:
            result[direction] = {
                "blog": cluster.blog and cluster.blog.name or ""
            }
            self._to_dict(cluster.left, result[direction], "left")
            self._to_dict(cluster.right, result[direction], "right")


api.add_resource(HierarchicalREST, "/api/hierarchical-clustering")


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

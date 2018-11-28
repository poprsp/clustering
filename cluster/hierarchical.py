#!/usr/bin/env python3

import sys
from typing import List, Optional

from .blog import Blog, Word
from .distance import pearson


class Cluster:
    def __init__(self) -> None:
        self._left = None  # type: Optional[Cluster]
        self._right = None  # type: Optional[Cluster]
        self._parent = None  # type: Optional[Cluster]
        self._blog = None  # type: Optional[Blog]
        self._distance = 0.0

    @property
    def left(self) -> Optional["Cluster"]:
        return self._left

    @left.setter
    def left(self, value: "Cluster") -> None:
        self._left = value

    @property
    def right(self) -> Optional["Cluster"]:
        return self._right

    @right.setter
    def right(self, value: "Cluster") -> None:
        self._right = value

    @property
    def parent(self) -> Optional["Cluster"]:
        return self._parent

    @parent.setter
    def parent(self, value: "Cluster") -> None:
        self._parent = value

    @property
    def blog(self) -> Optional[Blog]:
        return self._blog

    @blog.setter
    def blog(self, value: Blog) -> None:
        self._blog = value

    @property
    def distance(self) -> float:
        return self._distance

    @distance.setter
    def distance(self, value: float) -> None:
        self._distance = value


class HierarchicalClustering:
    def __init__(self, blogs: List[Blog]) -> None:
        self._clusters = []  # type: List[Cluster]
        for blog in blogs:
            c = Cluster()
            c.blog = blog
            self._clusters.append(c)

    def compute(self) -> Cluster:
        """
        Compute a hierarchical cluster and return the root node.
        """
        self._iterate()
        return self._clusters[0]

    def _iterate(self) -> None:
        """
        Iterate over the clusters and merge the closest ones until there
        is only one element left in the list of clusters.
        """
        while len(self._clusters) > 1:
            closest = sys.float_info.max

            for c_a in self._clusters:
                for c_b in self._clusters:
                    if c_a == c_b:
                        continue
                    if not c_a.blog or not c_b.blog:
                        raise RuntimeError("blogs must be assigned")

                    distance = pearson(c_a.blog, c_b.blog)
                    if distance < closest:
                        closest = distance
                        a = c_a
                        b = c_b

            c = self._merge(a, b, closest)
            self._clusters.remove(a)
            self._clusters.remove(b)
            self._clusters.append(c)

    @staticmethod
    def _merge(a: Cluster, b: Cluster, distance: float) -> Cluster:
        """
        Merge two clusters.
        """
        if not a.blog or not b.blog:
            raise RuntimeError("blogs must be assigned")

        blog = Blog("")

        # Merge blog data by averaging word counts for each word
        for i in range(len(a.blog.words)):
            a_w = a.blog.words[i]
            b_w = b.blog.words[i]
            count = (a_w.count + b_w.count) / 2
            blog.add_word(Word(a_w.word, count))

        p = Cluster()
        p.left = a
        p.right = b
        p.blog = blog
        p.distance = distance

        a.parent = b.parent = p
        return p

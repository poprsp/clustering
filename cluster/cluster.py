#!/usr/bin/env python3

import random
import sys
from typing import Dict, List

from .distance import pearson
from .blog import Blog, Word


class Centroid(Blog):
    def __init__(self, number: int) -> None:
        super().__init__("")

        self._number = number
        self._blogs = []  # type: List[Blog]

    def remove_blogs(self) -> None:
        self._blogs = []

    def assign_blog(self, blog: Blog) -> None:
        self._blogs.append(blog)

    def swap_word(self, index: int, word: Word) -> None:
        self._words[index] = word

    @property
    def blogs(self) -> List[Blog]:
        return self._blogs

    @property
    def number(self) -> int:
        return self._number


class KMeansClustering:
    _cluster_count = 5

    def __init__(self, blogs: List[Blog], iteration_count: int) -> None:
        self._blogs = blogs
        self._iteration_count = iteration_count

        self._words = self._prepare_words()
        self._centroids = self._create_centroids()
        self._assign_blogs()
        self._centroids.sort(key=lambda c: c.number)

    @property
    def centroids(self) -> List[Centroid]:
        return self._centroids

    def _create_centroids(self) -> List[Centroid]:
        centroids = []
        for i in range(self._cluster_count):
            centroid = Centroid(i)
            for word, counts in self._words.items():
                count = random.randint(counts["min"], counts["max"])
                centroid.add_word(Word(word, count))
            centroids.append(centroid)
        return centroids

    def _assign_blogs(self) -> None:
        for i in range(self._iteration_count):
            # Clear previous assignments
            for centroid in self._centroids:
                centroid.remove_blogs()

            # Assign each blog to the closest centroid
            for blog in self._blogs:
                distance = sys.float_info.max
                for centroid in self._centroids:
                    new_distance = pearson(blog, centroid)
                    if new_distance < distance:
                        distance = new_distance
                        closest_centroid = centroid
                closest_centroid.assign_blog(blog)

            # Re-calculate the center for each centroid
            for centroid in self._centroids:
                for i in range(len(centroid.words)):
                    avg = 0.0
                    for blog in centroid.blogs:
                        avg += blog.words[i].count

                    if centroid.blogs:
                        avg /= len(centroid.blogs)

                    old_word = centroid.words[i]
                    centroid.swap_word(i, Word(old_word.word, avg))

    def _prepare_words(self) -> Dict[str, Dict[str, int]]:
        """
        Take the word list from the first blog and store every word
        alongside their min and max mentions.
        """
        words = {}
        for word in self._blogs[0].words:  # YOLO
            words[word.word] = {
                "min": self._min(word.word),
                "max": self._max(word.word)
            }
        return words

    def _min(self, w: str) -> int:
        """
        Calculate the min mentions of a given word in all blogs.
        """
        count = sys.float_info.max
        for blog in self._blogs:
            word = blog.find_word(w)
            if word.count < count:
                count = word.count
        return int(round(count))

    def _max(self, w: str) -> int:
        """
        Calculate the max mentions of a given word in all blogs.
        """
        count = 0.0
        for blog in self._blogs:
            word = blog.find_word(w)
            if word.count > count:
                count = word.count
        return int(round(count))

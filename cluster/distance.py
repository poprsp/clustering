#!/usr/bin/env python3

import math

from .blog import Blog


def pearson(a: Blog, b: Blog) -> float:
    """
    Calculate the pearson distance between two blogs.

    Args:
        a: The first blog
        b: The second blog

    Returns:
        float: The distance.
    """
    a_sum = a_sum_sq = b_sum = b_sum_sq = p_sum = 0.0
    n = 0

    for i in range(len(a.words)):
        a_c = a.words[i].count
        a_sum += a_c
        a_sum_sq += a_c**2

        b_c = b.words[i].count
        b_sum += b_c
        b_sum_sq += b_c**2

        p_sum += a_c * b_c
        n += 1

    if n:
        num = p_sum - (a_sum * b_sum / n)
        den = math.sqrt((a_sum_sq - a_sum**2 / n) * (b_sum_sq - b_sum**2 / n))
        if den:
            return num / den
    return 0.0

import numpy as np

def arc_chord_ratio(arc_length, chord_length):
    return arc_length / chord_length

def total_curvature(curvatures):
    return sum(curvatures)

def total_squared_curvature(curvatures, chord_lengths):
    return sum([(curv ** 2) / chord_len for curv, chord_len in zip(curvatures, chord_lengths)])

def tortuosity_index(arc_lengths, chord_lengths):
    return sum(arc_lengths) / sum(chord_lengths)

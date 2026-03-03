# Import numpy to perform vector math operations
import numpy as np


# Computes cosine similarity between two vectors.
#
# Cosine similarity measures how aligned two vectors are in direction.
# It does NOT measure distance.
# It measures the cosine of the angle between them.
#
# If vectors point in the same direction → similarity ≈ 1
# If vectors are unrelated → similarity ≈ 0
# If vectors point in opposite directions → similarity ≈ -1
#
# In embeddings:
# Similar meaning → vectors point in similar directions.
def cosine_similarity(vec1, vec2):

    # Convert lists into numpy arrays for mathematical operations
    np_vec1 = np.array(vec1)
    np_vec2 = np.array(vec2)

    # Dot product measures directional alignment.
    # It multiplies corresponding elements and sums them.
    #
    # If vectors align strongly → dot product is large.
    dot_product = np.dot(np_vec1, np_vec2)

    # Compute magnitudes (lengths) of each vector.
    # Magnitude = sqrt(sum of squares of elements).
    #
    # This represents how long the vector is in vector space.
    mag1 = np.linalg.norm(np_vec1)
    mag2 = np.linalg.norm(np_vec2)

    # Cosine similarity formula:
    #
    #           dot_product
    # --------------------------------
    #   (magnitude of vec1 * magnitude of vec2)
    #
    # Dividing by magnitudes removes length influence
    # and keeps only directional similarity.
    #Meaning if two vectors are in the same direction they are similar, 
    #we dont want the lenht of the vector or text to assume its not similar when they are
    score = dot_product / (mag1 * mag2)

    return score
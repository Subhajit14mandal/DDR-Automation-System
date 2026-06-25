
from difflib import SequenceMatcher


def similarity(a, b):

    return SequenceMatcher(
        None,
        a.lower(),
        b.lower()
    ).ratio()


def remove_duplicates(
        observations,
        threshold=0.85):

    unique = []

    for obs in observations:

        duplicate = False

        for existing in unique:

            if similarity(
                    obs["observation"],
                    existing["observation"]
            ) > threshold:

                duplicate = True
                break

        if not duplicate:
            unique.append(obs)

    return unique

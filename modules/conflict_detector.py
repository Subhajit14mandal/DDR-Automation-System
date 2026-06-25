
NEGATIVE_WORDS = [
    "no",
    "not",
    "none",
    "without",
    "absent"
]


def is_negative(text):

    text = text.lower()

    return any(
        word in text
        for word in NEGATIVE_WORDS
    )


def detect_conflicts(
        inspection,
        thermal):

    conflicts = []

    for i in inspection:

        for t in thermal:

            if (
                i["area"] == t["area"]
                and
                is_negative(
                    i["observation"]
                )
                !=
                is_negative(
                    t["observation"]
                )
            ):

                conflicts.append({
                    "area": i["area"],
                    "inspection":
                        i["observation"],
                    "thermal":
                        t["observation"]
                })

    return conflicts

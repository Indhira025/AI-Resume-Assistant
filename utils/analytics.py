import json
from pathlib import Path

from config.logging_config import setup_logger

logger = setup_logger()

FILE = Path("outputs/analytics.json")


def _default():
    return {
        "ats_scores": [],
        "resume_rewrites": 0,
        "jd_matches": 0,
        "cover_letters": 0,
        "interviews": 0
    }


def _load():

    data = _default()

    if FILE.exists():

        try:

            with open(FILE, "r", encoding="utf-8") as f:

                old = json.load(f)

                if isinstance(old, dict):
                    data.update(old)

        except Exception:

            logger.exception("Unable to read analytics file.")

    return data


def _save(data):

    FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


# ---------------- ATS ----------------

def add_ats_score(score):

    data = _load()

    data["ats_scores"].append(score)

    _save(data)

# ---------------- JD Matching ----------------

def increase_jd_match():

    data = _load()

    data["jd_matches"] = data.get(
        "jd_matches",
        0
    ) + 1

    _save(data)

# ---------------- Resume Rewrite ----------------

def increase_resume_rewrite():

    data = _load()

    data["resume_rewrites"] = data.get(
        "resume_rewrites",
        0
    ) + 1

    _save(data)

# ---------------- Cover Letter ----------------

def increase_cover_letter():

    data = _load()

    data["cover_letters"] = data.get(
        "cover_letters",
        0
    ) + 1

    _save(data)


# ---------------- Interview ----------------

def increase_interview():

    data = _load()

    data["interviews"] = data.get(
        "interviews",
        0
    ) + 1

    _save(data)


# ---------------- Dashboard ----------------

def get_statistics():

    data = _load()

    scores = data.get(
        "ats_scores",
        []
    )

    avg = round(
        sum(scores) / len(scores),
        2
    ) if scores else 0

    return {

        "average_score": avg,

        "total_ats": len(scores),

        "resume_rewrites": data.get(
            "resume_rewrites",
            0
        ),

        "jd_matches": data.get(
            "jd_matches",
            0
        ),

        "cover_letters": data.get(
            "cover_letters",
            0
        ),

        "interviews": data.get(
            "interviews",
            0
        )
    }
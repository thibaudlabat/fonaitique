import argparse
import multiprocessing
import re
import pysrt
import eng_to_ipa as ipa
import tqdm


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def _convert_one(task: tuple[int, str, bool]) -> tuple[int, str]:
    """Worker: (index, raw_text, show_original) -> (index, new_text). Top-level for pickling."""
    idx, raw_text, show_original = task
    original = strip_html(raw_text)
    ipa_text = ipa.convert(original)
    if show_original:
        new_text = ipa_text + '\n<font size="20px">' + original.replace("\n", "") + '</font>'
    else:
        new_text = ipa_text
    return (idx, new_text)


def main():
    p = argparse.ArgumentParser(description="Convert SRT subtitles to IPA.")
    p.add_argument("input", help="Input SRT file")
    p.add_argument("output", help="Output SRT file")
    p.add_argument(
        "--show-original",
        action="store_true",
        help="Add original (HTML-stripped) English under each IPA line in small text",
    )
    args = p.parse_args()
    subs = pysrt.open(args.input)
    n_workers = min(len(subs), multiprocessing.cpu_count())
    tasks = [(i, sub.text, args.show_original) for i, sub in enumerate(subs)]
    chunksize = max(1, len(tasks) // (n_workers * 4))
    with multiprocessing.Pool(n_workers) as pool:
        results = list(tqdm.tqdm(
            pool.imap_unordered(_convert_one, tasks, chunksize=chunksize),
            total=len(tasks),
        ))
    for idx, new_text in sorted(results):
        subs[idx].text = new_text
    subs.save(args.output, encoding="utf-8")


if __name__ == "__main__":
    main()
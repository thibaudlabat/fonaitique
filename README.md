# Fonaitique

This project allows converting `.srt` subtitles from US English to its [International Phonetic Alphabet (IPA)](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) representation, using the [Carnegie-Mellon University Pronouncing Dictionary](https://en.wikipedia.org/wiki/CMU_Pronouncing_Dictionary).

## Usage

**Requirements:** 
- Python package [uv](https://github.com/astral-sh/uv).

**Run:**

```bash
uv run python ./main.py input.srt output.srt
```

**Optional arguments:**

| Argument           | Description                            |
|--------------------|----------------------------------------|
| `--show-original`  | Add original text under each IPA line. |

### Example Input

```
1
00:00:11,625 --> 00:00:13,540
The International Phonetic Alphabet (IPA) is an alphabetic system of phonetic notation.
```

### Example Output

```
1
00:00:11,625 --> 00:00:13,540
ðə ˌɪnərˈnæʃənɑl fəˈnɛtɪk ˈælfəˌbɛt (ipa*) ɪz ən ˌælfəˈbɛtɪk ˈsɪstəm əv fəˈnɛtɪk noʊˈteɪʃən.
```

## Contributions

Feel free to open GitHub issues for questions, bugs and feature ideas. Pull Requests are also welcome.

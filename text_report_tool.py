import re
from collections import Counter
from pathlib import Path


def read_text_file():
    path = input("Enter file path: ").strip()
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        print("File not found")
        return None, None
    try:
        text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = file_path.read_text(encoding="latin-1")
    return file_path, text


def clean_words(text):
    return re.findall(r"[a-zA-Z]+", text.lower())


def text_stats(text):
    words = clean_words(text)
    lines = text.splitlines()
    sentences = re.split(r"[.!?]+", text)
    sentence_count = len([s for s in sentences if s.strip()])
    word_count = len(words)
    unique_count = len(set(words))
    char_count = len(text)
    avg_word_len = (sum(len(w) for w in words) / word_count) if word_count else 0

    freq = Counter(words)
    top_words = freq.most_common(10)

    return {
        "lines": len(lines),
        "sentences": sentence_count,
        "words": word_count,
        "unique_words": unique_count,
        "characters": char_count,
        "avg_word_length": avg_word_len,
        "top_words": top_words,
    }


def show_report(path, report):
    print(f"\nReport for: {path}")
    print(f"Lines: {report['lines']}")
    print(f"Sentences: {report['sentences']}")
    print(f"Words: {report['words']}")
    print(f"Unique words: {report['unique_words']}")
    print(f"Characters: {report['characters']}")
    print(f"Average word length: {report['avg_word_length']:.2f}")
    print("Top words:")
    for word, count in report["top_words"]:
        print(f"{word}: {count}")


def export_report(path, report):
    out_name = input("Output report filename: ").strip()
    if not out_name:
        print("Filename cannot be empty")
        return
    lines = [
        f"Report for: {path}",
        f"Lines: {report['lines']}",
        f"Sentences: {report['sentences']}",
        f"Words: {report['words']}",
        f"Unique words: {report['unique_words']}",
        f"Characters: {report['characters']}",
        f"Average word length: {report['avg_word_length']:.2f}",
        "Top words:",
    ]
    for word, count in report["top_words"]:
        lines.append(f"{word}: {count}")
    Path(out_name).write_text("\n".join(lines), encoding="utf-8")
    print("Report exported")


def main():
    while True:
        path, text = read_text_file()
        if text is None:
            retry = input("Try another file? (y/n): ").strip().lower()
            if retry != "y":
                break
            continue

        report = text_stats(text)
        show_report(path, report)

        choice = input("Export report to file? (y/n): ").strip().lower()
        if choice == "y":
            export_report(path, report)

        again = input("Analyze another file? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()

"""
Stage 2 of the pipeline: splitting documents into chunks.

Milestone 3 replaces the starter's fixed-size chunking strategy with one
designed for the city_guides corpus.

The city guides are organized using Markdown section headings such as
"Getting there", "Eat and drink", and "When to go". Instead of cutting at a
fixed character count, split_documents keeps each labeled section together.
"""

from dataclasses import dataclass

import config

from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """

    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []

    for doc in documents:
        start = 0
        index = 0

        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()

            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1

            start += chunk_size - overlap

    return chunks


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split city guides using their Markdown section headings.

    Each ## section is kept together as one chunk instead of splitting at a
    fixed character count. This keeps related information together and avoids
    cutting sentences or words in half.
    """

    chunks: list[Chunk] = []

    for doc in documents:
        sections: list[str] = []
        current_section: list[str] = []

        for line in doc.text.splitlines():

            # A level-two Markdown heading begins a new topic.
            if line.startswith("## ") and current_section:
                section_text = "\n".join(current_section).strip()

                if section_text:
                    sections.append(section_text)

                current_section = []

            current_section.append(line)

        # Add the final section after reaching the end of the document.
        if current_section:
            section_text = "\n".join(current_section).strip()

            if section_text:
                sections.append(section_text)

        # Turn each section into a Chunk object.
        for index, section in enumerate(sections):
            chunks.append(
                Chunk(
                    text=section,
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""

    if not chunks:
        return "0 chunks"

    lengths = [len(c.text) for c in chunks]

    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
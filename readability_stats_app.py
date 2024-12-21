import re
import spacy
import textstat
## !python -m spacy download en_core_web_sm

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    return len(text)

def sentence_count(text):
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def paragraph_count(text):
    paragraphs = text.split('\n')
    return len([p for p in paragraphs if p.strip()])

def characters_per_word(text):
    words = text.split()
    total_characters = sum(len(word) for word in words)
    return total_characters / len(words) if words else 0

def words_per_sentence(text):
    words = word_count(text)
    sentences = sentence_count(text)
    return words / sentences if sentences else 0

def sentences_per_paragraph(text):
    sentences = sentence_count(text)
    paragraphs = paragraph_count(text)
    return sentences / paragraphs if paragraphs else 0


nlp = spacy.load("en_core_web_sm")

def passive_sentence_count(text):
    doc = nlp(text)
    passive_sentences = 0
    for sent in doc.sents:
        if any(token.dep_ == "auxpass" for token in sent):
            passive_sentences += 1
    return passive_sentences

def calculate_all_statistics(text):
    stats = {
        "Flesch Reading Ease": textstat.flesch_reading_ease(text),
        "Flesch-Kincaid Grade": textstat.flesch_kincaid_grade(text),
        "Gunning Fog Index": textstat.gunning_fog(text),
        "Dale-Chall Readability Score": textstat.dale_chall_readability_score(text),
        "Automated Readability Index": textstat.automated_readability_index(text),
        "SMOG Index": textstat.smog_index(text),
        "Reading Time (seconds)": textstat.reading_time(text, ms_per_char=14.69),
        "Characters": character_count(text),
        "Words": word_count(text),
        "Sentences": sentence_count(text),
        "Paragraphs": paragraph_count(text),
        "Words per Sentence": words_per_sentence(text),
        "Characters per Word": characters_per_word(text),
        "Sentences per Paragraph": sentences_per_paragraph(text),
        "Passive Sentences": passive_sentence_count(text),
    }
    return stats


import os

def process_brochures(folder_path, output_csv_path):
    docx_files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]
    all_stats = []

    for docx_file in docx_files:
        file_path = os.path.join(folder_path, docx_file)
        print(f"Processing {docx_file}...")

        text = read_docx(file_path)

        stats = calculate_all_statistics(text)
        stats['BrochureID'] = docx_file 

        all_stats.append(stats)

    write_stats_to_csv(all_stats, output_csv_path)

    print(f"Readability and additional statistics saved to {output_csv_path}")

if __name__ == "__main__":
    folder_path = r"folder_path\to\input_docx"
    output_csv_path = "results.csv"
    process_brochures(folder_path, output_csv_path)

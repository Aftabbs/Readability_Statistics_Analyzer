# Readability Statistics Analyzer

![image](https://github.com/user-attachments/assets/891f1884-1b73-4408-b6a7-512d8336c33b)



## Introduction

Readability is a critical aspect of any written document, as it determines how easily readers can comprehend the content. This project provides a comprehensive solution for analyzing the readability of documents using advanced Natural Language Processing (NLP) techniques and widely-used readability metrics.

The tool processes `.docx` files to calculate various readability statistics, such as word count, sentence count, Flesch Reading Ease, and many others. It also includes advanced insights like passive sentence detection using NLP.

---

## Objective

The primary objective of this project is to create a tool that:
- **Preprocesses documents**: Converts `.docx` files into plain text for readability analysis.
- **Calculates readability metrics**: Leverages established formulas to evaluate document readability.
- **Generates detailed statistics**: Provides advanced insights such as passive sentence counts and average characters per word.
- **Exports results**: Saves the statistics in a structured format (CSV) for further analysis.

---

## Features

1. **Multi-Metric Readability Analysis**:
   - Flesch Reading Ease
   - Flesch-Kincaid Grade
   - Gunning Fog Index
   - Dale-Chall Readability Score
   - SMOG Index
   - Automated Readability Index

2. **Text Statistics**:
   - Total Characters
   - Total Words
   - Total Sentences
   - Total Paragraphs
   - Words per Sentence
   - Characters per Word
   - Sentences per Paragraph

3. **Advanced NLP-Based Insights**:
   - Passive Sentence Count (using SpaCy).

4. **Batch Processing**:
   - Automatically processes multiple `.docx` files in a folder.

5. **Output**:
   - Saves all statistics in a CSV file for easy reporting and analysis.

---

## Libraries Used

- **re**: Regular expressions for text processing.
- **spacy**: Advanced NLP library for passive voice detection.
- **textstat**: Readability metrics computation.
- **os**: File management and folder traversal.
- **docx**: Reads `.docx` files to extract text.

---

## Workflow

1. **Input**: The tool takes a folder of `.docx` files as input.
2. **Text Extraction**: Reads and preprocesses the text from each file.
3. **Readability Metrics Calculation**: Computes multiple readability metrics and text statistics.
4. **NLP Analysis**: Uses SpaCy to identify passive sentences.
5. **Output**: Exports the results as a CSV file for reporting.

---

## Use Cases

1. **Content Optimization**: Evaluate the readability of marketing brochures, technical documents, or educational material.
2. **Regulatory Compliance**: Ensure that legal or healthcare documents meet readability standards.
3. **Academic Analysis**: Analyze the complexity of academic papers or essays.
4. **User-Friendly Content**: Tailor content for different audiences by improving readability scores.

---

## Advantages

1. **Comprehensive Metrics**: Provides a wide range of readability metrics and text statistics.
2. **Advanced NLP Integration**: Identifies passive sentences using SpaCy for better writing insights.
3. **Batch Processing**: Handles multiple documents simultaneously, saving time.
4. **Customizable and Extensible**: Easily integrate with additional tools or pipelines.

---

## Improvements and Future Enhancements

1. **Multi-Format File Processing**:
   - Add support for `.pdf`, `.txt`, and `.html` files.
   - Use libraries like `PyPDF2` or `pdfplumber` for PDF processing.

2. **LLM-Powered Analysis**:
   - Incorporate large language models (LLMs) to generate summaries or improve readability metrics.
   - Use APIs such as OpenAI’s GPT or Google Bard for context-aware readability analysis.

3. **User Interface**:
   - Create a web-based interface using Flask or Streamlit for user-friendly interaction.

4. **Real-Time Insights**:
   - Provide real-time feedback and suggestions for improving readability.

---

## Example Code Snippet

```python
import re
import spacy
import textstat
!python -m spacy download en_core_web_sm

def calculate_all_statistics(text):
    stats = {
        "Flesch Reading Ease": textstat.flesch_reading_ease(text),
        "Flesch-Kincaid Grade": textstat.flesch_kincaid_grade(text),
        "Gunning Fog Index": textstat.gunning_fog(text),
        "Dale-Chall Readability Score": textstat.dale_chall_readability_score(text),
        "Automated Readability Index": textstat.automated_readability_index(text),
        "SMOG Index": textstat.smog_index(text),
        "Reading Time (seconds)": textstat.reading_time(text, ms_per_char=14.69),
        "Passive Sentences": passive_sentence_count(text),
    }
    return stats
```
---
### **Important Notes**

- Ensure that all .docx files are well-formatted for accurate text extraction.
- For multi-format support, additional libraries will be required.
- To analyze larger documents or datasets, consider optimizing the text processing pipeline.
---

### **Conclusion**
This project provides an automated and scalable solution for evaluating the readability of documents. With the integration of advanced NLP techniques and comprehensive readability metrics, this tool is ideal for content creators, educators, and businesses looking to improve the accessibility and clarity of their documents.

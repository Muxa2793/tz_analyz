import docx
import re


def main():
    doc = docx.Document('Examples/ТЗ.docx')

    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)

    searching_term(fullText)


def searching_term(text):
    term_list = []
    for term in text:
        if re.search(r'срок*', term.lower()):
            term_list.append(term)

    index_list = []
    n = 0
    for garanted in term_list:
        if re.search(r'гарант*', garanted.lower()):
            index_list.append(n)
        n = n + 1
    for x in sorted(index_list, reverse=True):
        del term_list[x]
    print(term_list)


if __name__ == "__main__":
    main()

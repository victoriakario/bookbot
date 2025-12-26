from stats import get_num_words, get_letter_count, get_list_of_dictionaries
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  if len(sys.argv) < 2:
    print( "Usage: python3 main.py <path_to_book>" )
    sys.exit(1)
  report = "============ BOOKBOT ============\n"
  content = get_book_text(sys.argv[1])
  report += f"Analyzing book found at {sys.argv[1]}\n"
  num_words = get_num_words(content)
  report += "----------- Word Count ----------\n"
  report += f"Found {num_words} total words\n"
  count_of_letters = get_letter_count(content)
  report += "--------- Character Count -------\n"
  pretty_list = get_list_of_dictionaries(count_of_letters)

  for item in pretty_list:
    report += f"{item['char']}: {item['num']}\n"

  report += "============= END ===============\n"
  return report

print(main())



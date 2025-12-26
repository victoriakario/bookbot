def get_num_words(contents):
  return len(contents.split())

def get_letter_count(contents):
  letter_and_count = {}
  words = contents.split()
  for word in words:
    for letter in word:
      letter = letter.lower()
      if letter in letter_and_count:
        letter_and_count[letter] += 1
      else:
        letter_and_count[letter] = 1
  return letter_and_count

def sort_on(item):
    return item['num']

def get_list_of_dictionaries(dictionary):
  list_of_dictionaries = []
  for item in dictionary:
    count = dictionary[item]
    if item.isalpha():
      list_of_dictionaries.append({"char": item, "num": count})
  list_of_dictionaries.sort(key=sort_on, reverse=True)
  return list_of_dictionaries

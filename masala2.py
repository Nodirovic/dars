def pluralize(ls):
  return set(i + 's' * (ls.count(i) > 1) for i in ls)

lst = input('Enter the list of words:\n').split(',')
print(pluralize(lst))
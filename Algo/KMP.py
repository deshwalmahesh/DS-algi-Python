def KMP(text:str, query:str, find_all:bool = False)->list:
  '''
  Given a text string, find 1 or all occurance os the query string is present in the text: https://www.youtube.com/watch?v=4jY57Ehc14Y
  args:
    text: given text
    query: sub string we want to find
    find_all: Whether to find all the occurances of the text or just the first one
  out:
    first index encountered, indices of all the occurances or -1 if no occurance was found
  '''
  occurances = []
  text_len = len(text)
  query_len = len(query)
  lps_table = LPSTable(query,query_len)
  i = 0 # for text
  j = 0 # for query
  while i < text_len:
    if text[i] == query[j]:
      i += 1
      j += 1
    else: # in case of mismatch, go to the table, find what is length of the prefix that is a suffix "at THIS exact index" where mismatch happened
      if j==0: i+=1 # if the first character mismatches itself, just go to the next one in text
      else: j = lps_table[j-1]
    
    if j == query_len: # if we have matched successfully
      if not find_all: return i-j # return first occurance
      occurances.append(i-j)
      j = lps_table[j-1] # skip the first words which are suffix and prefix
  
  return occurances if occurances else -1



def LPSTable(string:str, N:int)->list:
  '''
  Genrerate LPS Table for KMP query string : https://www.youtube.com/watch?v=4jY57Ehc14Y
  args:
   string: string
   N: length of string
  '''
  length = 0 # length of longest "proper" prefix that is also a suffix
  table = [0]*N # at index 'i', what is the length of the longest prefict that is also a suffix. Basically holds value of length at every index
  i = 1
  while i < N:
    if string[i] == string[length]:
      table[i] = length+1 # because index starts from 0
      length+=1
      i+=1
    else:
      if length !=0: # Because we have already advanced the prefic pointer and there a partial match
        length = table[length-1]# It'll just that how much of the string we have already checked so we don't have to start from length=0
      
      else:
        table[i] = 0 # current max length at the pointer where nothing has matched as of now should be 0
        i += 1
  return table

# KMP("slim shady",'lim', True)

# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    i = 0
    url_list = []
    index_item = []
    l = len(index)
    if not l:
        url_list.append(url)
        index_item.append(keyword)
        index_item.append(url_list)
        index.append(index_item)
    while i < l:
        if index[i][0] == keyword:
            j = 0
            while j < len(index[i][1]):
                if index[i][1][j] == url:
                    return "same keyword and url!"
                j = j + 1
            index[i][1].append(url)
        else:
            url_list.append(url)
            index_item.append(keyword)
            index_item.append(url_list)
            index.append(index_item)
            i = i + 1
    return index
            






add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]



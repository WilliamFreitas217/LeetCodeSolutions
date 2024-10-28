"""
You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].

After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.
"""


storage = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

def get_most_similar_products(search_string):
    return [product for product in storage if search_string in product][:3]

products_found = []
chars_so_far = ""
storage = sorted(storage)

last_set = []
for char in searchWord:
    chars_so_far += char
    if chars_so_far not in last_set:
        last_set = get_most_similar_products(chars_so_far)

    products_found.append(last_set)

print(products_found)

# O(n*n*n*logn) -> O(n*n*n)

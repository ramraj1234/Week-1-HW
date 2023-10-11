#Probelm 1
prevnumber = 0
number = 1
fibonacci_numbers = [1]
count = 0
while count<9:
    number = number + prevnumber
    fibonacci_numbers.append(number)
    count = count+1
    prevnumber = fibonacci_numbers[count-1]
print(fibonacci_numbers)

#Problem 2 using the list from the previous questions
count = 0
odd_list = []
while count<len(fibonacci_numbers):
    if count%2==0:
        count = count+1
    else:
        odd_number = fibonacci_numbers[count]
        odd_list.append(odd_number)
        count = count+1
print(odd_list)

#Problem 3 using list from porblem 1
count = 0
reverse_list = []
while count<len(fibonacci_numbers):
    indice = -1 * (count+1)
    indice_number = fibonacci_numbers[indice]
    reverse_list.append(indice_number)
    count = count+1
print(reverse_list)

#Problem 4
string = """
	ChatGPT has created this text to provide tips on creating interesting paragraphs. 
	First, start with a clear topic sentence that introduces the main idea. 
	Then, support the topic sentence with specific details, examples, and evidence.
	Vary the sentence length and structure to keep the reader engaged.
	Finally, end with a strong concluding sentence that summarizes the main points.
	Remember, practice makes perfect!
	"""
string1 = string.lower()
new_lst = []
list_two = []
list_one = []
b = 0
list_of_words = string1.split()
for l in list_of_words:
    length = len(l)
    while b < length:
        if l[b] in [',', '.', '!']:
            nm = 0
        else:
            list_one.append(l[b])
        b = b+1
    word12 = ''.join(list_one)
    list_two.append(word12)
    list_one = []
    b = 0
length2 = len(list_two)
nj = 0
total3 = 0
totalp = 0
for nl in list_two:
    while nj < length2:
        if nl == list_two[nj]:
            totalp = totalp+1
        else:
            mlk = 0
        nj = nj+1
    nj=0
    if totalp == 1:
        total3 = total3+1
    totalp = 0
print(total3)
    
#Probelm 5
def vowel_count(word):
    list_one = []
    for b in word:
        list_one.append(b)
    vowel_count = 0
    vowel_list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for i in list_one:
        if i in vowel_list:
            vowel_count = vowel_count+1
    return(vowel_count)

#Problem 6
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for i in animals:
    word1 = i.upper()
    print(word1)

#Problem 7
count = 0
count = 1
while count <=15:
    if count%2==0:
        print(count, 'is even')
        count = count+1
    else:
        print(count, 'is odd')
        count = count+1
count = 0

#Problem 8
def sum1(n1, n2):
    n1 = int(input('Please enter number 1 '))
    n2 = int(input('Please enter number 2 '))
    total = n1+n2
    return(total)


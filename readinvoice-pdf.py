import re
from PyPDF2 import PdfReader
import pandas as pd

files = ['IV202308-01.pdf']
header = ['Date','Customer Name','Tel No.', 'E-mail', 'Total']

date_list = []
fullname_list = []
telno_list = []
email_list = []
total_list = []

reader = PdfReader(files[0])
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text().strip().split('\n')

cleaned_text = []

for t in text:
    if t != '' and t != ' ':
        replace_text = t.strip()
        cleaned_text.append(replace_text)
print(cleaned_text)

# ค้นหา Date
date_pattern = r'\d{1,2}\s[ADFJMNOS]\D+\d{4}'
date_regex = re.compile(date_pattern)
date_search = date_regex.search(cleaned_text[1].replace(' 3','3'))
date_list.append(date_search.group())

# ค้นหา Customer
fullname_pattern = r'[A-Z][a-z]+\s[A-Z][a-z]+'
fullname_regex = re.compile(fullname_pattern)
fullname_search = fullname_regex.search(cleaned_text[2][17:])
fullname_list.append(fullname_search.group())

# ค้นหา Tel No.
telno_pattern = r'(\+66|0)\d{1,2}(-)?\d{3}(-)?\d{4}'
telno_regex = re.compile(telno_pattern)
telno_search = telno_regex.search(cleaned_text[4])
telno_list.append(telno_search.group())

# ค้นหา E-mail
email_pattern = r'[\w\-._]+@\w+\.\w{2,3}(.)?\w{0,2}'
email_regex = re.compile(email_pattern)
email_search = email_regex.search(cleaned_text[5].replace(' ',''))
email_list.append(email_search.group())

# ค้นหา Total
total_pattern = r'(-)?\d{1,3}(?:,\d{3})*(.)?\d{0,2}'
total_regex = re.compile(total_pattern)
total_search = total_regex.search(cleaned_text[-2].replace(' ',''))
total_list.append(total_search.group())

print(date_list)
print(fullname_list)
print(telno_list)
print(email_list)
print(total_list)

data = pd.DataFrame({
    header[0]:date_list,
    header[1]:fullname_list,
    header[2]:telno_list,
    header[3]:email_list,
    header[4]:total_list
})

data.to_excel('invoice.xlsx', index=False)
import re
def validate_email(emails):
    pattern = r"\b[\w\.-]+@[\w\.-]+\.(?:com|org|net|edu|gov)\b"
    result = []
    for email in emails:
        match = re.findall(pattern, email)
        if match:
            result.append(match[0])
    print(result)

    
emails = [ "john@example.com", "alice@company.org", "bob@email", 
          "susan@123.com", "invalid.email", "no_domain@", "@missing_local", 
          "invalid@@domain.com", "john.doe@my_example.com"]

# validate_email(emails)
a = ['john@example.com', 'alice@company.org', 
     'susan@123.com', 'doe@my_example.com']
b = ['john@example.com', 'alice@company.org', 
     'susan@123.com', 'john.doe@my_example.com']


def aarr():
    pattern = re.search('a+', 'aaaAAA')
    print(pattern)
    
# aarr()

set1 = {1, 2, 4}
set2 = {4, 5, 6}
print(len(set1 + set2))
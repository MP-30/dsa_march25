import re

# def check(str):
#     pattern = r"\d{2}:\d{2}(?::\d{2})?"
#     match = re.findall(pattern, str)
#     # pattern = r"\d{2}:\d{2}(:\d{2}?)"
#     # match = re.search(pattern, str)
#     print(match)
    
# check("Started at 09:30, ended 13:45:10")

# def check(str):
#     pattern = r"\b\w+ing\b"
#     match = re.findall(pattern, str)
#     print(match)
    
# check("Started at aing bing cingh")


# def check(str):
#     # pattern = r"\b[A-Z]+[0-9]+\b"
#     pattern = r"\b[A-Z]+\d{3}\b"
#     match = re.findall(pattern, str)
#     print(match)
    
# check("ERP123 occufjfja asjfdu WARN456 adnd FAIL342")

# def check(str):
#     pattern = r"[0-9]+.[0-9]+.[0-9]+.[0-9]+"
#     match = re.sub(pattern, "[]", str)
#     print(match)
    
# check("dfd    13.45.34.1 ddff 34.677.89.6")

def check(str):
    pattern = r"^a-z"
    match = re.findall(pattern, str)
    print(match)
    
check("word worked wordead a s")

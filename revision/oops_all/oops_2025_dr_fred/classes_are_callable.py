class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}')

p = Program()
print(type(p))
print(Program.__dict__)
print(p.__dict__)
print(p.language)
p.language = 'java'
print(p.language)

def header(func):
    def wraper():
        return '<h1>' + func() + '</h1'
    return wraper

def strong(func):
    def wraper():
        return '<strong>' + func() + '</strong'
    return wraper

@strong
@header
def greet():
    return 'Hello'

print(greet())
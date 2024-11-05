def all_variants(text):
    len_ = len(text)
    for i in range(1, len_ + 1):
        for j in range(len_ - i + 1):
            yield text[j:j+i]

a = all_variants("abc")
for s in a:
    print(s)
f = open("eng.txt", "r")
frequency_dict = {}


def freq(word):
    if word in frequency_dict:
        frequency_dict[word] += 1
    else:
        frequency_dict[word] = 1


list(map(freq, f.read().split()))
sort = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)  # отсортировать по уменьшению частоты слов
print(frequency_dict)
print(sort)  # отсортированный frequency_dict
f.close()
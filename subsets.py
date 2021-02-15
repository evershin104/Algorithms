with open("input.txt", "r") as Input:
    n, k = map(int, Input.readline().split())


def generate_permutations(list):
    if len(list) < n:
        next = list.copy()
        for i in range(1, accepted_k(next) + 1):
            next.append(i)
            generate_permutations(next)
            next.pop()
    else:
         if rule(list):
            lists.append(list.copy())


# Возвращает максимальный допустимый элемент на следующую позицию
def accepted_k(list):
    toRet = max(list) + 1
    if toRet > k:
        return k
    return toRet


# Проверяет на выполнение правила заполнения листа распределений на блоки
def rule(indexes):
    if indexes[0] != 1:
        return False
    for i in range(1, len(indexes)):
        if len(indexes[0:i:1]) == 0:
            continue
        if indexes[i] > max(indexes[0:i:1]) + 1:
            return False
    if len(set(indexes)) == k:
        return True
    return False

# Числа
numbers = [str(i) for i in range(1, n + 1)]
# Лист листов, которые показывают разбиения на блоки
lists = []
# 0-ой элемент всегда принадлежит первому блоку (правило)
generate_permutations([1])


# Кривой вывод в output.txt
with open("output.txt", "w") as out:
    for list in lists:
        for kk in range(1, k + 1):
            str = "{"
            for nn in range(0, n):
                if list[nn] == kk:
                    str = str + numbers[nn] + " "
            if kk == k:
                str = str + "}" + "\n"
                out.write(str.replace(" }", "}"))
            else:
                str = str + "},"
                out.write(str.replace(" }", "}"))

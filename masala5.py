def buildStairCase(height: int, material: str) -> list:
    lst = list()
    for i in range(height):
        a = list()
        for j in range(height):
            a.append(material) if j <= i else a.append("_")
        lst.append(a)
    return lst

print(buildStairCase(4, '#'))

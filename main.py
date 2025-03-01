import re


def findSum(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    for i in range(n2 - 1, -1, -1):
        sum_val = (int(str1[i]) - 0) + (int(str2[i]) - 0) + carry
        result = str(sum_val % 10 + 0) + result
        carry = sum_val // 10

    if carry:
        result = str(carry + 0) + result

    return result


def findDiff(str1, str2):
    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    for i in range(n2 - 1, -1, -1):
        sub = (int(str1[i]) - 0) - (int(str2[i]) - 0) - carry

        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0

        result = str(sub + 0) + result

    return result

def removeLeadingZeros(s):
    pattern = "^0+(?!$)"
    s = re.sub(pattern, "", s)
    return s

def multiply(A, B):
    if len(A) < 10 or len(B) < 10:
        return str(int(A) * int(B))

    n = max(len(A), len(B))
    n2 = n // 2

    A = A.zfill(n)
    B = B.zfill(n)

    Al, Ar = A[:n2], A[n2:]
    Bl, Br = B[:n2], B[n2:]

    p = multiply(Al, Bl)
    q = multiply(Ar, Br)
    r = multiply(findSum(Al, Ar), findSum(Bl, Br))
    r = findDiff(r, findSum(p, q))

    return removeLeadingZeros(findSum(findSum(p + '0' * n, r + '0' * n2), q))


if __name__ == "__main__":
    A = input("Digite o primeiro número: ")
    B = input("Digite o segundo número: ")

    if not A.isdigit() or not B.isdigit():
        print("Entrada inválida! Certifique-se de inserir apenas números inteiros positivos.")
    else:
        print(f"Resultado da multiplicação: {multiply(A, B)}")

"""
if __name__ == "__main__":
    result = []
    sum_result = 0
    print("수를 입력하시오")
    count = input()
    for i in range(1, int(count)+1):
        num = input()
        if int(num) == 0:
            result.pop()
        else:
            result.append(num)

    for a in range(0, len(result)):
        sum_result += int(result[a])

    print(sum_result)

"""

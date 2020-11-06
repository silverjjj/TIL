# data는 오름차순으로 정렬된 리스트
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None
    mid = (start + end) // 2
    print(data[start], data[mid], data[end])
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    elif data[mid] < target:
        start = mid+1

    return binary_search_recursion(target, start, end, data)

if __name__ == '__main__':
    li = [i*2 for i in range(11)]
    target = 6
    idx = binary_search_recursion(target, 0, 10, li)

    print(li)
    print(idx)
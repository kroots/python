#lonely_int.py

def lonelyinteger(a):
    answer = 0
    for number in a:
        answer = answer ^ number
    return answer


if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
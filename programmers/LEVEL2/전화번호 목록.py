"""
해시 관련 문제
"""
def solution(phone_book):
    phone_book.sort() # 정렬
    book_list = [] 
    for i in range(1, len(phone_book)):
        j = len(phone_book[i-1]) # 요소의 길이값 
        print(phone_book[i][0:j],phone_book[i-1][0:j])
        book_list.append(phone_book[i][0:j].startswith(phone_book[i-1][0:j])) 
    if True not in book_list:
        return True
    else:
        return False
# datetime 라이브러리
import datetime as dt

def solution(book_time):
    answer = 1

    # n = len(book_time)
    # 모든 시작 시각을 기준으로 정렬 -> O(nlogn)
    book_time.sort(key=lambda x: x[0])

    # O(N^2) -> 백만
    rest_book_time = []
    i = 0
    while book_time:
        st1, et1 = book_time[i]
        for j in range(i + 1, len(book_time)):
            st2, et2 = book_time[j]
            diff = dt.datetime.strptime(st2, "%H:%M") - dt.datetime.strptime(et1, "%H:%M")
            if diff < dt.timedelta(minutes=10):
                rest_book_time.append((st2, et2))
            else:
                st1, et1 = st2, et2
        i += 1
        if rest_book_time:
            answer += 1
            i = 0
            book_time = rest_book_time[:]
            rest_book_time = []
        else:
            return answer

ex1 = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
ex3 = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
ex4 = [["10:00", "10:10"], ["10:05", "10:15"], ["10:10", "10:20"], ["10:15", "10:25"], ["10:20", "10:30"]]

solution(ex4)
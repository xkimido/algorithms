def solution(a, b):
    days = ['THU', 'FRI', 'SAT','SUN', 'MON', 'TUE','WED']
    months = [31,29,31,30,31,30, 31, 31, 30, 31, 30, 31]
    
    return days[(sum(months[:a-1])+b)%7]
def solution(data, ext, val_ext, sort_by):
    column_idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    return sorted(filter(lambda x:x[column_idx[ext]] < val_ext,data),key=lambda x:x[column_idx[sort_by]])
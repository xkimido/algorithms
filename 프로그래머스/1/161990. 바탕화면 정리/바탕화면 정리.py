def solution(wallpaper):
    width, height = len(wallpaper[0]), len(wallpaper)
    lux, luy, rdx, rdy = height, width, 0, 0

    for row_idx, row in enumerate(wallpaper):
        if "#" in row:
            lux = min(lux, row_idx)
            rdx = max(rdx, row_idx)
            luy = min(luy, row.index("#"))
            rdy = max(rdy, width - row[::-1].index("#") - 1)

    answer = [lux, luy, rdx + 1, rdy + 1]
    return answer
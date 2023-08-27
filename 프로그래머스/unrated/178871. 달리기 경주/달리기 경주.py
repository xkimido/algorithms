def solution(players, callings):
    player_indices = {player: index for index, player in enumerate(players)}

    for j in callings:
        current_index = player_indices[j]
        desired_index = current_index - 1
        if current_index > 0 and players[desired_index] != j:
            players[current_index], players[desired_index] = players[desired_index], players[current_index]
            player_indices[players[current_index]] = current_index
            player_indices[players[desired_index]] = desired_index

    return players
class KnightMoves:
    def run(self, start_x_y, end_x_y, board_x_y):
        i = 0
        next_moves = {start_x_y}
        while i < 20:
            if end_x_y in next_moves: return i          
            i += 1
            next_moves = self.calc_all_next_moves(next_moves)
            next_moves = self.filter_bounds(next_moves, board_x_y)

    def calc_all_next_moves(self, x_y_set):
        out = set()
        for x_y_tuple in x_y_set:
            out.update(self.calc_single_move(x_y_tuple))
        return out

    # note: uses a set to reduce dupes and increase efficiency
    def calc_single_move(self, current_pos_tuple):
        return {
            (current_pos_tuple[0]+2, current_pos_tuple[1] + 1),
            (current_pos_tuple[0]+2, current_pos_tuple[1] - 1),
            (current_pos_tuple[0]-2, current_pos_tuple[1] + 1),
            (current_pos_tuple[0]-2, current_pos_tuple[1] - 1),
            (current_pos_tuple[0]+1, current_pos_tuple[1] + 2),
            (current_pos_tuple[0]+1, current_pos_tuple[1] - 2),
            (current_pos_tuple[0]-1, current_pos_tuple[1] + 2),
            (current_pos_tuple[0]-1, current_pos_tuple[1] - 2),
        }

    # remove out of bounds
    def filter_bounds(self, x_y_set, x_y_bounds):
        out = set()
        for tuple in x_y_set:
            if(tuple[0] >= 0 and tuple[0] <= x_y_bounds[0]): # x bound
                if(tuple[1] >= 0 and tuple[1] <= x_y_bounds[1]): # y bound
                    out.add(tuple)
        return out
    
def convert_to_x_y(input):
    x = int(input % 8)
    y = int(input / 8)
    return (x,y)

def answer(src, dest):
    src = convert_to_x_y(src)
    dest = convert_to_x_y(dest)
    return KnightMoves().run(src, dest, (8, 64))



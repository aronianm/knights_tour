import random
class KnightsTour():

    def __init__(self, board_axis):
        if len(board_axis) != 2:
            raise Exception('Error Baord Axis incorrect', board_axis)
        self.board_axis = board_axis
        self.m = board_axis[0]
        self.n = board_axis[1]
        self.board = None
        self.moves = {}


    def build_board(self):

        if self.board is None:
            self.board_hash = {}
            self.available_moves = {}
            self.board = " " 
            self.board += "_" * 5 * self.m
            self.board += "\n"
            for y in range(1, self.m + 1):
                self.board += "|____"
                for x in range(1, self.n):
                    if self.board_hash.get((x,y)):
                        self.board += "|_xx_"
                    else:
                        self.board += "|____"

                
                self.board += "|\n"
        return self.board_hash
    def print_board(self):
        print(self.board)
    def run(self):
        board = self.build_board()
        possible_moves = self.get_all_available_moves()
        first_move = random.sample(self.available_moves.keys(), 1)[0]
        self.find_tour(first_move, 1)
        import pdb; pdb.set_trace()

    def get_all_available_moves(self):
        number_of_moves = self.m * self.n
        for y in range(1, self.m + 1):
            for x in range(1, self.n + 1):
                coordinates = (x, y)
                self.board_hash[coordinates] = False
                self.available_moves[coordinates] = self.find_all_moves(x,y)

    def find_all_moves(self, x, y):
        ## gets all valid moves for coordinates
        moves = [
            (x + 1, y + 2),
            (x + 1, y - 2),
            (x - 1, y + 2),
            (x - 1, y - 2),

            (x + 2, y + 1),
            (x + 2, y - 1),
            (x - 2, y + 1),
            (x - 2, y - 1),
        ]

        # less than 'n' and 'm' because we want to make sure its less than 
        # the edges
        return [m for m in moves if(
                            m[0] > 0 
                            and m[0] <= self.m
                            and m[1] <= self.n
                            and m[1] > 0
                            and not self.moves.get(m))]

    
    def find_tour(self, coordinates, i):
        moves = self.available_moves.get(coordinates)

        if len(moves) > 0:
            self.moves[coordinates] = i
            self.board_hash[coordinates] = True
            found_move = moves[0]
            self.get_all_available_moves()
            self.find_tour(found_move, i + 1)
        else:
            self.fix_euler(i)
        return self.moves

    def fix_euler(self, i):
        new_moves = self.find_max_moves()
        coords = new_moves[0]
        new_move = random.sample(new_moves[1], 1)[0]
        index = self.moves[coords]
        temp_moves = self.moves.copy()
        self.moves = {}
        self.moves[new_move] = index
        all_moves = [mv for mv in temp_moves.keys()]
        for y in range(0, len(temp_moves.keys())):
            new_i = index - 1
            if new_i > 1:
                new_c = all_moves[new_i]
                self.moves[new_c] = new_i
            else:
                another_temp = temp_moves.copy()
                for k,v in temp_moves.items():
                    another_temp[k] += 1
                self.moves.update(another_temp)




    def find_max_moves(self):
        moves = [m for m in self.moves.keys()]
        temp_array = []
        for move in moves:
            available_moves = self.find_all_moves(move[0], move[1])
            if len(available_moves) > 0:
                temp_array.append([move, available_moves])

        return random.sample(temp_array, 1)[0]








k = KnightsTour((5,5)).run()
from time import time


class Bot:

	def __init__(self):
		self.util = [3, 2, 3, 2, 4, 2, 3, 2, 3]
		self.small_util = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [
			[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
		self.small_val = self.small_util
		self.cells = []
		self.avail = []
		self.inf = 100000000000
		self.sym = '-'
		self.opp = '-'
		self.time = 0.0

	def solve_small(self, board, bo_pos, sym, opp):
		bpos = [bo_pos[0], bo_pos[1] / 3, bo_pos[2] / 3]
		val = 0
		for i in range(0, 3):
			s = 0
			f = 0
			for j in range(0, 3):
				val += self.small_util[bpos[0]][bpos[1] + i][bpos[2] + j]
				if board.small_boards_status[bpos[0]][bpos[1] + i][bpos[2] + j] == sym:
					s += 1
				if board.small_boards_status[bpos[0]][bpos[1] + i][bpos[2] + j] == opp:
					f = 1
					break
			if f == 0:
				if s == 3:
					val += 1000
				if s == 2:
					val += 100
				if s == 1:
					val += 10
		for j in range(0, 3):
			s = 0
			f = 0
			for i in range(0, 3):
				val += self.small_util[bpos[0]][bpos[1] + i][bpos[2] + j]
				if board.small_boards_status[bpos[0]][bpos[1] + i][bpos[2] + j] == sym:
					s += 1
				if board.small_boards_status[bpos[0]][bpos[1] + i][bpos[2] + j] == opp:
					f = 1
					break
			if f == 0:
				if s == 3:
					val += 1000
				if s == 2:
					val += 100
				if s == 1:
					val += 10
		s = 0
		f = 0
		for i in range(0, 3):
			val += self.small_util[bpos[0]][bpos[1] + i][bpos[2] + i]
			if board.small_boards_status[bpos[0]][bpos[1] + i][bpos[2] + i] == sym:
				s += 1
			if board.small_boards_status[bpos[0]][bpos[1] + i][bpos[2] + i] == opp:
				f = 1
				break
		if f == 0:
			if s == 3:
				val += 1000
			if s == 2:
				val += 100
			if s == 1:
				val += 10
		s = 0
		f = 0
		for i in range(0, 3):
			val += self.small_util[bpos[0]][bpos[1] + 2 - i][bpos[2] + i]
			if board.small_boards_status[bpos[0]][bpos[1] + 2 - i][bpos[2] + i] == sym:
				s += 1
			if board.small_boards_status[bpos[0]][bpos[1] + 2 - i][bpos[2] + i] == opp:
				f = 1
				break
		if f == 0:
			if s == 3:
				val += 1000
			if s == 2:
				val += 100
			if s == 1:
				val += 10
		return val

	def check_win(self, sym, bo_pos, board, ww):
		if ww == 1:
			bpos = [bo_pos[0], bo_pos[1] / 3, bo_pos[2] / 3]
			win = sym + sym + sym
			for i in range(0, 3):
				s = ""
				for j in range(0, 3):
					s += board.big_boards_status[bpos[0]
												 ][3 * bpos[1] + i][3 * bpos[2] + j]
					if s == win:
						return 1

			for j in range(0, 3):
				s = ""
				for i in range(0, 3):
					s += board.big_boards_status[bpos[0]
												 ][3 * bpos[1] + i][3 * bpos[2] + j]
				if s == win:
					return 1

			s = ""
			for i in range(0, 3):
				s += board.big_boards_status[bpos[0]
											 ][3 * bpos[1] + i][3 * bpos[2] + i]
			if s == win:
				return 1
			s = ""
			for i in range(0, 3):
				s += board.big_boards_status[bpos[0]
											 ][3 * bpos[1] + 2 - i][3 * bpos[2] + i]
			if s == win:
				return 1
			return 0
		else:
			win = sym + sym + sym
			bpos = [bo_pos[0], bo_pos[1], bo_pos[2]]
			for i in range(0, 3):
				s = ""
				for j in range(0, 3):
					s += board.small_boards_status[bpos[0]
												   ][3 * bpos[1] + i][3 * bpos[2] + j]
				if s == win:
					return 1

			for j in range(0, 3):
				s = ""
				for i in range(0, 3):
					s += board.small_boards_status[bpos[0]
												   ][3 * bpos[1] + i][3 * bpos[2] + j]
				if s == win:
					return 1

			s = ""
			for i in range(0, 3):
				s += board.small_boards_status[bpos[0]
											   ][3 * bpos[1] + i][3 * bpos[2] + i]
			if s == win:
				return 1
			s = ""
			for i in range(0, 3):
				s += board.small_boards_status[bpos[0]
											   ][3 * bpos[1] + 2 - i][3 * bpos[2] + i]
			if s == win:
				return 1
			return 0

	def finish_board(self, bo_pos, board, ww):
		if ww == 1:
			bpos = [bo_pos[0], bo_pos[1] / 3, bo_pos[2] / 3]
			for i in range(0, 3):
				for j in range(0, 3):
					if board.big_boards_status[bpos[0]][bpos[1] + i][bpos[2] + j] == '-':
						return 0
		else:
			bpos = [bo_pos[0], bo_pos[1], bo_pos[2]]
			for i in range(0, 3):
				for j in range(0, 3):
					if board.small_boards_status[bpos[0]][bpos[1] + i][bpos[2] + j] == '-':
						return 0
		return 1

	def first_move_board(self, board, bo_pos):
		bpos = [bo_pos[0], bo_pos[1] / 3, bo_pos[2] / 3]
		for i in range(0, 3):
			for j in range(0, 3):
				if board.big_boards_status[bpos[0]][bpos[1] + i][bpos[2] + j] != '-':
					return 0
		return 1

	def block(self, board, bo_pos, ww):
		if ww == 1:
			sig1 = self.sym
			sig2 = 'x'
			if sig1 == 'x':
				sig2 = 'o'
			bpos = [bo_pos[0], bo_pos[1] / 3, bo_pos[2] / 3]
			for i in range(0, 3):
				val = 0
				s = 0
				for j in range(0, 3):
					if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sig1:
						val += self.util[3 * i + j]
						s += 1
					if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sig2:
						val -= self.util[3 * i + j]
						s -= 1
				if s == 2:
					return val
			for j in range(0, 3):
				val = 0
				s = 0
				for i in range(0, 3):
					if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sig1:
						val += self.util[3 * i + j]
						s += 1
					if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sig2:
						val -= self.util[3 * i + j]
						s -= 1
				if s == 2:
					return val

			s = 0
			val = 0
			for i in range(0, 3):
				if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + i] == sig1:
					val += self.util[3 * i + j]
					s += 1
				if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + i] == sig2:
					val -= self.util[3 * i + j]
					s -= 1
			if s == 2:
				return val
			s = 0
			val = 0
			for i in range(0, 3):
				if board.big_boards_status[bpos[0]][bpos[1] + 2 - i][bpos[2] + i] == sig1:
					s += 1
				if board.big_boards_status[bpos[0]][bpos[1] + 2 - i][bpos[2] + i] == sig2:
					s -= 1
			if s == 2:
				return val
			return 0
		else:
			bpos = [bo_pos[0], bo_pos[1], bo_pos[2]]
			for i in range(0, 3):
				val = 0
				s = 0
				for j in range(0, 3):
					if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sig1:
						val += self.util[3 * i + j]
						s += 1
					if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sig2:
						val -= self.util[3 * i + j]
						s -= 1
				if s == 2:
					return val

			for j in range(0, 3):
				val = 0
				s = 0
				for i in range(0, 3):
					if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sig1:
						val += self.util[3 * i + j]
						s += 1
					if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sig2:
						val -= self.util[3 * i + j]
						s -= 1
				if s == 2:
					return val
			val = 0
			s = 0
			for i in range(0, 3):
				if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + i] == sig1:
					val += self.util[3 * i + j]
					s += 1
				if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + i] == sig2:
					val -= self.util[3 * i + j]
					s -= 1
			if s == 2:
				return val
			val = 0
			s = 0
			for i in range(0, 3):
				if board.small_boards_status[bpos[0]][bpos[1] + 2 - i][bpos[2] + i] == sig1:
					val += self.util[3 * i + j]
					s += 1
				if board.small_boards_status[bpos[0]][bpos[1] + 2 - i][bpos[2] + i] == sig2:
					val -= self.util[3 * i + j]
					s -= 1
			if s == 2:
				return val
			return 0

	def two_in_line(self, board, bo_pos, ww, sign):
		if ww == 1:
			bpos = [bo_pos[0], bo_pos[1] / 3, bo_pos[2] / 3]
			opp = 'o'
			if sign == 'o':
				opp = 'x'
			for i in range(0, 3):
				s = 0
				for j in range(0, 3):
					if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sign:
						s += 1
					if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == opp:
						s -= 1
				if s == 2:
					return 1
			for j in range(0, 3):
				s = 0
				for i in range(0, 3):
					if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sign:
						s += 1
					if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == opp:
						s -= 1
				if s == 2:
					return 1
			s = 0
			for i in range(0, 3):
				if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + i] == sign:
					s += 1
				if board.big_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + i] == opp:
					s -= 1
			if s == 2:
				return 1
			s = 0
			for i in range(0, 3):
				if board.big_boards_status[bpos[0]][bpos[1] + 2 - i][bpos[2] + i] == sign:
					s += 1
				if board.big_boards_status[bpos[0]][bpos[1] + 2 - i][bpos[2] + i] == opp:
					s -= 1
			if s == 2:
				return 1
			return 0
		else:
			bpos = [bo_pos[0], bo_pos[1], bo_pos[2]]
			for i in range(0, 3):
				s = 0
				for j in range(0, 3):
					if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sign:
						s += 1
					if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == opp:
						s -= 1
				if s == 2:
					return 1
			for j in range(0, 3):
				s = 0
				for i in range(0, 3):
					if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == sign:
						s += 1
					if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == opp:
						s -= 1
				if s == 2:
					return 1
			s = 0
			for i in range(0, 3):
				if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + i] == sign:
					s += 1
				if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + i] == opp:
					s -= 1
			if s == 2:
				return 1
			s = 0
			for i in range(0, 3):
				if board.small_boards_status[bpos[0]][bpos[1] + 2 - i][bpos[2] + i] == sign:
					s += 1
				if board.small_boards_status[bpos[0]][3 * bpos[1] + i][3 * bpos[2] + j] == opp:
					s -= 1
			if s == 2:
				return 1
			return 0

	def true_eve(self, board, sign):
		ans = 0
		for k in range(0, 2):
			for i in range(0, 3):
				for j in range(0, 3):
					if board.small_boards_status[k][i][j] == sign:
						ans += 40 * self.small_val[k][i][j]
					if board.small_boards_status[k][i][j] == '-':
						ans += self.small_val[k][i][j]
			for i in range(0, 3):
				conq, not_t, rep = 0, 0, 0
				for j in range(0, 3):
					if board.small_boards_status[k][i][j] == sign:
						conq += 1
					if board.small_boards_status[k][i][j] == '-':
						not_t += 1
					rep += self.small_val[k][i][j]
				if conq == 3 - not_t:
					if conq == 1:
						rep *= 10
					if conq == 2:
						rep *= 20
					ans += rep
			for j in range(0, 3):
				conq, not_t, rep = 0, 0, 0
				for i in range(0, 3):
					if board.small_boards_status[k][i][j] == sign:
						conq += 1
					if board.small_boards_status[k][i][j] == '-':
						not_t += 1
					rep += self.small_val[k][i][j]
				if conq == 3 - not_t:
					if conq == 1:
						rep *= 10
					if conq == 2:
						rep *= 20
					ans += rep
			conq, not_t, rep = 0, 0, 0
			for i in range(0, 3):
				if board.small_boards_status[k][i][i] == sign:
					conq += 1
				if board.small_boards_status[k][i][i] == '-':
					not_t += 1
				rep += self.small_val[k][i][i]
			if conq == 3 - not_t:
				if conq == 1:
					rep *= 10
				if conq == 2:
					rep *= 20
				ans += rep
			conq, not_t, rep = 0, 0, 0
			for i in range(0, 3):
				if board.small_boards_status[k][2 - i][i] == sign:
					conq += 1
				if board.small_boards_status[k][2 - i][i] == '-':
					not_t += 1
				rep += self.small_val[k][2 - i][i]
			if conq == 3 - not_t:
				if conq == 1:
					rep *= 10
				if conq == 2:
					rep *= 20
				ans += rep
		return ans

	def Heuristic_M(self, board, sign):
		for k in range(0, 2):
			for i in range(0, 3):
				for j in range(0, 3):
					self.small_val[k][i][j] = 0
					if board.small_boards_status[k][i][j] == sign:
						self.small_val[k][i][j] = 6 * self.inf
					if board.small_boards_status[k][i][j] == '-':
						conq, not_t, rep = 0, 0, 0
						for m in range(0, 3):
							conq, not_t = 0, 0
							for n in range(0, 3):
								if board.big_boards_status[k][3 * i + m][3 * j + n] == sign:
									conq += 1
								if board.big_boards_status[k][3 * i + m][3 * j + n] == '-':
									not_t += 1
							if conq == 3 - not_t:
								if conq == 1:
									rep += 500
								if conq == 2:
									rep += 50000
						for n in range(0, 3):
							conq, not_t = 0, 0
							for m in range(0, 3):
								if board.big_boards_status[k][3 * i + m][3 * j + n] == sign:
									conq += 1
								if board.big_boards_status[k][3 * i + m][3 * j + n] == '-':
									not_t += 1
							if conq == 3 - not_t:
								if conq == 1:
									rep += 500
								if conq == 2:
									rep += 50000
						conq, not_t = 0, 0
						for m in range(0, 3):
							if board.big_boards_status[k][3 * i + m][3 * j + m] == sign:
								conq += 1
							if board.big_boards_status[k][3 * i + m][3 * j + m] == '-':
								not_t += 1
						if conq == 3 - not_t:
							if conq == 1:
								rep += 500
							if conq == 2:
								rep += 50000
						conq, not_t = 0, 0
						for m in range(0, 3):
							if board.big_boards_status[k][3 * i + 2 - m][3 * j + m] == sign:
								conq += 1
							if board.big_boards_status[k][3 * i + 2 - m][3 * j + m] == '-':
								not_t += 1
						if conq == 3 - not_t:
							if conq == 1:
								rep += 500
							if conq == 2:
								rep += 50000
						self.small_val[k][i][j] = rep
		return self.true_eve(board, sign)

	def minimax_new(self, board,  old_move,sign, alpha, beta, depth, limit, bonus):
		stat = board.find_terminal_state()
		if stat[1] == 'WON':
			if self.sym == stat[0]:
				return (self.inf - depth,old_move)
			else:
				return (depth - self.inf,old_move)
		if stat[1] == 'DRAW':
			ans = 0
			mat = [[4, 6, 4], [6, 3, 6], [4, 6, 4]]
			for k in range(0, 2):
				for i in range(0, 3):
					for j in range(0, 3):
						if board.small_boards_status[k][i][j] == self.sym:
							ans += mat[i%3][j%3]
			return (200*ans,old_move)
		if depth > limit or time() - self.time > self.time_limit:
			return (self.Heuristic_M(board, self.sym) - self.Heuristic_M(board, self.opp),old_move)

		best = self.inf
		allowed_cells = board.find_valid_move_cells(old_move)
		res_moves = allowed_cells[0]
		opp = 'o'
		if sign == 'o':
			opp = 'x'
		 # for i in allowed_cells:
			# board.big_boards_status[i[0]][i[1]][i[2]] = opp
			# if self.check_win(opp, i, board, 1):
			# 	board.big_boards_status[bpos[0]][bpos[1]][bpos[2]] = '-'
			# 	board.big_boards_status[i[0]][i[1]][i[2]] = '-'
			# 	if sign == self.sym:
			# 		return (3 * (depth - self.inf),old_move)
			# 	else:
			# 		return (1.5 * (depth - self.inf),old_move)
		if sign == self.sym:
			best = -best
			for i in allowed_cells:
				ups = board.update(old_move, i, sign)[1]
				if ups and bonus == 0:
					val = self.minimax_new(board,i, sign, alpha, beta, depth + 1, limit, 1)
					if val[0] > best:
						best = val[0]
						res_moves = i
					alpha = max(alpha, best)
				else:
					val = self.minimax_new(board,i, opp, alpha, beta, depth + 1, limit, 0)
					if val[0] > best:
						best = val[0]
						res_moves = i
					alpha = max(alpha, best)
				board.big_boards_status[i[0]][i[1]][i[2]] = '-'
				board.small_boards_status[i[0]][i[1] / 3][i[2] / 3] = '-'
				if beta <= alpha:
					break
		else:
			for i in allowed_cells:
				ups = board.update(old_move, i, sign)[1]
				if ups and bonus == 0:
					val = self.minimax_new(board,i, sign, alpha, beta, depth + 1, limit, 1)
					if val[0] < best:
						best = val[0]
						res_moves = i
					beta = min(beta, best)
				else:
					val = self.minimax_new(board,i, opp, alpha, beta, depth + 1, limit, 0)
					if val[0] < best:
						best = val[0]
						res_moves = i
					beta = min(beta, best)
				board.big_boards_status[i[0]][i[1]][i[2]] = '-'
				board.small_boards_status[i[0]][i[1] / 3][i[2] / 3] = '-'
				if beta <= alpha:
					break
		return (best,res_moves)

	def move(self, board, old_move, flag):
		self.time_limit = 22
		st = time()
		self.sym = flag
		if self.sym == 'x':
			self.opp = 'o'
		else:
			self.opp = 'x'
		if old_move != (-1,-1,-1):
			self.util[3*(old_move[1]/3)+old_move[2]/3] -= 1000
		self.cells = board.find_valid_move_cells(old_move)
		self.time = time()
		limiter = 1
		ans = self.cells[0]
		maxval = -self.inf
		while 1:
			if time() - self.time > self.time_limit:
				break
			val = self.minimax_new(board,old_move, flag, -self.inf, self.inf, 0, limiter, 0)
			if val[0] > maxval:
				maxval = val[0]
				ans = val[1]
			if time() - self.time > self.time_limit:
				break
			limiter += 1
		self.util[3*(ans[1]/3)+ans[2]/3] += 1000
		return ans
		# self.util[3 * (self.cells[i][1] / 3) +
		#           self.cells[i][2] / 3] += 5
		# self.small_util[self.cells[i][0]][
		#     self.cells[i][1] / 3][self.cells[i][2] / 3] += 10

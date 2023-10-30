# Improved Eval
import chess
import time
class Evaluation:
        def evaluate_board(self, board):
            piece_values_midgame = {
                chess.PAWN: 100,
                chess.KNIGHT: 320,
                chess.BISHOP: 330,
                chess.ROOK: 500,
                chess.QUEEN: 900,
                chess.KING: 0
            }

            mg_pawn_table = [
             0,  0,  0,  0,  0,  0,  0,  0,
            50, 50, 50, 50, 50, 50, 50, 50,
            10, 10, 20, 30, 30, 20, 10, 10,
             5,  5, 10, 25, 25, 10,  5,  5,
             0,  0,  0, 20, 20,  0,  0,  0,
             5, -5,-10,  0,  0,-10, -5,  5,
             5, 10, 10,-20,-20, 10, 10,  5,
             0,  0,  0,  0,  0,  0,  0,  0
            ]

            eg_pawn_table = [
             0,  0,  0,  0,  0,  0,  0,  0,
            50, 50, 50, 50, 50, 50, 50, 50,
            10, 10, 20, 30, 30, 20, 10, 10,
             5,  5, 10, 25, 25, 10,  5,  5,
             0,  0,  0, 20, 20,  0,  0,  0,
             5, -5,-10,  0,  0,-10, -5,  5,
             5, 10, 10,-20,-20, 10, 10,  5,
             0,  0,  0,  0,  0,  0,  0,  0
            ]

            mg_knight_table = [
            -50,-40,-30,-30,-30,-30,-40,-50,
            -40,-20,  0,  0,  0,  0,-20,-40,
            -30,  0, 10, 15, 15, 10,  0,-30,
            -30,  5, 15, 20, 20, 15,  5,-30,
            -30,  0, 15, 20, 20, 15,  0,-30,
            -30,  5, 10, 15, 15, 10,  5,-30,
            -40,-20,  0,  5,  5,  0,-20,-40,
            -50,-40,-30,-30,-30,-30,-40,-50,
            ]

            eg_knight_table = [
            -50,-40,-30,-30,-30,-30,-40,-50,
            -40,-20,  0,  0,  0,  0,-20,-40,
            -30,  0, 10, 15, 15, 10,  0,-30,
            -30,  5, 15, 20, 20, 15,  5,-30,
            -30,  0, 15, 20, 20, 15,  0,-30,
            -30,  5, 10, 15, 15, 10,  5,-30,
            -40,-20,  0,  5,  5,  0,-20,-40,
            -50,-40,-30,-30,-30,-30,-40,-50,
            ]

            mg_bishop_table = [
            -20,-10,-10,-10,-10,-10,-10,-20,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -10,  0,  5, 10, 10,  5,  0,-10,
            -10,  5,  5, 10, 10,  5,  5,-10,
            -10,  0, 10, 10, 10, 10,  0,-10,
            -10, 10, 10, 10, 10, 10, 10,-10,
            -10,  5,  0,  0,  0,  0,  5,-10,
            -20,-10,-10,-10,-10,-10,-10,-20,
            ]

            eg_bishop_table = [
            -20,-10,-10,-10,-10,-10,-10,-20,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -10,  0,  5, 10, 10,  5,  0,-10,
            -10,  5,  5, 10, 10,  5,  5,-10,
            -10,  0, 10, 10, 10, 10,  0,-10,
            -10, 10, 10, 10, 10, 10, 10,-10,
            -10,  5,  0,  0,  0,  0,  5,-10,
            -20,-10,-10,-10,-10,-10,-10,-20,
            ]

            mg_rook_table = [
              0,  0,  0,  0,  0,  0,  0,  0,
              5, 10, 10, 10, 10, 10, 10,  5,
             -5,  0,  0,  0,  0,  0,  0, -5,
             -5,  0,  0,  0,  0,  0,  0, -5,
             -5,  0,  0,  0,  0,  0,  0, -5,
             -5,  0,  0,  0,  0,  0,  0, -5,
             -5,  0,  0,  0,  0,  0,  0, -5,
              0,  0,  0,  5,  5,  0,  0,  0
            ]

            eg_rook_table = [
              0,  0,  0,  0,  0,  0,  0,  0,
              5, 10, 10, 10, 10, 10, 10,  5,
             -5,  0,  0,  0,  0,  0,  0, -5,
             -5,  0,  0,  0,  0,  0,  0, -5,
             -5,  0,  0,  0,  0,  0,  0, -5,
             -5,  0,  0,  0,  0,  0,  0, -5,
             -5,  0,  0,  0,  0,  0,  0, -5,
              0,  0,  0,  5,  5,  0,  0,  0
            ]

            mg_queen_table = [
            -20,-10,-10, -5, -5,-10,-10,-20,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -10,  0,  5,  5,  5,  5,  0,-10,
             -5,  0,  5,  5,  5,  5,  0, -5,
              0,  0,  5,  5,  5,  5,  0, -5,
            -10,  5,  5,  5,  5,  5,  0,-10,
            -10,  0,  5,  0,  0,  0,  0,-10,
            -20,-10,-10, -5, -5,-10,-10,-20
            ]

            eg_queen_table = [
             -20,-10,-10, -5, -5,-10,-10,-20,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -10,  0,  5,  5,  5,  5,  0,-10,
             -5,  0,  5,  5,  5,  5,  0, -5,
              0,  0,  5,  5,  5,  5,  0, -5,
            -10,  5,  5,  5,  5,  5,  0,-10,
            -10,  0,  5,  0,  0,  0,  0,-10,
            -20,-10,-10, -5, -5,-10,-10,-20
            ]
        
            mg_king_table = [
            -30,-40,-40,-50,-50,-40,-40,-30,
            -30,-40,-40,-50,-50,-40,-40,-30,
            -30,-40,-40,-50,-50,-40,-40,-30,
            -30,-40,-40,-50,-50,-40,-40,-30,
            -20,-30,-30,-40,-40,-30,-30,-20,
            -10,-20,-20,-20,-20,-20,-20,-10,
             20, 20,  0,  0,  0,  0, 20, 20,
             20, 30, 10,  0,  0, 10, 30, 20
            ]
        
            eg_king_table = [
            -50,-40,-30,-20,-20,-30,-40,-50,
            -30,-20,-10,  0,  0,-10,-20,-30,
            -30,-10, 20, 30, 30, 20,-10,-30,
            -30,-10, 30, 40, 40, 30,-10,-30,
            -30,-10, 30, 40, 40, 30,-10,-30,
            -30,-10, 20, 30, 30, 20,-10,-30,
            -30,-30,  0,  0,  0,  0,-30,-30,
            -50,-30,-30,-30,-30,-30,-30,-50
            ]
        
            if board.is_checkmate():
                if board.turn == chess.WHITE:
                    return 10000
                else:
                    return -10000
            elif board.can_claim_draw() or board.is_stalemate() or board.is_insufficient_material():
                return 0
        
            num_pieces = len(board.piece_map())
            
            piece_values = piece_values_midgame
            pawn_square_table = mg_pawn_table
            knight_square_table = mg_knight_table
            bishop_square_table = mg_bishop_table
            rook_square_table = mg_rook_table
            queen_square_table = mg_queen_table
		
            if num_pieces <= 12:
                king_square_table = eg_king_table
            else:
                king_square_table = mg_king_table
        
            score = 0
            for square in chess.SQUARES:
                piece = board.piece_at(square)
                if piece is not None:
                    if piece.color == chess.WHITE:
        
                        if piece.piece_type == chess.PAWN:
                            score -= pawn_square_table[square]
                        if piece.piece_type == chess.KNIGHT:
                            score -= knight_square_table[square]
                        if piece.piece_type == chess.BISHOP:
                            score -= bishop_square_table[square]
                        if piece.piece_type == chess.ROOK:
                            score -= rook_square_table[square]
                        if piece.piece_type == chess.QUEEN:
                            score -= queen_square_table[square]
                        if piece.piece_type == chess.KING:
                            score -= king_square_table[square]
                        score -= piece_values[piece.piece_type]
                    else:
        
                        if piece.piece_type == chess.PAWN:
                            score += pawn_square_table[chess.square_mirror(square)]
                        if piece.piece_type == chess.KNIGHT:
                            score += knight_square_table[chess.square_mirror(square)]
                        if piece.piece_type == chess.BISHOP:
                            score += bishop_square_table[chess.square_mirror(square)]
                        if piece.piece_type == chess.ROOK:
                            score += rook_square_table[chess.square_mirror(square)]
                        if piece.piece_type == chess.QUEEN:
                            score += queen_square_table[chess.square_mirror(square)]
                        if piece.piece_type == chess.KING:
                            score += king_square_table[chess.square_mirror(square)]
                        score += piece_values[piece.piece_type]
        
            # Evaluate opponent's king mobility when there are 7 or fewer pieces on the board
            if board.legal_moves.count() <= 7:
                opponent_king_square = board.king(not board.turn)
                opponent_king_mobility = len(board.attacks(opponent_king_square))
                score += 100 * opponent_king_mobility if board.turn == chess.WHITE else 100 * opponent_king_mobility
        
            # Bonus for pushing pawns when there are less than 10 pieces on the board
            if board.legal_moves.count() <= 10:
                pawn_count = len(board.pieces(chess.PAWN, board.turn))
                if board.turn == chess.WHITE:
                  score -= 80 * pawn_count
                else:
                  score += 80 * pawn_count

                # Evaluate pawn structure
                white_pawns = board.pieces(chess.PAWN, chess.WHITE)
                black_pawns = board.pieces(chess.PAWN, chess.BLACK)
                white_pawn_structure = sum(mg_pawn_table[square] for square in white_pawns)
                black_pawn_structure = sum(mg_pawn_table[chess.square_mirror(square)] for square in black_pawns)
                score += white_pawn_structure - black_pawn_structure
            
            return score

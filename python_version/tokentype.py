from enum import Enum

class tokentype(Enum):


	function_tok, end_tok, if_tok, else_tok, print_tok, for_tok, while_tok, id, literal_integer, assignment_operator, le_operator, lt_operator, ge_operator,
    gt_operator, eq_operator, ne_operator, add_operator, sub_operator, mul_operator, div_operator, mod_operator,
    rev_div_operator, exp_operator, EOS_TOK
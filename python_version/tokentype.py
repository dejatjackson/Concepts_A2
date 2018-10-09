import enum


class tokentype():
    # TODO id, literal_integer, EOS_TOK
    def __init__(self):

        function_tok = "function"
        end_tok = "end"
        if_tok = "if"
        else_tok = "else"
        print_tok = "print"
        for_tok = "for"
        while_tok = "while"
        le_operator = "<="
        lt_operator = "<"
        ge_operator = ">="
        gt_operator = ">"
        ne_operator = "!="
        eq_operator = "=="
        assignment_operator = "="
        add_operator = "+"
        sub_operator = "-"
        mul_operator = "*"
        mod_operator = "%"
        exp_operator = "^"

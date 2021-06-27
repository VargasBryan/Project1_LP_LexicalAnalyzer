
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY BACKSLASH BOOLEAN BREAK CASE CHAR CLASS CLOSE_BRACE CLOSE_BRACKET CLOSE_PARENTHESIS COLON COMMA COMMENTS CONST DEFAULT DIFERENTE DIVIGUAL DIVISION DOUBLE_QUOTES ELSE FALSE FLOAT FOR FUNCTION IF IGUAL IGUALIGUAL INT LENGTH LET LINE_BREAK LONGCOMMENT MAP MASIGUAL MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MENOSIGUAL MODIGUAL MULTIPLICACION NAME NEW NOT NULL NUMBER OPEN_BRACE OPEN_BRACKET OPEN_PARENTHESIS OR POINT PORIGUAL POTIGUAK RESTA RETURN SEMICOLON SET SINGLE_QUOTE STATIC STRING SUMA SWITCH THEN TOSTRING TRUE TYPEOF UNDEFINED VAR WHILEexpression : expression SUMA expressionexpression : expression RESTA expression\n               | RESTA expressionexpression : termterm : term MULTIPLICACION factorterm : term DIVISION factorterm : factorfactor : NUMBERfactor : OPEN_PARENTHESIS expression CLOSE_PARENTHESIS'
    
_lr_action_items = {'RESTA':([0,1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,],[2,8,2,-4,-7,-8,2,2,2,8,8,8,8,-5,-6,-9,]),'NUMBER':([0,2,6,7,8,10,11,],[5,5,5,5,5,5,5,]),'OPEN_PARENTHESIS':([0,2,6,7,8,10,11,],[6,6,6,6,6,6,6,]),'$end':([1,3,4,5,9,13,14,15,16,17,],[0,-4,-7,-8,-3,-1,-2,-5,-6,-9,]),'SUMA':([1,3,4,5,9,12,13,14,15,16,17,],[7,-4,-7,-8,7,7,7,7,-5,-6,-9,]),'CLOSE_PARENTHESIS':([3,4,5,9,12,13,14,15,16,17,],[-4,-7,-8,-3,17,-1,-2,-5,-6,-9,]),'MULTIPLICACION':([3,4,5,15,16,17,],[10,-7,-8,-5,-6,-9,]),'DIVISION':([3,4,5,15,16,17,],[11,-7,-8,-5,-6,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,6,7,8,],[1,9,12,13,14,]),'term':([0,2,6,7,8,],[3,3,3,3,3,]),'factor':([0,2,6,7,8,10,11,],[4,4,4,4,4,15,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression SUMA expression','expression',3,'p_expression_plus','sintactical.py',10),
  ('expression -> expression RESTA expression','expression',3,'p_expressions_minus','sintactical.py',17),
  ('expression -> RESTA expression','expression',2,'p_expressions_minus','sintactical.py',18),
  ('expression -> term','expression',1,'p_expression_term','sintactical.py',25),
  ('term -> term MULTIPLICACION factor','term',3,'p_term_times','sintactical.py',29),
  ('term -> term DIVISION factor','term',3,'p_term_div','sintactical.py',33),
  ('term -> factor','term',1,'p_term_factor','sintactical.py',37),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactical.py',41),
  ('factor -> OPEN_PARENTHESIS expression CLOSE_PARENTHESIS','factor',3,'p_factor_expr','sintactical.py',45),
]

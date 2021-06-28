
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY BACKSLASH BOOLEAN BREAK CASE CHAR CLASS CLOSE_BRACE CLOSE_BRACKET CLOSE_PARENTHESIS COLON COMMA COMMENTS CONST DEFAULT DIFERENTE DIVIGUAL DIVISION DOUBLE_QUOTES ELSE FALSE FLOAT FOR FUNCTION IF IGUAL IGUALIGUAL INT LENGTH LET LINE_BREAK LONGCOMMENT MAP MASIGUAL MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MENOSIGUAL MODIGUAL MULTIPLICACION NAME NEW NOT NULL NUMBER OPEN_BRACE OPEN_BRACKET OPEN_PARENTHESIS OR POINT PORIGUAL POTIGUAL RESTA RETURN SEMICOLON SET SINGLE_QUOTE STATIC STRING SUMA SWITCH THEN TOSTRING TRUE TYPEOF UNDEFINED VAR WHILEexpression : variable\n    | variable expression\n    | dataStruct\n    | dataStruct expression\n    | controlStruct\n    | controlStruct expressionvariable : type NAME IGUAL datatype SEMICOLONcontrolStruct : while\n    | fordataStruct : arraywhile : WHILE OPEN_PARENTHESIS expression CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE\n    | WHILE OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACEfor : FOR OPEN_PARENTHESIS inicialization SEMICOLON condition SEMICOLON operations CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE inicialization : type NAME IGUAL NUMBER\n    | NAME IGUAL NUMBERcondition : NAME clause value operations : NUMBER operand NUMBER\n    | NAME SUMA SUMA\n    | NAME RESTA RESTA datatype : NUMBER\n    | STRING\n    | operations\n    | CHARoperand : SUMA \n    | RESTA \n    | MULTIPLICACION \n    | DIVISIONbool : TRUE\n    | FALSEtype : CONST\n    | LET\n    | VARclause :  IGUALIGUAL\n    | DIFERENTE\n    | MAYORQUE\n    | MAYORIGUALQUE\n    | MENORQUE\n    | MENORIGUALQUE value : NAME\n    | NUMBERarray : type NAME IGUAL OPEN_BRACKET items CLOSE_BRACKET SEMICOLON\n    | type NAME IGUAL NEW ARRAY OPEN_PARENTHESIS items CLOSE_PARENTHESIS SEMICOLONitems : numeros\n    | cadenanumeros : NUMBER\n    | NUMBER COMMA numeroscadena : STRING \n    | STRING COMMA cadena'
    
_lr_action_items = {'CONST':([0,2,3,4,6,7,8,18,19,43,55,56,79,83,84,92,93,95,],[9,9,9,9,-10,-8,-9,9,9,-7,9,9,-41,-11,-12,-42,9,-13,]),'LET':([0,2,3,4,6,7,8,18,19,43,55,56,79,83,84,92,93,95,],[10,10,10,10,-10,-8,-9,10,10,-7,10,10,-41,-11,-12,-42,10,-13,]),'VAR':([0,2,3,4,6,7,8,18,19,43,55,56,79,83,84,92,93,95,],[11,11,11,11,-10,-8,-9,11,11,-7,11,11,-41,-11,-12,-42,11,-13,]),'WHILE':([0,2,3,4,6,7,8,18,43,55,56,79,83,84,92,93,95,],[12,12,12,12,-10,-8,-9,12,-7,12,12,-41,-11,-12,-42,12,-13,]),'FOR':([0,2,3,4,6,7,8,18,43,55,56,79,83,84,92,93,95,],[13,13,13,13,-10,-8,-9,13,-7,13,13,-41,-11,-12,-42,13,-13,]),'$end':([1,2,3,4,6,7,8,14,15,16,43,79,83,84,92,95,],[0,-1,-3,-5,-10,-8,-9,-2,-4,-6,-7,-41,-11,-12,-42,-13,]),'CLOSE_PARENTHESIS':([2,3,4,6,7,8,14,15,16,21,22,23,24,43,45,46,47,48,61,62,67,79,80,81,82,83,84,85,92,95,],[-1,-3,-5,-10,-8,-9,-2,-4,-6,36,37,-28,-29,-7,-43,-44,-45,-47,-18,-19,-17,-41,-46,-48,90,-11,-12,91,-42,-13,]),'CLOSE_BRACE':([2,3,4,6,7,8,14,15,16,43,68,69,79,83,84,92,94,95,],[-1,-3,-5,-10,-8,-9,-2,-4,-6,-7,83,84,-41,-11,-12,-42,95,-13,]),'NAME':([5,9,10,11,19,20,26,38,70,71,72,73,74,75,76,77,],[17,-30,-31,-32,27,28,39,58,28,87,-33,-34,-35,-36,-37,-38,]),'OPEN_PARENTHESIS':([12,13,49,],[18,19,66,]),'IGUAL':([17,27,39,],[20,40,59,]),'TRUE':([18,],[23,]),'FALSE':([18,],[24,]),'OPEN_BRACKET':([20,],[30,]),'NEW':([20,],[31,]),'NUMBER':([20,30,40,50,51,52,53,54,59,64,66,70,71,72,73,74,75,76,77,],[32,47,60,67,-24,-25,-26,-27,78,47,47,86,89,-33,-34,-35,-36,-37,-38,]),'STRING':([20,30,65,66,],[33,48,48,48,]),'CHAR':([20,],[35,]),'SEMICOLON':([25,29,32,33,34,35,57,60,61,62,63,67,78,87,88,89,90,],[38,43,-20,-21,-22,-23,70,-15,-18,-19,79,-17,-14,-39,-16,-40,92,]),'SUMA':([28,32,41,86,],[41,51,61,51,]),'RESTA':([28,32,42,86,],[42,52,62,52,]),'ARRAY':([31,],[49,]),'MULTIPLICACION':([32,86,],[53,53,]),'DIVISION':([32,86,],[54,54,]),'OPEN_BRACE':([36,37,91,],[55,56,93,]),'CLOSE_BRACKET':([44,45,46,47,48,80,81,],[63,-43,-44,-45,-47,-46,-48,]),'COMMA':([47,48,],[64,65,]),'IGUALIGUAL':([58,],[72,]),'DIFERENTE':([58,],[73,]),'MAYORQUE':([58,],[74,]),'MAYORIGUALQUE':([58,],[75,]),'MENORQUE':([58,],[76,]),'MENORIGUALQUE':([58,],[77,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,4,18,55,56,93,],[1,14,15,16,21,68,69,94,]),'variable':([0,2,3,4,18,55,56,93,],[2,2,2,2,2,2,2,2,]),'dataStruct':([0,2,3,4,18,55,56,93,],[3,3,3,3,3,3,3,3,]),'controlStruct':([0,2,3,4,18,55,56,93,],[4,4,4,4,4,4,4,4,]),'type':([0,2,3,4,18,19,55,56,93,],[5,5,5,5,5,26,5,5,5,]),'array':([0,2,3,4,18,55,56,93,],[6,6,6,6,6,6,6,6,]),'while':([0,2,3,4,18,55,56,93,],[7,7,7,7,7,7,7,7,]),'for':([0,2,3,4,18,55,56,93,],[8,8,8,8,8,8,8,8,]),'bool':([18,],[22,]),'inicialization':([19,],[25,]),'datatype':([20,],[29,]),'operations':([20,70,],[34,85,]),'items':([30,66,],[44,82,]),'numeros':([30,64,66,],[45,80,45,]),'cadena':([30,65,66,],[46,81,46,]),'operand':([32,86,],[50,50,]),'condition':([38,],[57,]),'clause':([58,],[71,]),'value':([71,],[88,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> variable','expression',1,'p_expression_expr','sintactical.py',9),
  ('expression -> variable expression','expression',2,'p_expression_expr','sintactical.py',10),
  ('expression -> dataStruct','expression',1,'p_expression_expr','sintactical.py',11),
  ('expression -> dataStruct expression','expression',2,'p_expression_expr','sintactical.py',12),
  ('expression -> controlStruct','expression',1,'p_expression_expr','sintactical.py',13),
  ('expression -> controlStruct expression','expression',2,'p_expression_expr','sintactical.py',14),
  ('variable -> type NAME IGUAL datatype SEMICOLON','variable',5,'p_variable_expr','sintactical.py',17),
  ('controlStruct -> while','controlStruct',1,'p_controlStruct_expr','sintactical.py',20),
  ('controlStruct -> for','controlStruct',1,'p_controlStruct_expr','sintactical.py',21),
  ('dataStruct -> array','dataStruct',1,'p_dataStruct_expr','sintactical.py',24),
  ('while -> WHILE OPEN_PARENTHESIS expression CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE','while',7,'p_while_expr','sintactical.py',27),
  ('while -> WHILE OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE','while',7,'p_while_expr','sintactical.py',28),
  ('for -> FOR OPEN_PARENTHESIS inicialization SEMICOLON condition SEMICOLON operations CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE','for',11,'p_for_expr','sintactical.py',31),
  ('inicialization -> type NAME IGUAL NUMBER','inicialization',4,'p_inicialization','sintactical.py',34),
  ('inicialization -> NAME IGUAL NUMBER','inicialization',3,'p_inicialization','sintactical.py',35),
  ('condition -> NAME clause value','condition',3,'p_condition','sintactical.py',38),
  ('operations -> NUMBER operand NUMBER','operations',3,'p_operations','sintactical.py',41),
  ('operations -> NAME SUMA SUMA','operations',3,'p_operations','sintactical.py',42),
  ('operations -> NAME RESTA RESTA','operations',3,'p_operations','sintactical.py',43),
  ('datatype -> NUMBER','datatype',1,'p_datatype_expr','sintactical.py',46),
  ('datatype -> STRING','datatype',1,'p_datatype_expr','sintactical.py',47),
  ('datatype -> operations','datatype',1,'p_datatype_expr','sintactical.py',48),
  ('datatype -> CHAR','datatype',1,'p_datatype_expr','sintactical.py',49),
  ('operand -> SUMA','operand',1,'p_operand_expr','sintactical.py',52),
  ('operand -> RESTA','operand',1,'p_operand_expr','sintactical.py',53),
  ('operand -> MULTIPLICACION','operand',1,'p_operand_expr','sintactical.py',54),
  ('operand -> DIVISION','operand',1,'p_operand_expr','sintactical.py',55),
  ('bool -> TRUE','bool',1,'p_bool_expr','sintactical.py',58),
  ('bool -> FALSE','bool',1,'p_bool_expr','sintactical.py',59),
  ('type -> CONST','type',1,'p_type_expr','sintactical.py',62),
  ('type -> LET','type',1,'p_type_expr','sintactical.py',63),
  ('type -> VAR','type',1,'p_type_expr','sintactical.py',64),
  ('clause -> IGUALIGUAL','clause',1,'p_clause_expr','sintactical.py',67),
  ('clause -> DIFERENTE','clause',1,'p_clause_expr','sintactical.py',68),
  ('clause -> MAYORQUE','clause',1,'p_clause_expr','sintactical.py',69),
  ('clause -> MAYORIGUALQUE','clause',1,'p_clause_expr','sintactical.py',70),
  ('clause -> MENORQUE','clause',1,'p_clause_expr','sintactical.py',71),
  ('clause -> MENORIGUALQUE','clause',1,'p_clause_expr','sintactical.py',72),
  ('value -> NAME','value',1,'p_value_expr','sintactical.py',75),
  ('value -> NUMBER','value',1,'p_value_expr','sintactical.py',76),
  ('array -> type NAME IGUAL OPEN_BRACKET items CLOSE_BRACKET SEMICOLON','array',7,'p_array_expr','sintactical.py',79),
  ('array -> type NAME IGUAL NEW ARRAY OPEN_PARENTHESIS items CLOSE_PARENTHESIS SEMICOLON','array',9,'p_array_expr','sintactical.py',80),
  ('items -> numeros','items',1,'p_items_expr','sintactical.py',84),
  ('items -> cadena','items',1,'p_items_expr','sintactical.py',85),
  ('numeros -> NUMBER','numeros',1,'p_numeros_expr','sintactical.py',88),
  ('numeros -> NUMBER COMMA numeros','numeros',3,'p_numeros_expr','sintactical.py',89),
  ('cadena -> STRING','cadena',1,'p_cadena_expr','sintactical.py',92),
  ('cadena -> STRING COMMA cadena','cadena',3,'p_cadena_expr','sintactical.py',93),
]

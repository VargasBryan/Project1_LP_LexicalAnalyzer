
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND ARRAY BACKSLASH BOOLEAN BREAK CASE CHAR CLASS CLEAR CLOSE_BRACE CLOSE_BRACKET CLOSE_PARENTHESIS COLON COMMA COMMENTS CONST DEFAULT DELETE DIFERENTE DIVIGUAL DIVISION DOUBLE_QUOTES ELSE ELSEIF FALSE FLOAT FOR FUNCTION IF IGUAL IGUALIGUAL INT LENGTH LET LINE_BREAK LONGCOMMENT MAP MASIGUAL MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MENOSIGUAL MODIGUAL MULTIPLICACION NAME NEW NOT NULL NUMBER OPEN_BRACE OPEN_BRACKET OPEN_PARENTHESIS OR POINT POP PORIGUAL POTIGUAL PUSH RESTA RETURN SEMICOLON SET SINGLE_QUOTE STATIC STRING SUMA SWITCH THEN TOSTRING TRUE TYPEOF UNDEFINED UNSHIFT VAR WHILEexpression : variable\n    | variable expression\n    | dataStruct\n    | dataStruct expression\n    | controlStruct\n    | controlStruct expression\n    | methodsSetvariable : type NAME IGUAL datatype SEMICOLON\n        | type NAME IGUAL operations SEMICOLON\n        | NAME IGUAL datatype SEMICOLONcontrolStruct : while\n    | fordataStruct : array\n    | set while : WHILE OPEN_PARENTHESIS controlArg CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE\n    | WHILE OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACEif : soloIf \n    | soloIf elseIf\n    | soloIf elseIf else\n    | soloIf else soloIf : IF OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE elseIf : ELSEIF OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE\n        | ELSEIF OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE soloIf else : ELSE OPEN_BRACE expression CLOSE_BRACEcomparacion : IGUALIGUAL\n    | DIFERENTE\n    | MAYORQUE\n    | MAYORIGUALQUE\n    | MENORQUE\n    | MENORIGUALQUEcontrolArg : argUnico comparacion argUnicofor : FOR OPEN_PARENTHESIS inicialization SEMICOLON condition SEMICOLON operations CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE inicialization : type NAME IGUAL NUMBER\n    | NAME IGUAL NUMBERcondition : NAME clause value operations : NUMBER operand NUMBER\n    | NAME SUMA SUMA\n    | NAME RESTA RESTA datatype : NUMBER\n    | STRING\n    | CHARoperand : SUMA \n    | RESTA \n    | MULTIPLICACION \n    | DIVISIONbool : TRUE\n    | FALSEtype : CONST\n    | LET\n    | VARclause :  IGUALIGUAL\n    | DIFERENTE\n    | MAYORQUE\n    | MAYORIGUALQUE\n    | MENORQUE\n    | MENORIGUALQUE value : NAME\n    | NUMBERarray : type NAME IGUAL OPEN_BRACKET items CLOSE_BRACKET SEMICOLON\n    | type NAME IGUAL NEW ARRAY OPEN_PARENTHESIS items CLOSE_PARENTHESIS SEMICOLONmap : iniciarMap\n        | escribirMap\n        | generarMap iniciarMap : variable IGUAL NEW MAP OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLONescribirMap : variable IGUAL OPEN_BRACE claveValor CLOSE_BRACEclaveValor : clave COLON valor\n    | clave COLON valor COMMA claveValorclave : datatypevalor : datatype\n        | dataStructgenerarMap : variable IGUAL OPEN_BRACE tuplas CLOSE_BRACEtuplas : tupla\n        | tupla tuplas  tupla : OPEN_BRACKET datatype CLOSE_BRACKET\n        | OPEN_BRACKET datatype COMMA datatype CLOSE_BRACKETarrayFn : POINT POP OPEN_PARENTHESIS CLOSE_PARENTHESIS\n    | POINT PUSH OPEN_PARENTHESIS argUnico CLOSE_PARENTHESIS\n    | POINT UNSHIFT OPEN_PARENTHESIS argUnico CLOSE_PARENTHESISargUnico : NUMBER\n    | STRING\n    | NAMEset : type NAME IGUAL NEW SET OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON\n    | type NAME IGUAL NEW SET OPEN_PARENTHESIS OPEN_BRACKET items CLOSE_BRACKET CLOSE_PARENTHESIS SEMICOLON\n    | type NAME IGUAL NEW SET OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON\n    | NAME IGUAL NEW SET OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON\n    | NAME IGUAL NEW SET OPEN_PARENTHESIS OPEN_BRACKET items CLOSE_BRACKET CLOSE_PARENTHESIS SEMICOLON\n    | NAME IGUAL NEW SET OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLONmethodsSet : NAME POINT ADD OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON\n    | NAME POINT DELETE OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON\n    | NAME POINT CLEAR OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON\n    items : numeros\n    | cadenanumeros : NUMBER\n    | NUMBER COMMA numeroscadena : STRING \n    | STRING COMMA cadenaelement : STRING\n    | NUMBER\n    | NAME'
    
_lr_action_items = {'NAME':([0,2,3,4,6,8,9,10,11,12,13,14,23,24,25,43,51,53,54,58,59,60,61,62,63,64,65,70,71,84,91,92,104,114,115,116,117,118,119,120,121,123,130,135,136,143,147,149,151,153,155,157,158,],[7,7,7,7,20,-13,-14,-11,-12,-48,-49,-50,41,44,45,66,-10,85,85,41,-25,-26,-27,-28,-29,-30,95,-8,-9,85,7,7,85,45,139,-51,-52,-53,-54,-55,-56,-59,-85,-15,-16,-82,-87,-60,-84,7,-86,-83,-32,]),'CONST':([0,2,3,4,8,9,10,11,24,51,70,71,91,92,123,130,135,136,143,147,149,151,153,155,157,158,],[12,12,12,12,-13,-14,-11,-12,12,-10,-8,-9,12,12,-59,-85,-15,-16,-82,-87,-60,-84,12,-86,-83,-32,]),'LET':([0,2,3,4,8,9,10,11,24,51,70,71,91,92,123,130,135,136,143,147,149,151,153,155,157,158,],[13,13,13,13,-13,-14,-11,-12,13,-10,-8,-9,13,13,-59,-85,-15,-16,-82,-87,-60,-84,13,-86,-83,-32,]),'VAR':([0,2,3,4,8,9,10,11,24,51,70,71,91,92,123,130,135,136,143,147,149,151,153,155,157,158,],[14,14,14,14,-13,-14,-11,-12,14,-10,-8,-9,14,14,-59,-85,-15,-16,-82,-87,-60,-84,14,-86,-83,-32,]),'WHILE':([0,2,3,4,8,9,10,11,51,70,71,91,92,123,130,135,136,143,147,149,151,153,155,157,158,],[15,15,15,15,-13,-14,-11,-12,-10,-8,-9,15,15,-59,-85,-15,-16,-82,-87,-60,-84,15,-86,-83,-32,]),'FOR':([0,2,3,4,8,9,10,11,51,70,71,91,92,123,130,135,136,143,147,149,151,153,155,157,158,],[16,16,16,16,-13,-14,-11,-12,-10,-8,-9,16,16,-59,-85,-15,-16,-82,-87,-60,-84,16,-86,-83,-32,]),'$end':([1,2,3,4,5,8,9,10,11,17,18,19,51,70,71,111,123,130,133,134,135,136,143,147,149,151,155,157,158,],[0,-1,-3,-5,-7,-13,-14,-11,-12,-2,-4,-6,-10,-8,-9,-90,-59,-85,-88,-89,-15,-16,-82,-87,-60,-84,-86,-83,-32,]),'CLOSE_BRACE':([2,3,4,5,8,9,10,11,17,18,19,51,70,71,111,112,113,123,130,133,134,135,136,143,147,149,151,155,156,157,158,],[-1,-3,-5,-7,-13,-14,-11,-12,-2,-4,-6,-10,-8,-9,-90,135,136,-59,-85,-88,-89,-15,-16,-82,-87,-60,-84,-86,158,-83,-32,]),'IGUAL':([7,20,44,66,],[21,25,67,96,]),'POINT':([7,],[22,]),'OPEN_PARENTHESIS':([15,16,31,32,33,52,77,78,],[23,24,53,54,55,84,103,104,]),'NEW':([21,25,],[27,49,]),'NUMBER':([21,23,25,48,53,54,58,59,60,61,62,63,64,67,79,80,81,82,83,84,96,101,103,104,107,114,115,116,117,118,119,120,121,128,],[28,39,50,75,88,88,39,-25,-26,-27,-28,-29,-30,97,105,-42,-43,-44,-45,88,122,75,75,88,75,138,141,-51,-52,-53,-54,-55,-56,75,]),'STRING':([21,23,25,48,53,54,58,59,60,61,62,63,64,84,102,103,104,107,128,],[29,40,29,76,87,87,40,-25,-26,-27,-28,-29,-30,87,76,76,87,76,76,]),'CHAR':([21,25,],[30,30,]),'ADD':([22,],[31,]),'DELETE':([22,],[32,]),'CLEAR':([22,],[33,]),'TRUE':([23,],[37,]),'FALSE':([23,],[38,]),'OPEN_BRACKET':([25,84,104,],[48,107,128,]),'SEMICOLON':([26,28,29,30,42,46,47,50,90,94,97,98,99,100,105,106,109,110,122,127,132,139,140,141,142,145,152,154,],[51,-39,-40,-41,65,70,71,-39,111,114,-34,-37,-38,123,-36,130,133,134,-33,143,147,-57,-35,-58,149,151,155,157,]),'SET':([27,49,],[52,78,]),'CLOSE_PARENTHESIS':([34,35,37,38,39,40,41,55,73,74,75,76,84,85,86,87,88,89,93,98,99,104,105,108,124,125,126,129,137,146,150,],[56,57,-46,-47,-79,-80,-81,90,-91,-92,-93,-95,106,-99,109,-97,-98,110,-31,-37,-38,127,-36,132,-94,-96,142,145,148,152,154,]),'IGUALIGUAL':([36,39,40,41,95,],[59,-79,-80,-81,116,]),'DIFERENTE':([36,39,40,41,95,],[60,-79,-80,-81,117,]),'MAYORQUE':([36,39,40,41,95,],[61,-79,-80,-81,118,]),'MAYORIGUALQUE':([36,39,40,41,95,],[62,-79,-80,-81,119,]),'MENORQUE':([36,39,40,41,95,],[63,-79,-80,-81,120,]),'MENORIGUALQUE':([36,39,40,41,95,],[64,-79,-80,-81,121,]),'SUMA':([45,50,68,138,],[68,80,98,80,]),'RESTA':([45,50,69,138,],[69,81,99,81,]),'ARRAY':([49,],[77,]),'MULTIPLICACION':([50,138,],[82,82,]),'DIVISION':([50,138,],[83,83,]),'OPEN_BRACE':([56,57,148,],[91,92,153,]),'CLOSE_BRACKET':([72,73,74,75,76,124,125,131,144,],[100,-91,-92,-93,-95,-94,-96,146,150,]),'COMMA':([75,76,],[101,102,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,4,91,92,153,],[1,17,18,19,112,113,156,]),'variable':([0,2,3,4,91,92,153,],[2,2,2,2,2,2,2,]),'dataStruct':([0,2,3,4,91,92,153,],[3,3,3,3,3,3,3,]),'controlStruct':([0,2,3,4,91,92,153,],[4,4,4,4,4,4,4,]),'methodsSet':([0,2,3,4,91,92,153,],[5,5,5,5,5,5,5,]),'type':([0,2,3,4,24,91,92,153,],[6,6,6,6,43,6,6,6,]),'array':([0,2,3,4,91,92,153,],[8,8,8,8,8,8,8,]),'set':([0,2,3,4,91,92,153,],[9,9,9,9,9,9,9,]),'while':([0,2,3,4,91,92,153,],[10,10,10,10,10,10,10,]),'for':([0,2,3,4,91,92,153,],[11,11,11,11,11,11,11,]),'datatype':([21,25,],[26,46,]),'controlArg':([23,],[34,]),'bool':([23,],[35,]),'argUnico':([23,58,],[36,93,]),'inicialization':([24,],[42,]),'operations':([25,114,],[47,137,]),'comparacion':([36,],[58,]),'items':([48,103,107,128,],[72,126,131,144,]),'numeros':([48,101,103,107,128,],[73,124,73,73,73,]),'cadena':([48,102,103,107,128,],[74,125,74,74,74,]),'operand':([50,138,],[79,79,]),'element':([53,54,84,104,],[86,89,108,129,]),'condition':([65,],[94,]),'clause':([95,],[115,]),'value':([115,],[140,]),}

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
  ('expression -> methodsSet','expression',1,'p_expression_expr','sintactical.py',15),
  ('variable -> type NAME IGUAL datatype SEMICOLON','variable',5,'p_variable_expr','sintactical.py',18),
  ('variable -> type NAME IGUAL operations SEMICOLON','variable',5,'p_variable_expr','sintactical.py',19),
  ('variable -> NAME IGUAL datatype SEMICOLON','variable',4,'p_variable_expr','sintactical.py',20),
  ('controlStruct -> while','controlStruct',1,'p_controlStruct_expr','sintactical.py',32),
  ('controlStruct -> for','controlStruct',1,'p_controlStruct_expr','sintactical.py',33),
  ('dataStruct -> array','dataStruct',1,'p_dataStruct_expr','sintactical.py',36),
  ('dataStruct -> set','dataStruct',1,'p_dataStruct_expr','sintactical.py',37),
  ('while -> WHILE OPEN_PARENTHESIS controlArg CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE','while',7,'p_while_expr','sintactical.py',40),
  ('while -> WHILE OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE','while',7,'p_while_expr','sintactical.py',41),
  ('if -> soloIf','if',1,'p_if_expr','sintactical.py',44),
  ('if -> soloIf elseIf','if',2,'p_if_expr','sintactical.py',45),
  ('if -> soloIf elseIf else','if',3,'p_if_expr','sintactical.py',46),
  ('if -> soloIf else','if',2,'p_if_expr','sintactical.py',47),
  ('soloIf -> IF OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE','soloIf',7,'p_soloIf_expr','sintactical.py',50),
  ('elseIf -> ELSEIF OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE','elseIf',7,'p_elseIf_expr','sintactical.py',53),
  ('elseIf -> ELSEIF OPEN_PARENTHESIS bool CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE soloIf','elseIf',8,'p_elseIf_expr','sintactical.py',54),
  ('else -> ELSE OPEN_BRACE expression CLOSE_BRACE','else',4,'p_else_expr','sintactical.py',57),
  ('comparacion -> IGUALIGUAL','comparacion',1,'p_comparacion_expr','sintactical.py',60),
  ('comparacion -> DIFERENTE','comparacion',1,'p_comparacion_expr','sintactical.py',61),
  ('comparacion -> MAYORQUE','comparacion',1,'p_comparacion_expr','sintactical.py',62),
  ('comparacion -> MAYORIGUALQUE','comparacion',1,'p_comparacion_expr','sintactical.py',63),
  ('comparacion -> MENORQUE','comparacion',1,'p_comparacion_expr','sintactical.py',64),
  ('comparacion -> MENORIGUALQUE','comparacion',1,'p_comparacion_expr','sintactical.py',65),
  ('controlArg -> argUnico comparacion argUnico','controlArg',3,'p_controlArg_expr','sintactical.py',68),
  ('for -> FOR OPEN_PARENTHESIS inicialization SEMICOLON condition SEMICOLON operations CLOSE_PARENTHESIS OPEN_BRACE expression CLOSE_BRACE','for',11,'p_for_expr','sintactical.py',70),
  ('inicialization -> type NAME IGUAL NUMBER','inicialization',4,'p_inicialization','sintactical.py',73),
  ('inicialization -> NAME IGUAL NUMBER','inicialization',3,'p_inicialization','sintactical.py',74),
  ('condition -> NAME clause value','condition',3,'p_condition','sintactical.py',77),
  ('operations -> NUMBER operand NUMBER','operations',3,'p_operations','sintactical.py',80),
  ('operations -> NAME SUMA SUMA','operations',3,'p_operations','sintactical.py',81),
  ('operations -> NAME RESTA RESTA','operations',3,'p_operations','sintactical.py',82),
  ('datatype -> NUMBER','datatype',1,'p_datatype_expr','sintactical.py',85),
  ('datatype -> STRING','datatype',1,'p_datatype_expr','sintactical.py',86),
  ('datatype -> CHAR','datatype',1,'p_datatype_expr','sintactical.py',87),
  ('operand -> SUMA','operand',1,'p_operand_expr','sintactical.py',90),
  ('operand -> RESTA','operand',1,'p_operand_expr','sintactical.py',91),
  ('operand -> MULTIPLICACION','operand',1,'p_operand_expr','sintactical.py',92),
  ('operand -> DIVISION','operand',1,'p_operand_expr','sintactical.py',93),
  ('bool -> TRUE','bool',1,'p_bool_expr','sintactical.py',96),
  ('bool -> FALSE','bool',1,'p_bool_expr','sintactical.py',97),
  ('type -> CONST','type',1,'p_type_expr','sintactical.py',100),
  ('type -> LET','type',1,'p_type_expr','sintactical.py',101),
  ('type -> VAR','type',1,'p_type_expr','sintactical.py',102),
  ('clause -> IGUALIGUAL','clause',1,'p_clause_expr','sintactical.py',105),
  ('clause -> DIFERENTE','clause',1,'p_clause_expr','sintactical.py',106),
  ('clause -> MAYORQUE','clause',1,'p_clause_expr','sintactical.py',107),
  ('clause -> MAYORIGUALQUE','clause',1,'p_clause_expr','sintactical.py',108),
  ('clause -> MENORQUE','clause',1,'p_clause_expr','sintactical.py',109),
  ('clause -> MENORIGUALQUE','clause',1,'p_clause_expr','sintactical.py',110),
  ('value -> NAME','value',1,'p_value_expr','sintactical.py',113),
  ('value -> NUMBER','value',1,'p_value_expr','sintactical.py',114),
  ('array -> type NAME IGUAL OPEN_BRACKET items CLOSE_BRACKET SEMICOLON','array',7,'p_array_expr','sintactical.py',117),
  ('array -> type NAME IGUAL NEW ARRAY OPEN_PARENTHESIS items CLOSE_PARENTHESIS SEMICOLON','array',9,'p_array_expr','sintactical.py',118),
  ('map -> iniciarMap','map',1,'p_map_expr','sintactical.py',121),
  ('map -> escribirMap','map',1,'p_map_expr','sintactical.py',122),
  ('map -> generarMap','map',1,'p_map_expr','sintactical.py',123),
  ('iniciarMap -> variable IGUAL NEW MAP OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON','iniciarMap',7,'p_iniciarMap_expr','sintactical.py',126),
  ('escribirMap -> variable IGUAL OPEN_BRACE claveValor CLOSE_BRACE','escribirMap',5,'p_escribirMap_expr','sintactical.py',129),
  ('claveValor -> clave COLON valor','claveValor',3,'p_claveValor_expr','sintactical.py',132),
  ('claveValor -> clave COLON valor COMMA claveValor','claveValor',5,'p_claveValor_expr','sintactical.py',133),
  ('clave -> datatype','clave',1,'p_clave_expr','sintactical.py',136),
  ('valor -> datatype','valor',1,'p_valor_expr','sintactical.py',139),
  ('valor -> dataStruct','valor',1,'p_valor_expr','sintactical.py',140),
  ('generarMap -> variable IGUAL OPEN_BRACE tuplas CLOSE_BRACE','generarMap',5,'p_generarMap_expr','sintactical.py',143),
  ('tuplas -> tupla','tuplas',1,'p_tuplas_expr','sintactical.py',146),
  ('tuplas -> tupla tuplas','tuplas',2,'p_tuplas_expr','sintactical.py',147),
  ('tupla -> OPEN_BRACKET datatype CLOSE_BRACKET','tupla',3,'p_tupla_expr','sintactical.py',150),
  ('tupla -> OPEN_BRACKET datatype COMMA datatype CLOSE_BRACKET','tupla',5,'p_tupla_expr','sintactical.py',151),
  ('arrayFn -> POINT POP OPEN_PARENTHESIS CLOSE_PARENTHESIS','arrayFn',4,'p_arrayFn_expr','sintactical.py',154),
  ('arrayFn -> POINT PUSH OPEN_PARENTHESIS argUnico CLOSE_PARENTHESIS','arrayFn',5,'p_arrayFn_expr','sintactical.py',155),
  ('arrayFn -> POINT UNSHIFT OPEN_PARENTHESIS argUnico CLOSE_PARENTHESIS','arrayFn',5,'p_arrayFn_expr','sintactical.py',156),
  ('argUnico -> NUMBER','argUnico',1,'p_argUnico_expr','sintactical.py',159),
  ('argUnico -> STRING','argUnico',1,'p_argUnico_expr','sintactical.py',160),
  ('argUnico -> NAME','argUnico',1,'p_argUnico_expr','sintactical.py',161),
  ('set -> type NAME IGUAL NEW SET OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON','set',8,'p_set_expr','sintactical.py',163),
  ('set -> type NAME IGUAL NEW SET OPEN_PARENTHESIS OPEN_BRACKET items CLOSE_BRACKET CLOSE_PARENTHESIS SEMICOLON','set',11,'p_set_expr','sintactical.py',164),
  ('set -> type NAME IGUAL NEW SET OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON','set',9,'p_set_expr','sintactical.py',165),
  ('set -> NAME IGUAL NEW SET OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON','set',7,'p_set_expr','sintactical.py',166),
  ('set -> NAME IGUAL NEW SET OPEN_PARENTHESIS OPEN_BRACKET items CLOSE_BRACKET CLOSE_PARENTHESIS SEMICOLON','set',10,'p_set_expr','sintactical.py',167),
  ('set -> NAME IGUAL NEW SET OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON','set',8,'p_set_expr','sintactical.py',168),
  ('methodsSet -> NAME POINT ADD OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON','methodsSet',7,'p_methodsSet_expr','sintactical.py',171),
  ('methodsSet -> NAME POINT DELETE OPEN_PARENTHESIS element CLOSE_PARENTHESIS SEMICOLON','methodsSet',7,'p_methodsSet_expr','sintactical.py',172),
  ('methodsSet -> NAME POINT CLEAR OPEN_PARENTHESIS CLOSE_PARENTHESIS SEMICOLON','methodsSet',6,'p_methodsSet_expr','sintactical.py',173),
  ('items -> numeros','items',1,'p_items_expr','sintactical.py',177),
  ('items -> cadena','items',1,'p_items_expr','sintactical.py',178),
  ('numeros -> NUMBER','numeros',1,'p_numeros_expr','sintactical.py',181),
  ('numeros -> NUMBER COMMA numeros','numeros',3,'p_numeros_expr','sintactical.py',182),
  ('cadena -> STRING','cadena',1,'p_cadena_expr','sintactical.py',185),
  ('cadena -> STRING COMMA cadena','cadena',3,'p_cadena_expr','sintactical.py',186),
  ('element -> STRING','element',1,'p_element_expr','sintactical.py',189),
  ('element -> NUMBER','element',1,'p_element_expr','sintactical.py',190),
  ('element -> NAME','element',1,'p_element_expr','sintactical.py',191),
]

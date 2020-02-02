# 특정 함수의 바이트코드 보기

import dis
from simul import ParticleSimulator
dis.dis(ParticleSimulator.evolve)
#  17           0 LOAD_CONST               1 (0.0001)
#               2 STORE_FAST               2 (timestep)

#  18           4 LOAD_GLOBAL              0 (int)
#               6 LOAD_FAST                1 (dt)
#               8 LOAD_FAST                2 (timestep)
#              10 BINARY_TRUE_DIVIDE
#              12 CALL_FUNCTION            1
#              14 STORE_FAST               3 (nsteps)

#  20          16 SETUP_LOOP             134 (to 152)
#              18 LOAD_GLOBAL              1 (range)
#              20 LOAD_FAST                3 (nsteps)
#              22 CALL_FUNCTION            1
#              24 GET_ITER
#         >>   26 FOR_ITER               122 (to 150)
#              28 STORE_FAST               4 (i)

#  21          30 SETUP_LOOP             116 (to 148)
#              32 LOAD_FAST                0 (self)
#              34 LOAD_ATTR                2 (particles)
#              36 GET_ITER
#         >>   38 FOR_ITER               106 (to 146)
#              40 STORE_FAST               5 (p)

#  23          42 LOAD_FAST                5 (p)
#              44 LOAD_ATTR                3 (x)
#              46 LOAD_CONST               2 (2)
#              48 BINARY_POWER
#              50 LOAD_FAST                5 (p)
#              52 LOAD_ATTR                4 (y)
#              54 LOAD_CONST               2 (2)
#              56 BINARY_POWER
#              58 BINARY_ADD
#              60 LOAD_CONST               3 (0.5)
#              62 BINARY_POWER
#              64 STORE_FAST               6 (norm)

#  24          66 LOAD_FAST                5 (p)
#              68 LOAD_ATTR                4 (y)
#              70 UNARY_NEGATIVE
#              72 LOAD_FAST                6 (norm)
#              74 BINARY_TRUE_DIVIDE
#              76 STORE_FAST               7 (v_x)

#  25          78 LOAD_FAST                5 (p)
#              80 LOAD_ATTR                3 (x)
#              82 LOAD_FAST                6 (norm)
#              84 BINARY_TRUE_DIVIDE
#              86 STORE_FAST               8 (v_y)

#  28          88 LOAD_FAST                2 (timestep)
#              90 LOAD_FAST                5 (p)
#              92 LOAD_ATTR                5 (ang_vel)
#              94 BINARY_MULTIPLY
#              96 LOAD_FAST                7 (v_x)
#              98 BINARY_MULTIPLY
#             100 STORE_FAST               9 (d_x)

#  29         102 LOAD_FAST                2 (timestep)
#             104 LOAD_FAST                5 (p)
#             106 LOAD_ATTR                5 (ang_vel)
#             108 BINARY_MULTIPLY
#             110 LOAD_FAST                8 (v_y)
#             112 BINARY_MULTIPLY
#             114 STORE_FAST              10 (d_y)

#  31         116 LOAD_FAST                5 (p)
#             118 DUP_TOP
#             120 LOAD_ATTR                3 (x)
#             122 LOAD_FAST                9 (d_x)
#             124 INPLACE_ADD
#             126 ROT_TWO
#             128 STORE_ATTR               3 (x)

#  32         130 LOAD_FAST                5 (p)
#             132 DUP_TOP
#             134 LOAD_ATTR                4 (y)
#             136 LOAD_FAST               10 (d_y)
#             138 INPLACE_ADD
#             140 ROT_TWO
#             142 STORE_ATTR               4 (y)
#             144 JUMP_ABSOLUTE           38
#         >>  146 POP_BLOCK
#         >>  148 JUMP_ABSOLUTE           26
#         >>  150 POP_BLOCK
#         >>  152 LOAD_CONST               0 (None)
#             154 RETURN_VALUE


dis.dis(ParticleSimulator.evolve_fast)
#  35           0 LOAD_CONST               1 (0.0001)
#               2 STORE_FAST               2 (timestep)

#  36           4 LOAD_GLOBAL              0 (int)
#               6 LOAD_FAST                1 (dt)
#               8 LOAD_FAST                2 (timestep)
#              10 BINARY_TRUE_DIVIDE
#              12 CALL_FUNCTION            1
#              14 STORE_FAST               3 (nsteps)

#  38          16 SETUP_LOOP             110 (to 128)
#              18 LOAD_FAST                0 (self)
#              20 LOAD_ATTR                1 (particles)
#              22 GET_ITER
#         >>   24 FOR_ITER               100 (to 126)
#              26 STORE_FAST               4 (p)

#  39          28 LOAD_FAST                2 (timestep)
#              30 LOAD_FAST                4 (p)
#              32 LOAD_ATTR                2 (ang_vel)
#              34 BINARY_MULTIPLY
#              36 STORE_FAST               5 (t_x_ang)

#  40          38 SETUP_LOOP              84 (to 124)
#              40 LOAD_GLOBAL              3 (range)
#              42 LOAD_FAST                3 (nsteps)
#              44 CALL_FUNCTION            1
#              46 GET_ITER
#         >>   48 FOR_ITER                72 (to 122)
#              50 STORE_FAST               6 (i)

#  41          52 LOAD_FAST                4 (p)
#              54 LOAD_ATTR                4 (x)
#              56 LOAD_CONST               2 (2)
#              58 BINARY_POWER
#              60 LOAD_FAST                4 (p)
#              62 LOAD_ATTR                5 (y)
#              64 LOAD_CONST               2 (2)
#              66 BINARY_POWER
#              68 BINARY_ADD
#              70 LOAD_CONST               3 (0.5)
#              72 BINARY_POWER
#              74 STORE_FAST               7 (norm)

#  43          76 LOAD_FAST                4 (p)
#              78 LOAD_ATTR                4 (x)
#              80 LOAD_FAST                5 (t_x_ang)
#              82 LOAD_FAST                4 (p)
#              84 LOAD_ATTR                5 (y)
#              86 BINARY_MULTIPLY
#              88 LOAD_FAST                7 (norm)
#              90 BINARY_TRUE_DIVIDE
#              92 BINARY_SUBTRACT
#              94 LOAD_FAST                4 (p)
#              96 STORE_ATTR               4 (x)

#  44          98 LOAD_FAST                4 (p)
#             100 LOAD_ATTR                5 (y)
#             102 LOAD_FAST                5 (t_x_ang)
#             104 LOAD_FAST                4 (p)
#             106 LOAD_ATTR                4 (x)
#             108 BINARY_MULTIPLY
#             110 LOAD_FAST                7 (norm)
#             112 BINARY_TRUE_DIVIDE
#             114 BINARY_ADD
#             116 LOAD_FAST                4 (p)
#             118 STORE_ATTR               5 (y)
#             120 JUMP_ABSOLUTE           48
#         >>  122 POP_BLOCK
#         >>  124 JUMP_ABSOLUTE           24
#         >>  126 POP_BLOCK
#         >>  128 LOAD_CONST               0 (None)
#             130 RETURN_VALUE
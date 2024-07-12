# 2024.07.03(Wed)
# Benchmark: Factor time in 4matrix
# Contributor: Chanyoung Ahn (https://github.com/cold-young)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Factor time /w best r-c case (dim / ratio / speedup)
# 256^3 TDM;    16,777,216	1.79E-07	1.1
tdm=[
63.259,
57.332,
45.183,
]
# mc2depi;      525,825	    7.60E-06	1.11
mc2depi=[
11.776,
8.237,
6.027,
4.563,
3.521,
3.332,
]
# torso1;       116,158	    6.31E-04	1.4 
torso1=[
4.189,
3.005,
2.101,
1.681,
1.59,
1.536,
]
# ecology1; 	1,000,000	5.00E-06	1.7
ecology1=[
11.736,
8.525,
5.771,
4.391,
3.663,
]
# stomach;	    213,360	    6.64E-05	3
stomach=[
23.503,
13.843,
8.831,
5.897,
4.406,
3.48,
]
# g7jac200;     59,310	    2.04E-04	5
g7jac200=[
111.288,
49.714,
23.515,
12.89,
7.73,
5.684,
5.638,
5.5,
5.416,
]
# ML_Laplace;	377,002	    1.94E-04	5
ml_laplace=[
62.391,
36.018,
21.036,
13.617,
9.239,
6.695,
6.184,
5.118,
4.358,
4.167,
]
# RM07R;    	381,689	    2.57E-04	8
rm07r=[
1032.632,
530.897,
282.813,
152.422,
89.001,
54.784,
40.895,
32.433,
30.117,
]
# twotone;  	120,750	    8.27E-05	19
twotone=[
185.118,
67.408,
28.043,
13.423,
7.282,
4.885,
4.665,
4.634,
]
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15

plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Times New Roman"

########################################################
fig, ax = plt.subplots()

x_tdm = [4, 8, 16]
x_mc2depi = [1, 2, 4, 8, 16, 32]
x_torso1 = [1, 2, 4, 8, 16, 32]
x_ecology1 = [1, 2, 4, 8, 16]
x_stomach = [1, 2, 4, 8, 16, 32]
x_g7jac200 = [1, 2, 4, 8, 16, 32, 64, 128, 256]
x_ml_laplace = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
x_rm07r = [2, 4, 8, 16, 32, 64, 128, 256, 512]
x_twotone = [1, 2, 4, 8, 16, 32, 64, 128]
x = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

x_values = {"tdm": x_tdm, 
           "ecology1": x_ecology1, 
           "mc2depi": x_mc2depi,
           "stomach": x_stomach,
           "twotone": x_twotone, 
           "ml_laplace": x_ml_laplace, 
           "g7jac200": x_g7jac200, 
           "rm07r": x_rm07r, 
           "torso1": x_torso1
           }

y_values = {"tdm": tdm, 
           "mc2depi": mc2depi,
           "torso1": torso1, 
           "ecology1": ecology1, 
           "g7jac200": g7jac200, 
           "ml_laplace": ml_laplace, 
           "rm07r": rm07r, 
           "twotone": twotone, 
           "stomach": stomach}

# labels = {"tdm": "tdm; N=16,777,216", 
#            "mc2depi": "mc2depi; N=525,825",
#            "torso1": "torso1; N=116,158", 
#            "ecology1": "ecology1; N=1,000,000", 
#            "g7jac200": "g7jac200; N=59,310", 
#            "ml_laplace": "ml_laplace; N=377,002", 
#            "rm07r": "rm07r; N=381,689", 
#            "twotone": "twotone; N=120,750", 
#            "stomach": "stomach; N=213,360"}
labels = {"tdm":        f"tdm; nnz=1.79E-07; speed rate={round(tdm[0]/tdm[-1],1)}", 
           "ecology1":  f"ecology1; nnz=5.00E-06; speed rate={round(ecology1[0]/ecology1[-1],1)}", 
           "mc2depi":   f"mc2depi; nnz=7.60E-06; speed rate={round(mc2depi[0]/mc2depi[-1],1)}",
           "twotone":   f"twotone; nnz=8.27E-05; speed rate={round(twotone[0]/twotone[-1],1)}", 
           "stomach":   f"stomach; nnz=6.64E-05; speed rate={round(stomach[0]/stomach[-1],1)}",
           "ml_laplace":f"ml_laplace; nnz=1.94E-04; speed rate={round(ml_laplace[0]/ml_laplace[-1],1)}", 
           "g7jac200":  f"g7jac200; nnz=2.04E-04; speed rate={round(g7jac200[0]/g7jac200[-1],1)}", 
           "rm07r":     f"rm07r; nnz=2.57E-04; speed rate={round(rm07r[0]/rm07r[-1],1)}", 
           "torso1":    f"torso1; nnz=6.31E-04; speed rate={round(torso1[0]/torso1[-1],1)}", 
        }

for key in x_values.keys():
    ax.plot(
        x_values[key],
        y_values[key],
        "o-",
        # color="firebrick",
        markeredgecolor="black",
        # label="Twotone (Nurion); N=120,750",
        label=labels[key],
    )

# ax.plot(
#     x_32,
#     nurion_n1_g7jac200,
#     "o-",
#     # "^--",
#     color="blue",
#     markeredgecolor="black",
#     label="g7jac200 (Nurion); N=59,310",
# )

# ax.plot(
#     x_8,
#     [4.193, 3.545, 2.893, 2.481],
#     "o-",
#     color="gold",
#     markeredgecolor="black",
#     label="torso1 (Nurion); N=116,158",
# )

# ax.plot(
#     x_32,
#     [23.503, 16.184, 10.579, 7.474, 5.975, 5.686],
#     "o-",
#     color="seagreen",
#     markeredgecolor="black",
#     label="stomach (Nurion);N=213,360",
# )


plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

plt.xlim(2**-1, 2**11)
# plt.ylim(10**0, 10**3)

plt.yscale("log")
ax.set_xscale("log")
ax.set_xticks(x)
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

plt.ylabel("Factorization time (sec)")
plt.xlabel("Number of cores")
plt.legend(loc="upper right", fontsize="12", frameon=False, labelspacing=0.1)
plt.show()

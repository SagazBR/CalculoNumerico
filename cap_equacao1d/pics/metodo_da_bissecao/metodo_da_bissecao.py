#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite http://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 03/2015
Last update: 07/2016 by phkonzen
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

#canvas
fig = plt.figure(figsize=(4,4), dpi=100, linewidth=0.0, facecolor="white")

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(-2,10)
ax.set_ylim(-5,5)

ax.set_xticks([])
ax.set_yticks([])

ax.set_frame_on(False)

ax.arrow(-2, 0, 12, 0, head_width=0.25,head_length=0.25, length_includes_head=True)
ax.text(9.5,-0.75,r"$x$",fontsize=14)

ax.arrow(0, -5, 0, 10, head_width=0.25, head_length=0.25, length_includes_head=True)
ax.text(-0.75, 4.5, r"$y$",fontsize=14)

def f(x):
    return -4 * np.cos ((x-1)/(np.pi))

a = 2
b = 8
x = np.linspace (a, b, 100, endpoint=True)

ax.plot(x, f(x))

#dashed lines
#(a, f(a))
ax.plot (a, f(a), 'ko', markersize=3)
ax.text (-1.5, f(a), r"$f(a)$", fontsize=14)
ax.plot ([-0.1, 0.1], [f(a), f(a)], color='black')
ax.plot ([0, a], [f(a), f(a)], color='gray', linestyle='dashed')
ax.plot ([a, a], [f(a), 0], color='gray', linestyle='dashed')
ax.plot ([a, a], [-0.1, 0.1], color='black')
ax.text (a - 0.25, 0.25, r"$a$", fontsize=14)

#(b, f(b))
ax.plot (b, f(b), 'ko', markersize=3)
ax.text (-1.5, f(b), r"$f(b)$", fontsize=14)
ax.plot ([-0.1, 0.1], [f(b), f(b)], color='black')
ax.plot ([0, b], [f(b), f(b)], color='gray', linestyle='dashed')
ax.plot ([b, b], [f(b), 0], color='gray', linestyle='dashed')
ax.plot ([b, b], [-0.1, 0.1], color='black')
ax.text (b - 0.25, -0.75, r"$b$", fontsize=14)


#(p, f(p))
p = (a + b)/2
ax.plot (p, f(p), 'ko', markersize=3)
ax.text (-1.5, f(p), r"$f(p)$", fontsize=14)
ax.plot ([-0.1, 0.1], [f(p), f(p)], color='black')
ax.plot ([0, p], [f(p), f(p)], color='gray', linestyle='dashed')
ax.plot ([p, p], [f(p), 0], color='gray', linestyle='dashed')
ax.plot ([p, p], [-0.1, 0.1], color='black')
ax.text (p - 0.25, 0.25, r"$p$", fontsize=14)

plt.show()

fig_file =  "metodo_da_bissecao"
#fig.savefig(fig_file+".svg", bbox_inches='tight', pad_inches=0.0)
fig.savefig(fig_file+".png", bbox_inches='tight', pad_inches=0.0)



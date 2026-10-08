
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Crear una sola ventana con cinco figuras
fig = plt.figure(figsize=(15, 10))

# =====================================
# FUNCION PARA DIBUJAR CADA FIGURA
# =====================================
def dibujar_figura(posicion, titulo, vertices, caras, aristas, color):

    ax = fig.add_subplot(posicion, projection="3d")

    # Dibujar las caras
    figura = Poly3DCollection(
        caras,
        alpha=0.5,
        facecolor=color,
        edgecolor="black"
    )
    ax.add_collection3d(figura)

    # Dibujar vertices y nombres
    nombres = [chr(65 + i) for i in range(len(vertices))]

    for nombre, v in zip(nombres, vertices):
        x, y, z = v
        ax.scatter(x, y, z, color="red", s=40)
        ax.text(x, y, z + 0.1, nombre, fontsize=9)

    # Dibujar aristas
    for inicio, fin in aristas:
        ax.plot(
            [inicio[0], fin[0]],
            [inicio[1], fin[1]],
            [inicio[2], fin[2]],
            color="black",
            linewidth=1.5
        )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(titulo)

    # Mantener proporciones similares
    ax.set_box_aspect((1, 1, 1))


# =====================================
# 1. CUADRADO
# =====================================
A = (-0.5, 1, 0)
B = (1, 2, 0)
C = (2.5, 1, 0)
D = (1, 0, 0)

v = [A, B, C, D]
c = [v]
a = [(A, B), (B, C), (C, D), (D, A)]

dibujar_figura(231, "1. Cuadrado", v, c, a, "skyblue")


# =====================================
# 2. TRIANGULO
# =====================================
A = (0, 0, 0)
B = (3, 0, 0)
C = (1.5, 2, 1)

v = [A, B, C]
c = [v]
a = [(A, B), (B, C), (C, A)]

dibujar_figura(232, "2. Triangulo", v, c, a, "orange")


# =====================================
# 3. CUBO
# =====================================
A = (0, 0, 0)
B = (2, 0, 0)
C = (2, 2, 0)
D = (0, 2, 0)
E = (0, 0, 2)
F = (2, 0, 2)
G = (2, 2, 2)
H = (0, 2, 2)

v = [A, B, C, D, E, F, G, H]

c = [
    [A, B, C, D],
    [E, F, G, H],
    [A, B, F, E],
    [B, C, G, F],
    [C, D, H, G],
    [D, A, E, H]
]

a = [
    (A, B), (B, C), (C, D), (D, A),
    (E, F), (F, G), (G, H), (H, E),
    (A, E), (B, F), (C, G), (D, H)
]

dibujar_figura(233, "3. Cubo", v, c, a, "lightgreen")


# =====================================
# 4. PIRAMIDE
# =====================================
A = (0, 0, 0)
B = (2, 0, 0)
C = (2, 2, 0)
D = (0, 2, 0)
E = (1, 1, 3)

v = [A, B, C, D, E]

c = [
    [A, B, C, D],
    [A, B, E],
    [B, C, E],
    [C, D, E],
    [D, A, E]
]

a = [
    (A, B), (B, C), (C, D), (D, A),
    (A, E), (B, E), (C, E), (D, E)
]

dibujar_figura(234, "4. Piramide", v, c, a, "salmon")


# =====================================
# 5. PRISMA TRIANGULAR
# =====================================
A = (0, 0, 0)
B = (2, 0, 0)
C = (1, 2, 0)
D = (0, 0, 2)
E = (2, 0, 2)
F = (1, 2, 2)

v = [A, B, C, D, E, F]

c = [
    [A, B, C],
    [D, E, F],
    [A, B, E, D],
    [B, C, F, E],
    [C, A, D, F]
]

a = [
    (A, B), (B, C), (C, A),
    (D, E), (E, F), (F, D),
    (A, D), (B, E), (C, F)
]

dibujar_figura(235, "5. Prisma triangular", v, c, a, "plum")


# Mostrar todas en una sola ventana
plt.tight_layout()
plt.show()

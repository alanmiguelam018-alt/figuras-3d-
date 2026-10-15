import matplotlib.pyplot as plt

fig = plt.figure("Jenny - estilo Minecraft", figsize=(7, 8))
ax = fig.add_subplot(111, projection="3d")


def bloque(x, y, z, ancho, fondo, alto, color):
    """Agrega un bloque rectangular al modelo."""
    ax.bar3d(
        x, y, z, ancho, fondo, alto,
        color=color, edgecolor="#33313b", linewidth=0.25, shade=True
    )


# Botas y pantalones
bloque(-0.60, -0.02, 0.00, 0.54, 0.78, 0.42, "#25232c")
bloque( 0.06, -0.02, 0.00, 0.54, 0.78, 0.42, "#25232c")
bloque(-0.56,  0.08, 0.42, 0.50, 0.58, 2.55, "#292633")
bloque( 0.06,  0.08, 0.42, 0.50, 0.58, 2.55, "#292633")

# Suéter morado, mangas y manos
bloque(-0.65, 0.08, 2.97, 1.30, 0.70, 1.72, "#713a91")
bloque(-1.00, 0.10, 3.52, 0.35, 0.62, 0.95, "#713a91")
bloque( 0.65, 0.10, 3.52, 0.35, 0.62, 0.95, "#713a91")
bloque(-1.00, 0.10, 2.98, 0.35, 0.62, 0.54, "#e7b28e")
bloque( 0.65, 0.10, 2.98, 0.35, 0.62, 0.54, "#e7b28e")
bloque(-0.18, 0.18, 4.65, 0.36, 0.42, 0.28, "#e7b28e")

# Cabeza y cabello castaño
bloque(-0.65, 0.05, 4.92, 1.30, 0.65, 1.48, "#e7b28e")
bloque(-0.72, 0.02, 6.20, 1.44, 0.72, 0.34, "#75452e")
bloque(-0.72, 0.00, 5.28, 0.25, 0.76, 0.98, "#75452e")
bloque( 0.47, 0.00, 5.28, 0.25, 0.76, 0.98, "#75452e")
bloque(-0.40, -0.03, 6.02, 0.80, 0.07, 0.22, "#75452e")

# Ojos azules y boca pequeña, al frente de la cara
bloque(-0.39, -0.05, 5.70, 0.20, 0.07, 0.20, "#43a9e8")
bloque( 0.19, -0.05, 5.70, 0.20, 0.07, 0.20, "#43a9e8")
bloque(-0.08, -0.05, 5.28, 0.20, 0.07, 0.08, "#8f4650")

# Flor rosa con centro amarillo en el cabello
bloque(0.46, -0.10, 6.45, 0.22, 0.12, 0.22, "#ff72a8")
bloque(0.68, -0.10, 6.45, 0.22, 0.12, 0.22, "#ff72a8")
bloque(0.57, -0.10, 6.34, 0.22, 0.12, 0.22, "#ff72a8")
bloque(0.57, -0.10, 6.56, 0.22, 0.12, 0.22, "#ff72a8")
bloque(0.57, -0.13, 6.45, 0.16, 0.08, 0.16, "#ffd34e")

ax.set_xlim(-1.35, 1.35)
ax.set_ylim(-0.85, 1.10)
ax.set_zlim(0, 7.05)
ax.set_box_aspect((2.7, 1.95, 7.05))
ax.set_proj_type("ortho")
ax.view_init(elev=9, azim=-72)
ax.set_axis_off()
fig.patch.set_facecolor("#f1f4f8")
ax.set_facecolor("#f1f4f8")
plt.tight_layout()
plt.show()

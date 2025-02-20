import arcade

WIDTH = 1200
HEIGHT = 1000

arcade.open_window(WIDTH, HEIGHT, "Prueba")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render() #comienzo dibujo

i = 0
star_points = [
        [i + 50, 900],  # Punto superior
        [i + 75, 800],  # Punto exterior derecho superior
        [i + 125, 800],  # Punto exterior derecho inferior
        [i + 100, 725],  # Punto interior derecho
        [i + 125, 650],  # Punto inferior derecho
        [i + 50, 700],  # Punto inferior central
        [i - 25, 650],  # Punto inferior izquierdo
        [i, 725],  # Punto interior izquierdo
        [i - 50, 800],  # Punto exterior izquierdo inferior
        [i + 25, 800]  # Punto exterior izquierdo superior
    ]

for i in range(800):
    arcade.draw_polygon_filled(
        [star_points], arcade.color.LIGHT_YELLOW)


i = 800
arcade.draw_polygon_filled([[i+20, i], [i+30, i+20], [i+40, i], [i+40, i+20], [i+60, i+30], [i+40, i+40], [i+30, i+60], [i+20, i+40], [i, i+30], [i+20, i+20]], arcade.color.LIGHT_YELLOW)
arcade.draw_rectangle_filled(400, 600, 150, 300, arcade.color.LIGHT_BLUE)
arcade.draw_rectangle_filled(550, 750, 100, 75, arcade.color.LIGHT_BLUE)
arcade.draw_lrtb_rectangle_filled(400, 550, 825, 750, arcade.color.LIGHT_BLUE)
arcade.draw_lrtb_rectangle_filled(315, 450, 550, 350, arcade.color.LIGHT_BLUE)
arcade.draw_lrtb_rectangle_filled(325, 425, 400, 250, arcade.color.LIGHT_BLUE)
arcade.draw_lrtb_rectangle_filled(325, 400, 250, 175, arcade.color.LIGHT_BLUE)
arcade.draw_lrtb_rectangle_filled(340, 390, 160, 125, arcade.color.LIGHT_BLUE)
arcade.draw_polygon_filled([[600,775], [600, 715], [700, 825], [650, 825]], arcade.color.LIGHT_BLUE)
arcade.draw_polygon_filled([[575,190], [575, 210], [590, 230], [610, 230]], arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(475, 575, 100, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(475, 725, 100, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(675, 825, 25, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(340, 180, 40, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(390, 250, 30, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(425, 325, 40, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(455, 400, 15, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(375, 815, 30, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(400, 875, 20, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(475, 865, 30, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(550, 825, 20, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(600, 250, 25, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(675, 255, 30, arcade.color.LIGHT_BLUE)
arcade.draw_triangle_filled(325, 750, 400,750,400,900, arcade.color.LIGHT_BLUE)
arcade.draw_triangle_filled(400, 900, 400,825,575,825, arcade.color.LIGHT_BLUE)
arcade.draw_triangle_filled(390, 125, 390,75,440,75, arcade.color.LIGHT_BLUE)
arcade.draw_triangle_filled(625, 200, 675,200,650,250, arcade.color.LIGHT_BLUE)



#Triangulo = arcade.draw_triangle_filled(400, 400, 600,400,600,600,arcade.color.LIGHT_BLUE)
#Rectangulo = arcade.draw_rectangle_filled(500, 500, 400, 800, arcade.color.LIGHT_BLUE)
#Circulo = arcade.draw_circle_filled(500, 500, 250, arcade.color.LIGHT_BLUE)
#Poligono = arcade.draw_polygon_filled([[200,400], [200, 300], [500, 600], [400, 600]], arcade.color.LIGHT_BLUE)

arcade.finish_render() #final dibujo
arcade.run()
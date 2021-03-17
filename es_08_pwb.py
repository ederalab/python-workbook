#widget and gizmos
#widget = 75 grams - gizmo = 112 grams
#read the number of widget and gizmos and display the total weight
widget = 75
gizmo = 112
widget_num = int(input("How many widgets? "))
gizmo_num = int(input("How many gizmos? "))

total = (widget_num * widget) + (gizmo_num * gizmo)
print("The total weight is %1i grams" % total)

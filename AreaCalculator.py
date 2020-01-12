"""
This program is to receive input from users which can then be used in calculating areas of shapes, namely: triangles and circles
"""
print 'The calculator is on!'

option = raw_input('Enter C for Circle or T for Triangle: ')
if option == 'C':
  radius = float(raw_input('We\'ll need a radius for that: '))
  area = 3.14159 * radius ** 2
  print 'The area of the circle is ' + str(area)
  
elif option == 'T':
  base = float(raw_input('What is the base of this triangle?: '))
  height = float(raw_input('Height?: '))
  area = 0.5 * base * height
  print 'The area is %f' % (area)

else: 
  print 'The shape you have selected is invalid or you have failed to provide an input'

print 'Oh, we done done'
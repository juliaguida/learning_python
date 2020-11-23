#Write a program to work out if you should visit planet Mars based on whether you want to visit and if you can afford it:

visit_mars = input('Would you like to vist Mars? y/n ')
is_willing_go = visit_mars == 'y'
can_you_afford = input('Can you affort visiting Mars? y/n')
can_afford = can_you_afford == 'y'
should_visit_mars = is_willing_go and can_afford
print('You should visit Mars: {}'.format(should_visit_mars))

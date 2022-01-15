import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''



# Findall function to get all of the 'sit-amet' or 'sit:amet' in the string
occurences_sit_amet = re.findall('sit.amet', lorem_ipsum)

# Display the number of 'sit-amet' or 'sit:amet' in the string
print(len(occurences_sit_amet))



# Findall function to get all of the non-alphanumeric characters in the string 
results = re.findall('\W', lorem_ipsum)

# Display the number of non-alphanumeric characters in the string
print(len(results))



# Sub function to replace sit:amet and sit-amet with sit amet
replace_results = re.sub('sit[-:]amet', 'sit amet', lorem_ipsum)

# Findall function to get all of the 'sit amet' in the string
occurrance_sit_amet = re.findall('sit amet', replace_results)

# Display the number of 'sit amet' in the string
print(len(occurrance_sit_amet))
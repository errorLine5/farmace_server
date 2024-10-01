import re

pattern = re.compile('[^A-Za-z0-9.@_-]')
def sanitize(value): #allow @ and . - ! _ and numbers and letters
 sanitized = re.sub(pattern, '', value)
 return sanitized




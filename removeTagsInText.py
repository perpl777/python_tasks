s = "<p><div>helloooуууууу</div></p>"

while ">" in s:
    index1 = s.find("<")
    index2 = s.find(">")
    s = s.replace(s[index1:index2 + 1], "")

print(s)        

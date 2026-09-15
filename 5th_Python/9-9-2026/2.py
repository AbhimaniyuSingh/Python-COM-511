# Write a Python program to detect whether aa comment is spam or not. A comment should be treated as spam if it conatin any of these keywords: "make a lot of money ", "buy now","subscribe this" or "click this".
a = input("comment: ")
if "buy now" in a or "click this" in a:
    print("Spam")
else:
    print("Not Spam")
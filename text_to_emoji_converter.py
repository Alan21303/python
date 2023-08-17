message = input("Enter the message : ")
words = message.split(" ")
emojis = {
  ":)":"😊",
  ":(":"😥",
  ">:(":"😡",
  "B-)":"😎"
}
output=""
for word in words:
  output += " "+ emojis.get(word,word) +" "
print(output)

def emoji_converter(message):
    message = text.split(' ')
    emoji = {
        ':)' :'😀',
        ':(' : '😔',
        ':|' : '😐'
    }
    output = ''
    for word in message:
        output += emoji.get(word, word) + ' '
    return output

text = input("Enter your message : ")
output = emoji_converter(text)
print(output)
print("Finish")
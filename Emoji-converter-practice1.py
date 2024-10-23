text = input("> ")
message = text.split(' ')
emoji = {
    ':)' :'😀',
    ':(' : '😔',
    ':|' : '😐'
}
output = ''
for word in message:
    output += emoji.get(word, word) + ' '
print(output)
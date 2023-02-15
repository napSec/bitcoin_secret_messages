import codecs

# Prompt user to enter the message to be encoded
message = input("message to be encoded")

# Convert message to hexadecimal
hex_message = codecs.encode(message.encode(), 'hex_codec')

# Convert hexadecimal message to a string
hex_message_str = hex_message.decode()

# Create `OP_RETURN` script
script = "6a" + hex(len(hex_message) // 2)[2:] + hex_message_str

# Print script
print("The OP_RETURN script for the message is: ", script)

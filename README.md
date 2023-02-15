
<html>
</head>
<body>
<h1>BTC Hidden Message Generator</h1>

<p>This Python script demonstrates how to create an <em><code>OP_RETURN</code></em> script with an encoded message in hexadecimal format for the Bitcoin blockchain. &nbsp; &nbsp; &nbsp; An <em>OP_RETURN</em> is a special transaction output used in the Bitcoin blockchain that allows the inclusion of data in a transaction without transferring any bitcoins:</p>

<h2>Usage</h2>

<p>&nbsp;</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $ <code>git clone https://github.com/napSec/bitcoin_secret_messages.git</code></p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $ <code>cd bitcoin_secret_messages</code></p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $ <code>python3 op_return_generator.py</code></p>

<pre>
<small><big>The script can be used as the data to be included in an <em><strong>OP_RETURN</strong></em> output of a Bitcoin transaction.
When the transaction is added to the blockchain, the <em><strong>OP_RETURN</strong></em> output with the encoded message will be
stored permanently on the blockchain, allowing anyone to access and verify the data.</big></small>

<span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif">
What the script does:

Imports <em>codecs</em> library, used to encode/decode data in different formats.</span></span>

<span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif">Sets your message to be encoded as the string  &quot;<em>This secret message is is on the blockchain!</em>&quot;.<span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif"> </span></span></span></span></span></span>

<span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif">Converts message to hexadecimal using <em>encode()method</em> of the string object, this converts the string to bytes, uses the hex_codec <strong><em>codec</em></strong> to encode bytes in hexadecimal format.</span></span></span></span></span></span>

<span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif">Converts the hexadecimal message from bytes to a string using the decode() method of the bytes object.</span></span>

<span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif">Creates the <strong><em>OP_RETURN</em></strong> script by concatenating the opcode 6a with the length of the hexadecimal message </span></span>
<span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif">in bytes represented in hexadecimal format, followed by the hexadecimal message itself.</span></span>

<span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:12px"><span style="font-family:Arial,Helvetica,sans-serif"> Prints the <strong><em>OP_RETURN</em></strong> script to be used in the output transaction on the bitcoin blockchain.</span></span></span></span></pre>

<h4>&nbsp;</h4>

<p>&nbsp;
<h2>License</h2>
</p>

<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>

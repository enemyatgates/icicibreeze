import json
import hashlib
from datetime import datetime

# App related Secret Key
secret_key = 'your_SECRET_goes_here'

# 'body' is the request-body of your current request
payload = json.dumps(body, separators=(',', ':'))

#time_stamp & checksum generation for request-headers
time_stamp = datetime.utcnow().isoformat()[:19] + '.000Z'
checksum = hashlib.sha256((time_stamp+payload+secret_key).encode("utf-8")).hexdigest()
var crypto = require('crypto');

var secret = 'your_SECRET_goes_here';
var time_stamp = new Date().getTime().toString();
var data = JSON.stringify(body); // 'body' is the body of the current request
var rawChecksum = time_stamp+'\r\n'+data;

var checksum = crypto.createHmac('sha256', secret).update(rawChecksum);

// to base64
checksum.digest('base64');
//You might need to import the following

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.NoSuchAlgorithmException;
import java.security.InvalidKeyException;
import javax.xml.bind.DatatypeConverter;


//The following code generates the checksum

try {
    String secret = "your_SECRET_goes_here";

    // 'body' is the body of the current request
    String data = body.toString();

    String rawChecksum = timeStamp+"\r\n"+data;

    Mac hasher = Mac.getInstance("HmacSHA256");
    hasher.init(new SecretKeySpec(secret.getBytes(), "HmacSHA256"));

    byte[] checksum = hasher.doFinal(rawChecksum.getBytes());

    DatatypeConverter.printBase64Binary(checksum);
}
catch (NoSuchAlgorithmException e) {}
catch (InvalidKeyException e) {}
//You might need to import the following

using System;
using System.Security.Cryptography;
using System.Text;

//The following code generates the checksum

string secret = "yourSECRETgoeshere";
string timeStamp = DateTimeOffset.Now.ToUnixTimeSeconds();

// 'body' is the body of the current request
string data = body.ToString();

string rawChecksum = timeStamp+"\r\n"+data;

byte[] secretByte = new ASCIIEncoding().GetBytes(secret);
byte[] checksumBytes = new ASCIIEncoding().GetBytes(rawChecksum);

byte[] checksum = new HMACSHA256(secretByte).ComputeHash(checksumBytes);

Convert.ToBase64String(checksum);

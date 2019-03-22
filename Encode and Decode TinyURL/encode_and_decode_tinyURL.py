# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    
    i = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        global i
        crypto = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        self.i[crypto] = longUrl
        return "http://tinyurl.com/" + crypto
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        crypto = shortUrl.split("/")[-1]
        return self.i[crypto]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

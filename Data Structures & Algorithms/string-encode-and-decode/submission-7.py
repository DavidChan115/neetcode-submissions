class Solution:

    def encode(self, strs: List[str]) -> str:
        # input = strs=["neet", "code", "love", "you"]
        encoded = []
        for i in strs:
            # unsupported operand type(s) for +: 'int' and 'str'
            # len(i)係int, 唔可以就咁+ string
            encoded.append(str(len(i)) + "#" + i)
            # encoded.append("#")
            # encoded.append(i)


        # since the encode function needs to return a string, we have to convert the encoded list to string before returning
        encoded_string = "".join(encoded)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded = []
        start_track = 0

        while start_track < len(s):
            end_track = start_track
            while s[end_track] != "#":
                end_track += 1

            length = int(s[start_track:end_track])

            start_track = end_track + 1
            end_track = start_track + length

            decoded.append(s[start_track:end_track])

            start_track = end_track
        return decoded






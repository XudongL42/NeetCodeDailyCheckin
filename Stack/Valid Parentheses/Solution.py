class Solution:
    def isValid(self, s: str) -> bool:
        open_char = set(['(', '{', '['])
        close_char = set([')', '}', ']'])
        char_stack = []
        for char in s:
            if char in open_char:
                char_stack.append(char)
            elif char in close_char:
                # if there's no matching opening bracket available
                if not char_stack:
                    return False
                pop_char = char_stack.pop()
                # pop_char is an opening bracket, char is a closing bracket
                if not self.isMatch(pop_char, char):
                    return False
            else:
                raise Exception(f"not supported char {char}")
        return True if len(char_stack) == 0 else False
    
    def isMatch(self, opening: str, closing: str) -> bool:
        """Return True if `opening` and `closing` are matching brackets."""
        return (
            (opening == '(' and closing == ')')
            or (opening == '{' and closing == '}')
            or (opening == '[' and closing == ']')
        )
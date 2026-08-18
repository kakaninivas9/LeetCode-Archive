class Solution {

    /**
     * @param String $s
     * @return String
     */
    public function longestPalindrome(string $stringToCheck): string
    {
        // whole word is a palindrome; also works for single chars
        if ($stringToCheck === strrev($stringToCheck)) {
            return $stringToCheck;
        }

        $length = strlen($stringToCheck);

        $result = '';
        $maxLen = 1;

        for ($i = 0; $i < $length; ++$i) {
            for ($len = $maxLen; $len <= $length; ++$len) {
                $subStart = $i - ($len >> 1);

                if ($subStart < 0 || $subStart + $len > $length)
                    break;

                $sub = substr($stringToCheck, $subStart, $len);

                if ($sub === strrev($sub)) {
                    $result = $sub;
                    $maxLen = strlen($sub);
                } elseif ($maxLen + 1 < $len) {
                    break;
                }
            }
        }

        return $result;
    }
}
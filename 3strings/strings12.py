"234567" !=2345 # true
# 234567 does not equal 2345, so it is true.

"234567">23456 # typeerror
# typeerror thrown because < > not supported between strings and integers, can only instead use != (not equal) or == (equal)

"234567" < str(2346) # true
# the str(2346) will return '2346' and the comparison will be done character by character up to the 4th character. Since 4th character of '2346' is 6, it is greater than 4th character of 234567, which is 5. 

"234567" > str(2346) # false
# fales because str(2346) will return '2346' and compare to 2345 of 234567. since 5 > 6 it is false comparison.
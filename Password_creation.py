Question: A password manager wants to create new passwords using two strings given by the user, then combined to create a harder-to-guess combination. Given two strings, interleave the characters of the strings to create a new string. Beginning with an empty string, alternately append a character from string a and from string b. If one of the strings is exhausted before the other, append the remaining letters from the other string all at once. The result is the new password.

Solution: http://pythontutor.com/live.html#code=def%20merge%28a,b%29%3A%0A%20%20%20%20char_pairs%20%3D%20list%28zip%28a,b%29%29%0A%20%20%20%20%0A%20%20%20%20print%28char_pairs%20%29%0A%20%20%20%20%0A%20%20%20%20temp%20%3D%20%5B%5D%0A%20%20%20%20%0A%20%20%20%20for%20a_pair%20in%20char_pairs%3A%0A%20%20%20%20%20%20%20%20temp.append%28''.join%28a_pair%29%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20print%28temp%29%0A%20%20%20%20%0A%20%20%20%20return_result%20%3D%20''.join%28temp%29%0A%20%20%20%20%0A%20%20%20%20print%28return_result%29%0A%20%20%20%20%0A%20%20%20%20return%20return_result%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Aa%20%3D%20'hackerrank'%0Ab%20%3D%20'mountain'%0Amerge%28a,b%29&cumulative=false&curInstr=17&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
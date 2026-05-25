#Input: num = 3749
#Output: "MMMDCCXLIX"

class Solution(object):
    def intToRoman(self, nums):
        """
        :type num: int
        :rtype: str
        """
        roman = []
        new_val = nums
        if new_val == 0:
            return 0
        while new_val != 0:
            converting_str_number = str(new_val)
            dist = len(converting_str_number) - 1
            divided_int = int(converting_str_number[0] + "0"*dist)
            new_val = int(converting_str_number) - divided_int

            copy_divided_int = divided_int
            if copy_divided_int >= 1000:            #handles romans of numbers above 1000
                div1 = copy_divided_int // 1000
                rom1 = 'M'*div1
                roman.append(rom1)
                continue
            
            if copy_divided_int >= 100 and copy_divided_int < 1000:         #handles roman from 100-999
                if copy_divided_int == 500:                                 #handles  from 500-999
                    roman.append('D')
                    continue
                elif copy_divided_int > 500:
                    if copy_divided_int == 900:
                        roman.append('CM')
                        continue
                    rem2 = copy_divided_int % 500
                    div2 = copy_divided_int // 500
                    rom2 = 'D'*div2
                    roman.append(rom2)    
                    if rem2 >=100 and rem2 < 500:                        
                        div3 = rem2 // 100
                        rom3 = 'C'*div3
                        roman.append(rom3)
                        continue
                else:                                       #handles from 100-499
                    if copy_divided_int == 100:          
                        roman.append('C')
                        continue

                    if copy_divided_int == 400:
                        roman.append('CD')
                        continue
                    else:
                        div5 = copy_divided_int // 100
                        rom5 = 'C'*div5
                        roman.append(rom5)
                        continue 
            if copy_divided_int >= 10 and copy_divided_int < 100:
                if copy_divided_int == 50:
                    roman.append('L')
                    continue
                elif copy_divided_int > 50:
                    if copy_divided_int == 90:
                        roman.append('XC')
                        continue
                    rem4 = copy_divided_int % 50
                    div4 = copy_divided_int // 50
                    rom4 = 'L'*div2
                    roman.append(rom2)    
                    if rem4 >=10 and rem4 < 50:                        
                        div6 = rem2 // 10
                        rom4 = 'X'*div6
                        roman.append(rom3)
                        continue
                else:                                       
                    if copy_divided_int == 10:          
                        roman.append('X')
                        continue

                    if copy_divided_int == 40:
                        roman.append('XL')
                        continue
                    else:
                        div7 = copy_divided_int // 10
                        rom7 = 'X'*div7
                        roman.append(rom7)
                        continue 
            if copy_divided_int >= 1 and copy_divided_int < 10:    #handles 1-9
                if copy_divided_int == 5:
                    roman.append('V')
                    continue
                elif copy_divided_int > 5:
                    if copy_divided_int == 9:
                        roman.append('IX')
                        continue
                    rem8 = copy_divided_int % 5
                    div8 = copy_divided_int // 5
                    rom8 = 'V'*div8
                    rom9 = 'I'*rem8
                    roman.append(rom8)    
                    roman.append(rom9)
                    continue
                else:                                       
                    if copy_divided_int == 4:          
                        roman.append('IV')
                        continue

                    else:
                        rem10 = copy_divided_int % 5
                        rom10 = 'I'*rem10
                        roman.append(rom10)
                        continue 

        roman_text = "".join(roman)            
        print(roman_text)

                
     
                

sol = Solution()
sol.intToRoman(3749)


        
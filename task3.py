good=r"""
,adPPYba, 8b,dPPYba,  8b       d8  
I8[    "" 88P'    "8a `8b     d8'  
 `"Y8ba,  88       d8  `8b   d8'   
aa    ]8I 88b,   ,a8"   `8b,d8'    
`"YbbdP"' 88`YbbdP"'      Y88'     
          88              d8'      
          88             d8'    
    """
bad=r"""
,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \__
        """
guard_awake = False
if guard_awake:
    outcome = "Doom: YOU HAVE BEEN CAUGHT"
    print(bad)
else:
    outcome = "Shadow: SNEAK PAST"
    print(good)
print(outcome)
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 22:20:30 2021

@author: 97250
"""

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

y = json.loads(sampleJson)

print(y["company"]["employee"]["payable"]["salary"]) # Access the nested “salary” key from the JSON-string above.

# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.

# Save the dictionary as JSON to a file.


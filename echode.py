
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

class echode:
	
	def encryp(text,key1,key2):
		
		output = ""
		text = text.lower()
		
		for i in text:
			index = 0
			if i != " ":
				for k in alphabet:
					if k == i:
						output += str((key1 * index)+key2)
						output += "-"
						break
						
					index += 1
			else:
					output += "+"
					
		return output
		
		
	def decryp(text,key1,key2):
		text = text.split("+")
		output = ""
		
		for i in range(0,len(text)):
			text2 = text[i].split("-")
			
			for k in text2:
				if k != " " and k != "":
					output += alphabet[int((int(k)-key2)/key1)]
				
			output += " "

		return output
		
		

			
		
	
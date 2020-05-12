def main():

	myGroceryList = ["apples","bananas","milk","eggs","bread","hamburgers","hotdogs","ketchup","grapes","tilapia","sweet potatoes","cereal","paper plates","napkins","cookies","ice cream","cherries","shampoo"]

	vegetables = ["sweet potatoes","carrots","broccoli","spinach","onions","mushrooms","peppers"]
	fruit = ["bananas","apples","grapes","plubms","cherries","ice cream"]
	cold_items = ["eggs","milk","orange juice","cheese","ice cream"]
	proteins = ["turkey","tilapia","hamburgers","hotdogs","pork chop","ham","meatballs"]
	boxed_items = ["pasta","cereal","oatmeal","cookies","ketchup","bread"]
	paper_products = ["toilet paper","paper plates","napkins","paper towels"]
	toiletry_items = ["toothbrush","toothpaste","deodorant","shampoo","soap"]

	my_vegs = []
	my_fruits = []
	my_cold_items = []
	my_proteins = []
	my_boxed_items = []
	my_paper_products = []
	my_toiletry_items = []

	for i in myGroceryList:
		if(i in vegetables):
			my_vegs.append(i)
		elif(i in fruit):
			my_fruits.append(i)
		elif(i in cold_items):
			my_cold_items.append(i)
		elif(i in proteins):
			my_proteins.append(i)
		elif(i in boxed_items):
			my_boxed_items.append(i)
		elif(i in my_paper_products):
			my_paper_products.append(i)
		elif(i in toiletry_items):
			my_toiletry_items.append(i)

	print("My vegetable list: ",my_vegs)
	print("My fruit list: ",my_fruits)
	print("My cold item list: ",my_cold_items)
	print("My protein list: ",my_proteins)
	print("My boxed item list: ",my_boxed_items)
	print("My paper product list: ",my_paper_products)
	print("My toiletry item list: ",my_toiletry_items)




if __name__ == '__main__':
	main()	
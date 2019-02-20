start_urls = ["https://fundrazr.com/find?category=Health"]

npages = 2

# This mimics getting the pages using the next button. 
for i in range(2, npages + 2 ):
	start_urls.append("https://fundrazr.com/find?category=Health&page="+str(i)+"")
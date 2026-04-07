# Blog views list
blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

# Initialize variables
total_views = 0
trending_count = 0

# Loop through views
for views in blog_views:
    if views > 1000:
        print(views, "- Trending")
        trending_count += 1
    elif 500 <= views <= 1000:
        print(views, "- Average")
    else:
        print(views, "- Low Traffic")
    
    total_views += views

# Print results
print("Total views:", total_views)
print("Number of Trending posts:", trending_count)
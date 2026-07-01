from pathlib import Path
path = Path('action.php')
text = path.read_text(encoding='utf-8')
old_blocks = [
    "\t\t\t\t\t\t\t\t$rating_query = \"SELECT ROUND(AVG(rating),1) AS avg_rating  FROM reviews WHERE product_id='$pro_id '\";\n\t\t\t\t\t\t\t\t$run_review_query = mysqli_query($con,$rating_query);\n\t\t\t\t\t\t\t\t$review_row = mysqli_fetch_array($run_review_query);\n\t\t\t\t\t\t\t\tif($review_row > 0){\n\t\t\t\t\t\t\t\t\t$avg_count=$review_row[\"avg_rating\"];\n\t\t\t\t\t\t\t\t\t$i=1;\n\t\t\t\t\t\t\t\t\twhile($i <= round($avg_count)){\n\t\t\t\t\t\t\t\t\t\t$i++;\n\t\t\t\t\t\t\t\t\t\t echo'\n\t\t\t\t\t\t\t\t\t\t <i class=\"fa fa-star\"></i>';\n\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t\t$i=1;\n\t\t\t\t\t\t\t\t\twhile($i <= 5-round($avg_count)){\n\t\t\t\t\t\t\t\t\t\t$i++;\n\t\t\t\t\t\t\t\t\t\t echo'\n\t\t\t\t\t\t\t\t\t\t <i class=\"fa fa-star-o empty\"></i>';\n\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t}\n",
    "\t\t\t\t\t\t$rating_query = \"SELECT ROUND(AVG(rating),1) AS avg_rating  FROM reviews WHERE product_id='$pro_id '\";\n\t\t\t\t\t\t$run_review_query = mysqli_query($con,$rating_query);\n\t\t\t\t\t\t$review_row = mysqli_fetch_array($run_review_query);\n\t\t\t\t\t\tif($review_row > 0){\n\t\t\t\t\t\t\t$avg_count=$review_row[\"avg_rating\"];\n\t\t\t\t\t\t\t$i=1;\n\t\t\t\t\t\t\twhile($i <= round($avg_count)){\n\t\t\t\t\t\t\t\t$i++;\n\t\t\t\t\t\t\t\t echo'\n\t\t\t\t\t\t\t\t <i class=\"fa fa-star\"></i>';\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t$i=1;\n\t\t\t\t\t\t\twhile($i <= 5-round($avg_count)){\n\t\t\t\t\t\t\t\t$i++;\n\t\t\t\t\t\t\t\t echo'\n\t\t\t\t\t\t\t\t <i class=\"fa fa-star-o empty\"></i>';\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n",
]
new_block = "\t\t\t\t\t\t\t\t$rating_query = \"SELECT ROUND(AVG(rating),1) AS avg_rating  FROM reviews WHERE product_id='$pro_id '\";\n\t\t\t\t\t\t\t\t$run_review_query = mysqli_query($con,$rating_query);\n\t\t\t\t\t\t\t\t$review_row = mysqli_fetch_array($run_review_query);\n\t\t\t\t\t\t\t\tif($review_row > 0){\n\t\t\t\t\t\t\t\t\t$avg_count=$review_row[\"avg_rating\"];\n\t\t\t\t\t\t\t\t\t$avg_count = is_numeric($avg_count) ? floatval($avg_count) : 0;\n\t\t\t\t\t\t\t\t\t$filledStars = round($avg_count);\n\t\t\t\t\t\t\t\t\t$emptyStars = max(0, 5 - $filledStars);\n\t\t\t\t\t\t\t\t\t$i=1;\n\t\t\t\t\t\t\t\t\twhile($i <= $filledStars){\n\t\t\t\t\t\t\t\t\t\t$i++;\n\t\t\t\t\t\t\t\t\t\t echo'\n\t\t\t\t\t\t\t\t\t\t <i class=\"fa fa-star\"></i>';\n\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t\t$i=1;\n\t\t\t\t\t\t\t\t\twhile($i <= $emptyStars){\n\t\t\t\t\t\t\t\t\t\t$i++;\n\t\t\t\t\t\t\t\t\t\t echo'\n\t\t\t\t\t\t\t\t\t\t <i class=\"fa fa-star-o empty\"></i>';\n\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t}\n"
count = 0
for old in old_blocks:
    if old in text:
        text = text.replace(old, new_block)
        count += 1
path.write_text(text, encoding='utf-8')
print(f'patched {count} blocks')

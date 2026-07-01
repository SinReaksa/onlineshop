from pathlib import Path
path = Path('action.php')
text = path.read_text(encoding='utf-8')
old = '''							$rating_query = "SELECT ROUND(AVG(rating),1) AS avg_rating  FROM reviews WHERE product_id='$pro_id '";
							$run_review_query = mysqli_query($con,$rating_query);
							$review_row = mysqli_fetch_array($run_review_query);
							if($review_row > 0){
								$avg_count=$review_row["avg_rating"];
								$i=1;
								while($i <= round($avg_count)){
									$i++;
									echo'
										<i class="fa fa-star"></i>';
								}
								$i=1;
								while($i <= 5-round($avg_count)){
									$i++;
									echo'
										<i class="fa fa-star-o empty"></i>';
								}
							}
'''
new = '''							$rating_query = "SELECT ROUND(AVG(rating),1) AS avg_rating  FROM reviews WHERE product_id='$pro_id '";
							$run_review_query = mysqli_query($con,$rating_query);
							$review_row = mysqli_fetch_array($run_review_query);
							if($review_row > 0){
								$avg_count=$review_row["avg_rating"];
								$avg_count = is_numeric($avg_count) ? floatval($avg_count) : 0;
								$filledStars = round($avg_count);
								$emptyStars = max(0, 5 - $filledStars);
								$i=1;
								while($i <= $filledStars){
									$i++;
									echo'
										<i class="fa fa-star"></i>';
								}
								$i=1;
								while($i <= $emptyStars){
									$i++;
									echo'
										<i class="fa fa-star-o empty"></i>';
								}
							}
'''
count = text.count(old)
if count == 0:
    raise SystemExit('old block not found')
text = text.replace(old, new)
path.write_text(text, encoding='utf-8')
print(f'replaced {count} occurrence(s)')
